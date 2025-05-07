# web/app.py
from flask import Flask, request, jsonify, render_template
from agent.agent import agent_executor, get_logs

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        question = data.get("question", "").strip()
        if not question:
            return jsonify({"response": "Please provide a question."}), 400

        # Clear previous logs
        get_logs().clear()
        response = agent_executor.run(question)
        logs = get_logs()
        return jsonify({"response": response, "logs": logs})

    except Exception as e:
        # Catch any exception and return as JSON
        return jsonify({"response": f"Error: {str(e)}", "logs": get_logs()}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
