import json 

from flask import Flask,request

import chatGpt

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():  # put application's code here

    print("url：{}".format(request.values))
    print("请求包json：{}".format(request.json))
    print("请求包：{}".format(request.data))
    print(json.loads(request.data))
    msg = request.json.get("content")
    if msg is None or "" == msg:
        return "msg not exits"
    content = chatGpt.get_message(msg)
    return content


if __name__ == '__main__':
    app.run()