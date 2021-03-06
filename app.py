# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/zSz984R86HtvBOngs4TrL1ERBmox2AJWtNwDfNinNZY7oyT2FimEL2UMLs+4duI1FkmAkdrouCQQ9F1tlZCrricIPuU2197ERzwp3Xq4FtlME0evu7s63WIQlCc0A7zVPp/FWspxAqcCyXfcSl6XwdB04t89/1O/w1cDnyilFU=') 
handler = WebhookHandler('232b3d5feec793db430a04ebc37aa12f') 

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])