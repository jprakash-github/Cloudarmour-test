from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Testing Cloud Armour to protect python app."

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/client-ip")
def client_ip():
    return jsonify({
        "remote_addr": request.remote_addr,
        "x_forwarded_for": request.headers.get("X-Forwarded-For")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)