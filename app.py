from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('gqg2I/lG+uFd3oNe/TBt7xVDYx8Um3PJufHx1ctTrutLi0PHzIU7UYMQ/w9eR5ZEn7qB0nmN9xJd0EuH+4VMiTOg+x29yZzrfxwqnLFMGNLVr5mPeYjyNTYirsa4028P4DPwB6SJdqADcDfrNJTq6gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a6ff822dfad748a4f0e7582042a24634')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    message = TextSendMessage(text='Hello world')
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
