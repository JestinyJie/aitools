import time

import gevent.monkey
gevent.monkey.patch_all()

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__, template_folder='pages')
CORS(app)

openai.api_key = 'your api key'

# 前端页面
@app.route("/ping")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/chat")
def chat_page():
    return render_template("chat.html")

# 后端api
@app.route("/api/chat", methods=['POST'])
def chat():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=data['msg']
    )
    text = response.choices[0].message.content.strip()
    return jsonify({"result": text})

