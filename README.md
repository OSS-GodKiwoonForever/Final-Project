# 미세먼지 봇 
> 지역명을 말하면 그 곳의 현재 미세먼지와 초미세먼지 수치를 알려주는 Line 채팅 봇
>>

>>

>>

>>

>>
>>
>>
>>
>>
>>
>>
>>
>>
>>
![](https://user-images.githubusercontent.com/38426656/49336668-4165bf00-f64a-11e8-84ea-960d4df8f8c5.PNG)

&nbsp;
## 미세먼지 봇 QR코드 
![](https://user-images.githubusercontent.com/38426656/49324322-92a08080-f56e-11e8-872d-3d7449800dcb.PNG)

## 기능
&nbsp;
 - 17개의 주요 도시명 입력시, 해당 도시의 미세먼지와 초미세먼지 수치를 알려줍니다.
 - '전체' 입력시, 모든 주요 도시에 대한 수치를 알려줍니다.
 - 매 시간 측정소에서 API로 정보를 받아 측정 시간을 알려줍니다.
 - 미세먼지 농도의 등급을 알려줍니다.
 - 미세먼지 등급에 따라 지역의 특색에 맞게 행동요령을 알려줍니다.

## 실행화면 

&nbsp;
- 친구 추가시

 ![](https://user-images.githubusercontent.com/38426656/49519136-a720a800-f8e3-11e8-9f8a-a44bbfba05da.PNG)

- 서울 입력

![](https://user-images.githubusercontent.com/38426656/49515749-252c8100-f8db-11e8-9eb1-53efb5c5ac45.PNG)

 - 전체 지역 입력
 
![](https://user-images.githubusercontent.com/38426656/49515735-1b0a8280-f8db-11e8-8aab-6e8aba83d3ea.PNG )

 - 잘못된 입력 
 
![](https://user-images.githubusercontent.com/38426656/49515799-48573080-f8db-11e8-8ae1-6327d0a7a127.PNG )

 ### 지방 지역 입력시, 사투리로 행동 요령을 알려줍니다
 

 - 경북 입력
 
![](https://user-images.githubusercontent.com/38426656/49515782-3f665f00-f8db-11e8-94bd-67d5b36e527b.PNG )

 - 전북 입력

![](https://user-images.githubusercontent.com/45088680/49534383-b6641d80-f904-11e8-87bb-47207953dc4b.PNG )

 - 제주 입력

![](https://user-images.githubusercontent.com/38426656/49515760-2f4e7f80-f8db-11e8-9f4e-85aabae9816a.PNG )

## 사용된 기술
&nbsp;
 - 개발언어는 py 사용
 - Python Line Bot SDK를 Heroku 프로그램에서 설정 
 - Line Console에서 Bot 채널 생성 
 - 지역 별 미세먼지와 초 미세먼지 Openaip 를 사용하기 위해, data.go.kr에 계정을      생성해서 API 접근키 이용

## 문제점 및 해결 과정
&nbsp;
- Line Developer 단계에서 봇 만들 때 Echo가 안될 경우, 설정에서 Channel Settings   -> Messaging settings -> Use webhooks 항목을 반드시 'Enabled'해야 합니다. 
- 작성한 코드는 event_reply_token은 1회용이라 사용시 expire되어 여러번 send_message를 실행할 수 없습니다 -> 유의하기
- 타인이 커밋한 소스코드 포크할 경우 덮어쓰고 실험해볼 때, 반드시 Chammel Access Token 이랑 Channel Secret Key를 본인의 Line Developer의 봇 넘버로 바꿔 올려 주어야 응답을 합니다. (변경하는 것을 깜빡할 시, 상대방 봇을 건드리게 되어 상대방도 난처해질 수 있음.) Github에 push하는 사람도 봇 넘버 키란은 비워둘 것을 권장
- 우리가 선택한 Openapi에서 처음엔 지역별 미세먼지만 출력하게 하였으나, 초미세먼지도 함수화하여 둘 다 받아오게끔 해결하였습니다.



## 데이터 출처
&nbsp;
- [Line bot](https://github.com/yaoandy107/line-bot-tutorial)
   : Line bot을 만드는 github 오픈 소스
- [한국환경공단](https://www.data.go.kr/dataset/15000581/openapi.do)
   : 미세먼지에 대한 API를 받아오는 곳




