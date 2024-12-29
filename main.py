from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

server_data = {}

@app.route('/metrics', methods=['POST'])
def receive_metrics():
    data = request.json
    server_id = data.get("server_id")
    if server_id:
        server_data[server_id] = {
            "cpu": data.get("cpu"),
            "memory": data.get("memory"),
            "disk": data.get("disk"),
        }
        return jsonify({"message": "Metrics received!"}), 200
    return jsonify({"error": "Invalid data"}), 400

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("dashboard.html", servers=server_data)

@app.route('/')
def index():
    return redirect('/dashboard')

if __name__ == "__main__":
    app.run(debug=True)
