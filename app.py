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
line_bot_api = LineBotApi('lea6HxWjzQpT5OQgbMpKYTAff2l8/T3/O0jFblDIJbENWlAxwlFBlFRTkspHYRqN9f4Ubk5uwwvjIzcN/v3Xy2AgWYptDFjP4hTdE2fLicIv6mB6uAFliBAtnxXDPh3Gnve/kW+qBJSMLXk32mHVvgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b7e5280d7ef356f880b392ed308eae7e')

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

def get_air_quality(pm):
    API_key = unquote('R1V4MPrTQswXXkm8ChQgr%2BGl%2F%2F1SaMuMBpFpDZpflAftaVSnjVK%2F8ye6OZtNsdsyFbvfEsWfPdJAWX2soyzLeg%3D%3D')
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('numOfRows') : '18', quote_plus('pageNo') : '1', quote_plus('itemCode') : pm, quote_plus('dataGubun') : 'HOUR', quote_plus('searchCondition') : 'MONTH' })

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

    return {"서울":seoul,"경기":gyeonggi,"부산":busan,"대구":daegu,"인천":incheon,"광주":gwangju,"대전":daejeon,"울산":ulsan,"강원":gangwon,
    "충북":chungbuk,"충남":chungnam,"전북":jeonbuk,"전남":jeonnam,"경북":gyeongbuk,"경남":gyeongnam,"제주":jeju,"세종":sejong}, date

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    PM10,date1 = get_air_quality("PM10")
    PM25,date2 = get_air_quality("PM25")
    dicts = [PM10,PM25]
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
    textmsg = "전국 미세먼지 측정 현황\n측정 시간 : " + date1.text + "\n"
    if (userinput == "전체"):
        for i in dicts[0].keys():
            textmsg += i+": 미세먼지 {:>3}".format(dicts[0][i].text)+", 초미세먼지 {:>3}".format(dicts[1][i].text)+"\n" #for문을 돌면서 textmsg에 시도별 정보를 추가해줌
            #이렇게 하는 이유는 line_sdk에서 event.reply_token은 일회성이라 재사용이 불가능해서임.
    elif(userinput not in dicts[0].keys()):
        textmsg = help_msg.format(userinput)
    else:
        textmsg = ""
        textmsg += userinput+ "의 미세먼지 현황\n측정 시간 : " + date1.text + "\n"
        textmsg += "미세먼지:{:>3}".format(dicts[0][userinput].text) +", 초미세먼지:{:>3}".format(dicts[1][userinput].text)+ "\n"
        result = air_status(dicts[0][userinput].text)
        textmsg += "현재 미세먼지 농도 등급은 " + result + "입니다."
		if(result == "보통" or result == "좋음"):
    		if(userinput=="전남" or userinput=="전북"or userinput=="광주"): #전라도 방언 조건문
    			textmsg += "\n" + "오늘은 아따 거시기 하기에 양호하다잉."
    			elif(userinput=="부산" or userinput=="대구"or userinput=="울산"or userinput=="경북"or userinput=="경남"): #경상도 방언 조건문
    				textmsg += "\n" + "오늘은~ 외출하기에 양호하데이~."
    			elif(userinput=="충북" or userinput=="충남"or userinput=="대전"or userinput=="세종"): #충청도 방언 조건문
    				textmsg += "\n" + "오늘은 뭐유 외출하기에 양호하데유~."
    			elif(userinput=="강원"): #강원도 방언 조건문
    				textmsg += "\n" + "오늘은 외출하기에 양호이래요."
    			elif(userinput=="제주"): #제주 방언 조건문
    				textmsg += "\n" + "오늘은 외출하기에 양호하우다."
    			else:
    				textmsg += "\n" + "오늘은 외출하기에 양호합니다."
		else:
			if(userinput=="전남" or userinput=="전북"or userinput=="광주"): #전라도 방언 조건문
				textmsg += "\n" + "아따 거시기할때 미세먼지 전용 마스크랑 야외활동 자제 하쇼잉"
			elif(userinput=="부산" or userinput=="대구"or userinput=="울산"or userinput=="경북"or userinput=="경남"): #경상도 방언 조건문
				textmsg += "\n" + "나갈때 미세먼지 전용 마스크 챙깄나? 그리고 왠만하믄 야외활동 자주 하그래이"
			elif(userinput=="충북" or userinput=="충남"or userinput=="대전"or userinput=="세종"): #충청도 방언 조건문
				textmsg += "\n" + "나갈때 미세먼지 전용 마스크햐~ 글고 왠만하면 나가는거 자제 해유"
			elif(userinput=="강원"): #강원도 방언 조건문
				textmsg += "\n" + "미세먼지 많드래요~ 전용 마스크꼭꼭 챙기시래요 나가는것도 자제 하는게 좋드래요"
			elif(userinput=="제주"): #제주 방언 조건문
				textmsg += "\n" + "어드레 감수과? 이래 옵서 전용 마스크 마씀 야외활동 자제하는게 좋수다"
			else:
				textmsg += "\n" + "외출시 미세먼지 전용 마스크를 쓰거나 야외활동을 자제하는게 바람직합니다."
    message = TextSendMessage(text=textmsg)
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
