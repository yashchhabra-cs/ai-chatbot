from flask import Flask,request,jsonify,render_template 
import os
from dotenv import load_dotenv
import anthropic
app = Flask(__name__) 
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message=data['message']
    response= client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": user_message # this is the message from the user
            }
        ]
    )
    return jsonify({"response": response.content[0].text}) # this is the response from the claude model 
if __name__ == '__main__':
    app.run(debug=True)  # debug=True means that the server will automatically reload when the code is changed


