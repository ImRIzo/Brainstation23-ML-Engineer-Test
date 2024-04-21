from flask import Flask, render_template, request
from chatbot import Medusa

app = Flask(__name__)

md = Medusa()

@app.route('/')
def index():    
    return render_template('./index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(md.enquiry(userText))

if __name__ == '__main__':
    app.run(debug=True)
