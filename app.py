from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus,unquote
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Channel Access Token')
# Channel Secret
handler = WebhookHandler('Channel Secret')

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

    API_key = unquote('API_key')
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('itemCode') : 'PM10', quote_plus('dataGubun') : 'HOUR', quote_plus('searchCondition') : 'MONTH' })

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    root = ET.fromstring(response_body)

    seoul = root.find('body').find('items').find('item').find('seoul')
    gyeonggi = root.find('body').find('items').find('item').find('gyeonggi')
    busan = root.find('body').find('items').find('item').find('busan')
    daegu = root.find('body').find('items').find('item').find('daegu')
    incheon = root.find('body').find('items').find('item').find('incheon')
    gwangju = root.find('body').find('items').find('item').find('gwangju')
    daejeon = root.find('body').find('items').find('item').find('daejeon')
    ulsan = root.find('body').find('items').find('item').find('ulsan')
    gangwon = root.find('body').find('items').find('item').find('gangwon')
    chungbuk = root.find('body').find('items').find('item').find('chungbuk')
    chungnam = root.find('body').find('items').find('item').find('chungnam')
    jeonbuk = root.find('body').find('items').find('item').find('jeonbuk')
    jeonnam = root.find('body').find('items').find('item').find('jeonnam')
    gyeongbuk = root.find('body').find('items').find('item').find('gyeongbuk')
    gyeongnam = root.find('body').find('items').find('item').find('gyeongnam')
    jeju = root.find('body').find('items').find('item').find('jeju')
    sejong = root.find('body').find('items').find('item').find('sejong')
    dicts = {"서울":seoul,"경기":gyeonggi,"부산":busan,"대구":daegu,"인천":incheon,"광주":gwangju,"대전":daejeon,"울산":ulsan,"강원":gangwon,
    "충북":chungbuk,"충남":chungnam,"전북":jeonbuk,"전남":jeonnam,"경북":gyeongbuk,"경남":gyeongnam,"제주":jeju,"세종":sejong}
    # message = TextSendMessage(text=event.message.text)
    userinput = event.message.text.lower()
    textmsg = userinput.capitalize()+"의 PM10 수치:"+dicts[userinput].text
    message = TextSendMessage(text=textmsg)
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
