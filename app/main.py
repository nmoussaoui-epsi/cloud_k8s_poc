from flask import Flask, jsonify, render_template
import sqlite3
import os
import time

app = Flask(__name__, static_folder="static", template_folder="templates")

DB_PATH = os.getenv("DB_PATH", "database.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/read_db", methods=["GET"])
def read_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, name FROM users")
        rows = cursor.fetchall()
        data = [{"id": row[0], "name": row[1]} for row in rows]
    except Exception as e:
        data = {"error": str(e)}
    conn.close()
    return jsonify(data)

@app.route("/cpu_load", methods=["GET"])
def cpu_load():
    start_time = time.time()
    while time.time() - start_time < 180:
        _ = sum(i*i for i in range(10000))
    return jsonify({"status": "CPU load simulated for 3 minutes"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
