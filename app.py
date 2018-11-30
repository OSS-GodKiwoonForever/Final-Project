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
def air_status(data):
    status = ""
    if(0<int(data)<=30):
        status = "좋음"
    elif(30<int(data)<80):
        status = "보통"
    elif(80<int(data)<=150):
        status = "나쁨"
    elif(150<int(data)):
        status = "매우나쁨"
    return status
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    API_key = unquote('R1V4MPrTQswXXkm8ChQgr%2BGl%2F%2F1SaMuMBpFpDZpflAftaVSnjVK%2F8ye6OZtNsdsyFbvfEsWfPdJAWX2soyzLeg%3D%3D')
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('numOfRows') : '18', quote_plus('pageNo') : '1', quote_plus('itemCode') : 'PM10', quote_plus('dataGubun') : 'HOUR', quote_plus('searchCondition') : 'MONTH' })

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    root = ET.fromstring(response_body)

    date = root.find('body').find('items').find('item').find('dataTime')
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

    textmsg = ""
    result = ""
    #textmsg 변수 생성
    help_msg ="""입력이 잘못되었습니다.
현재 입력 : {}
세종대학교 "갓기웅포레버" 미세먼지 봇 입니다.
지역 이름 혹은 "전체"를 입력하시면 미세먼지 수치를 말해줍니다.
ex) "울산" , reply "울산의 미세먼지 수치: 94"
ex) "전체" , reply "서울의 미세먼지 수치: 94 울산의 미세먼지 수치: 33 ..."
현재 조회할 수 있는 지역은
다음과 같습니다.

서울, 경기, 부산, 대구, 인천
광주, 대전, 울산, 강원, 충북
충남, 전북, 전남, 경북, 경남
제주, 세종
"""
    userinput = event.message.text
    textmsg = "측정 시간 : " + date.text + "\n"
    if (userinput == "전체"):
        for i in dicts.keys():
            textmsg += i+"의 PM10 수치:"+dicts[i].text+"\n" #for문을 돌면서 textmsg에 시도별 정보를 추가해줌
            #이렇게 하는 이유는 line_sdk에서 event.reply_token은 일회성이라 재사용이 불가능해서임.
    elif(userinput not in dicts.keys()):
        textmsg = help_msg.format(userinput)
    else:
        textmsg += userinput.capitalize()+"의 PM10 수치:"+dicts[userinput].text + "\n"
        result = air_status(dicts[userinput].text)
        textmsg += "현재 미세먼지 농도 등급은 " + result + "입니다."

    message = TextSendMessage(text=textmsg)
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
