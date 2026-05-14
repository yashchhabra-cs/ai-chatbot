
from flask import Flask,request,jsonify,render_template 
import os
from dotenv import load_dotenv
import anthropic
app = Flask(__name__) # this is the entry point of the application  creation of app. 
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message=data['message']
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            system="You are a helpful assistant. Answer clearly and concisely. If you don't know something, say I don't know.",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return jsonify({"response": response.content[0].text})
    
    except Exception as e:
        return jsonify({"error": "Something went wrong. Please try again."}), 500
if __name__ == '__main__':
    app.run(debug=True)  # debug=True means that the server will automatically reload when the code is changed


