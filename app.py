from flask import Flask, render_template, jsonify
import json, os
from datetime import datetime

app = Flask(__name__)

def get_today_filename():
    return datetime.now().strftime("%Y-%m-%d") + ".json"

def get_batch_data():
    path = os.path.join("data", get_today_filename())
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {"donatur": []}

@app.route("/")
def index():
    batch = get_batch_data()
    return render_template("index.html", donatur=batch["donatur"], target_time="2025-06-17T23:00:00")

@app.route("/data")
def live_data():
    batch = get_batch_data()
    return jsonify(batch["donatur"])

if __name__ == "__main__":
    app.run(debug=True)
