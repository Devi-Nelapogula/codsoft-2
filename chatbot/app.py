from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_message):

    message = user_message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"

    elif "how are you" in message:
        return "I am fine. Thank you for asking."

    elif "your name" in message:
        return "I am a Rule-Based Chatbot."

    elif "bye" in message:
        return "Goodbye! Have a great day."

    elif "help" in message:
        return "You can ask me about greetings, my name, or general questions."

    else:
        return "Sorry, I don't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():

    user_message = request.json["message"]

    response = chatbot_response(user_message)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)
