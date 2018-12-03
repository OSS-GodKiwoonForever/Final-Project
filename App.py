from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Toke
line_bot_api = LineBotApi('IJeXE4zAHUy3W5bCv/BUieiFnzkykNZUbpTTnDqYPNnfIyY3ay7u+ZcSYBpV3tez+Ta5cg3Gpp9Sa61oeTB0NIj2lA4g/pm0HBJ+8NyL3RuZ08WBLc4VYiXHEqnB6mmMtSN/NXLrZBfH3OPKqBzYSAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6bcf433f2727875ba56aeedbea0251c7')

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
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
