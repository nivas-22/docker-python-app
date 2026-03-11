from flask import Flask, jsonify
import platform
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Docker Python App 🚀",
        "python_version": platform.python_version(),
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/health")
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
