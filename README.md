# 라인에서 미세먼지 봇 만들기
##       by GodkiwoongForever

이 튜토리얼에서는 Python LINE Bot SDK를 사용하여 Heroku에서 간단한 컴백 로봇을 설정하는 방법을 보여줍니다.
<!--more-->
샘플 봇을 다른 언어로 설정하려면 아래의 LINE Bot SDK 저장소를 참조하십시오.
- [PHP](https://github.com/line/line-bot-sdk-php)
- [Go](https://github.com/line/line-bot-sdk-go)
- [Perl](https://github.com/line/line-bot-sdk-perl)
- [Ruby](https://github.com/line/line-bot-sdk-ruby)
- [Python](https://github.com/line/line-bot-sdk-python)
- [Node.js](https://github.com/line/line-bot-sdk-nodejs)

## 시작하기 전에

다음 사항을 확인하십시오.：

- 자신의 Line 계정 만들기
- [Heroku](https://www.heroku.com) 계정 (무료로 만들 수 있음)

## Heroku 프로젝트 만들기
1. Heroku에 로그인 한 후，
  [Heroku](https://dashboard.heroku.com/apps) 이 페이지에서 New -> Create New App
  ![](https://i.imgur.com/Y3njp7I.png)
2. 즐겨 사용하는 App name을 입력하고 Create app를 클릭.
  ![](https://i.imgur.com/WJ85jXR.png)

## Line Bot 채널 만들기
1. [Line Consol] 들어가기(https://developers.line.me/console/)
    ![](https://i.imgur.com/vseYQt1.png)
2. Provider 만들기.
    ![](https://i.imgur.com/0tnYFBd.png)
3. Provider 이름 입력.
    ![](https://i.imgur.com/2ne3H1F.png)
4. Create 클릭.
    ![](https://i.imgur.com/bdESW8G.png)
5. Create Channel 클릭.
    ![](https://i.imgur.com/F1nAWhK.png)
6. Bot 정보 채우기.
    ![](https://i.imgur.com/3wYFSvl.png)
7. Line 약관에 동의하고 Create 버튼 클릭.
    ![](https://i.imgur.com/WNzl4sL.png)
8. 금방 생성한 Bot 선택.
    ![](https://i.imgur.com/6ocsOBW.png)

## 샘플 봇 설정

다음 단계에 따라 리턴 로봇을 설정합니다。

1. 샘플 코드 다운로드(https://github.com/yaoandy107/line-bot-tutorial/archive/master.zip)
2. [Line Consol] 들어가기(https://developers.line.me/console/)，방금 생성 한 로봇을 선택.
    ![](https://i.imgur.com/6ocsOBW.png)
3.  webhook 열기
![](https://i.imgur.com/nxvFPB1.png)
![](https://i.imgur.com/PzEKzdq.png)
4. 미리 설정된 응답 메시지를 해제.
![](https://i.imgur.com/nXPRhT4.png)

5. **Channel access token** 생성
![](https://i.imgur.com/QyxnpZB.png)
![](https://i.imgur.com/quYbPx9.png)
6. **Channel access token**  확보
![](https://i.imgur.com/C7OTect.png)
7. **Channel secret** 확보
![](https://i.imgur.com/IwmvyzL.png)

6. 아톰과 같은 편집기를 사용하여 샘플 코드 폴더 열기 app.py，그냥 얻을 것이다 **channel secret** 와 **channel access token** 기입
  ![](https://i.imgur.com/Uz16joi.png)

## 프로그램을 Heroku 로 연결하기.

1. 다운로드 및 설치 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 방금 다운로드 한 샘플 코드 폴더를 열고 경로에 cmd를 입력하십시오.
3. 터미널이나 명령 줄 응용 프로그램을 사용하여 Heroku에 로그인하십시오.
    ```shell＝
    heroku login
    ```
4. git 초기화
    ``` shell=
    $ git config --global user.name "양세종"
    $ git config --global user.email Sejong@naver.com
    ```
   참고 : ** 귀하의 이름 ** 및 ** 귀하의 사서함 **은 해당 ** 이름 ** 및 ** 사서함 **으로 대체됩니다.

5.  git 초기화
    ```shell＝
    git init
    ```
   참고 : 처음 사용할 때만 입력하십시오.

6.git을 heroku에 연결
    ```shell＝
    heroku git:remote -a {HEROKU_APP_NAME}
    ```
    주의：{HEROKU_APP_NAME} Heroku 앱의 이름입니다.

7. 다음 명령을 입력하여 코드를 Heroku로 푸시하십시오，**반송 오류가 발생하면 재입력할 것.**
    ```shell
    git add .
    git commit -m "Add code"
    git push -f heroku master
    ```
    **Bot를 업데이트해야 할 때마다 위 지침을 다시 입력하십시오.**

##  Heroku 를 Line 에 연결하기
1. [Line Console]들어가기(https://developers.line.me/console/)，방금 생성 한 bot 선택
    ![](https://i.imgur.com/6ocsOBW.png)
2. Webhook URL에 Heroku URL을 입력하십시오.

    ```shell
    {HEROKU_APP_NAME}.herokuapp.com/callback
    ```
    ![](https://i.imgur.com/EkDhAgb.png)
   참고 : {HEROKU_APP_NAME}은 Heroku 앱의 이름입니다.


## 샘플 결과 테스트
1. [Line Console]들어가기](https://developers.line.me/console/)， 방금 생성 한 bot 선택
    ![](https://i.imgur.com/6ocsOBW.png)
2. Console을 통해 “Channel settings” 페이지에서  QR Code 스캔，LINE에 친구에게 Bot을 추가하십시오.
3. 온라인 봇 (Bot on Line)에 문자 메시지를 보내고 말하는 법을 배웁니다.

## 잘못된 검색

> 프로그램에서 문제가 발생하면 로그를보고 오류를 찾을 수 있습니다.

Heroku에서 Bot의 로그를 보려면 다음 단계를 따르십시오.

1. 먼저 Heroku CLI를 통해 로그인
    ```shell
    heroku login
    ```

2. app 로그 표시
    ```shell
    heroku logs --tail --app {HEROKU_APP_NAME}
    ```
   참고 : {HEROKU_APP_NAME}은 (는) 위의 2 단계에서 앱 이름입니다.
    ```shell
    --tail                     # 持續打印日誌
    --app {HEROKU_APP_NAME}    # 指定 App
    ```

## 프로그램 파일 설명

> 폴더에 두 개의 파일이있어 프로그램에서  heroku을 실행할 수 있습니다.

- Procfile : heroku는 web : {language} {file} 명령을 실행하고, 언어는 python이고 자동 실행되는 파일은 app.py이므로 ** web : python app.py **로 변경했습니다.
-Requirements.txt : 사용 된 모든 키트를 나열하면 heroku가이 파일을 기반으로 필요한 키트를 설치합니다.

### app.py (주요 프로그램)
프로그램에서 handle_message () 메소드의 코드를 수정하여 로봇의 메시지 응답을 제어 할 수 있습니다.

![](https://i.imgur.com/DNeNbpV.png)

새 예제 코드에 유의하십시오.
Git에 대해 더 알고 싶다면 Python3、[Flask kit](http://docs.jinkan.org/docs/flask/)、[Line bot sdk](https://github.com/line/line-bot-sdk-python)


## 고급 작동
[공식파일](https://github.com/line/line-bot-sdk-python#api)
### 답장 메시지
메시지가 도착하면 메시지에만 회신 할 수 있습니다.
```python
line_bot_api.reply_message(reply_token, 訊息物件)
```
### 능동적으로 메시지를 전송
Bot은 푸시 기능을 활성화해야합니다. 그렇지 않으면 프로그램에 오류가 발생합니다.
```python
line_bot_api.push_message(push_token, 訊息物件)
```

## 메시지 객체 분류

[공식 문서](https://developers.line.me/en/docs/messaging-api/message-types/)

샘플 코드 변경， handle_message() 메소드 내의 여러 함수를 구현.

### TextSendMessage （문자 메시지）
![](https://i.imgur.com/LieCFAb.png =250x)
```python
message = TextSendMessage(text='Hello, world')
line_bot_api.reply_message(event.reply_token, message)
```

### ImageSendMessage（그림 메시지）
![](https://i.imgur.com/RaH7gqo.png =250x)
```python
message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

### VideoSendMessage（비디오 메시지）
![](https://i.imgur.com/o6cvf3o.png =250x)
```python
message = VideoSendMessage(
    original_content_url='https://example.com/original.mp4',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

### AudioSendMessage（오디오 메시지）
![](https://i.imgur.com/w5szZag.png =250x)
```python
message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)
line_bot_api.reply_message(event.reply_token, message)
```

### LocationSendMessage（위치 메시지）
![](https://i.imgur.com/tXE7Aus.png =250x)
```python
message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
line_bot_api.reply_message(event.reply_token, message)
```

### StickerSendMessage（텍스처 메시지）
![](https://i.imgur.com/7x0mgK1.png =250x)
```python
message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
line_bot_api.reply_message(event.reply_token, message)
```

### ImagemapSendMessage （그룹 메시지）
![](https://i.imgur.com/MoSf2D6.png =250x)
```python
message = ImagemapSendMessage(
    base_url='https://example.com/base',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://example.com/',
            area=ImagemapArea(
                x=0, y=0, width=520, height=1040
            )
        ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=520, y=0, width=520, height=1040
            )
        )
    ]
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - ButtonsTemplate （버튼 인터페이스 메시지）
![](https://i.imgur.com/41lXWjP.png =250x)
```python
message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            ),
            URITemplateAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - ConfirmTemplate（인터페이스 메시지 확인）
![](https://i.imgur.com/U8NDhrt.png =250x)
```python
message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - CarouselTemplate
![](https://i.imgur.com/982Glgo.png =250x)
```python
message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://example.com/item1.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://example.com/item2.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - ImageCarouselTemplate
![](https://i.imgur.com/2ys1qqc.png =250x)
```python
message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
