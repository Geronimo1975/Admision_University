from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
