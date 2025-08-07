from flask import Flask, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
# Create a new client and connect to the server
client = MongoClient(MONGO_URI)
# Send a ping to confirm a successful connection
db = client.test
collection = db['flask_tutorial']

app = Flask(__name__)


# submit route
@app.route("/api/submit", methods=['POST'])
def submit():
  
    data = dict(request.json)
    collection.insert_one(data)
    
    # Redirect to the 'show' route after successful insert
    return redirect(url_for('show'))

# show page with all registered data
@app.route("/api/show")
def show():
    all_data = list(collection.find({}, {'_id': 0}))  # Get data as list, omit _id
    data = {
        "data": all_data
    }
    print(data)  # Logs the dictionary, fine to do for debugging

    return jsonify(data)  # Properly convert dict to JSON response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="9000",debug=True)


