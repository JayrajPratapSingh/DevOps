from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import requests

app = app = Flask(__name__)
BACKEND_URL = 'http://192.168.227.173:9000/api'

# signup form rendering
@app.route("/")
def signup():
    day_of_weak = datetime.today().strftime("%A")
    print(day_of_weak)
    return render_template("index.html", day_of_weak=day_of_weak)

@app.route("/api/submit", methods=['POST'])
def submit():
    form_data = dict(request.form)
    try:
        response = requests.post(BACKEND_URL + "/submit", json=form_data)
        response.raise_for_status()
    except requests.RequestException as e:
        # logging.error(f"Error posting data to backend: {e}")
        # Optionally handle error display or redirect to error page
        return "Error submitting data", 500
    return redirect(url_for('view'))

@app.route("/get_data", methods=["GET"])
def view():
    response = requests.get(BACKEND_URL + "/show")  # Note /api/show in backend
    print(response)  # Logs response object, e.g. <Response [200]>
    
    data = response.json()  # Extract JSON payload
    records = data.get('data', [])  # Get the list of records, default empty
    
    return render_template("show.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)


