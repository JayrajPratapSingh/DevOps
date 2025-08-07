from flask import Flask, jsonify
import json

app = Flask(__name__)

# Route to return data from JSON file
@app.route("/api", methods=["GET"])
def get_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
