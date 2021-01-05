from flask import Flask, request, abort, render_template, request, redirect, url_for, send_from_directory
import os
import json
import sys
import random
import tempfile

from tmpstate import *
from mapcolour import *
from Map import *
from Template import *
from DialogflowPro import *
from Mongo2 import *
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent, ImagemapSendMessage,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton, ImageSendMessage, BaseSize, MessageImagemapAction, ImagemapArea
)

from config import *

uid = ''
data = ''
Response = ''

app = Flask(__name__)
app.config["CLIENT_IMAGES"] = image_path

# line_bot_api = LineBotApi('vevuo42bYiqkQb9xTQffyixsTrfqUkLKFlJ8uAvcm8Ml8G0Xx4hnKP7R+TOHpvbjO0Wn2/OMgD0HgOaGaz2sI9mUqdHxJCPPi1H5TqUDsTbYmEi3QAjunvaGFd0XWxMvYgJwNI5sb2CLNNEArAP82AdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('073b76b9041fc0db8b536ac63c394123')

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)


def quickSend(text):
    Response = Send_Dialogflow("s$@ski216zcddwsrd", text, "th")
    txt = Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
    line_bot_api.reply_message(event.reply_token,  TextSendMessage(text=txt))



def deletesemi(text):
    c = 0
    txt = ''
    for i in text:
        if c == 1:
            txt += i
        if i == ':':
            c = 1
    return txt

@app.route("/", methods=['GET'])
def home():
    return "DelveiBot"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    print("callback")
    global Response
    try:
        signature = request.headers['X-Line-Signature']
        # get request body as text
        body = request.get_data(as_text=True)
        # if body.event
        Res = json.loads(body)
        global uid, data
        uid = Res['events'][0]['source']['userId']
        if Res['events'][0]['type'] == 'postback':
            # print(Res['events'][0]['postback']['data'])
            data = Res['events'][0]['postback']['data']
            if "info:" in data:
                txt = deletesemi(data)
                line_bot_api.reply_message(
                    Res['events'][0]['replyToken'],  TextSendMessage(text=disdata(txt)))

            if "tel:" in data:
                # print("tel:")
                txt = deletesemi(data)
                line_bot_api.reply_message(
                    Res['events'][0]['replyToken'],  TextSendMessage(text=distel(txt)))

    finally:
        print("yes")
    # if Res['events']
    # print(json.dumps(body, indent=4))
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK', 200


@app.route("/get-image/<image_name>", methods=['GET'])
def get_image(image_name):
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


def ChMeny(Response):
    x = 0
    for i in Response['queryResult']['fulfillmentMessages']:
        x += 1
    return x


# detect massage
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    global uid
    if text == "image":
        url = parturl+r"/get-image/colour.png"
        # url =parturl+r"/get-image/coin.jpg"
        app.logger.info("url=" + url)
        imagemap_message = getimagemapcolour()
#         image_message = ImageSendMessage(
#     original_content_url=url,
#     preview_image_url=url
# )
        # Mes = FlexSendMessage(alt_text="hello", contents=json.loads(bubble_string))
        line_bot_api.reply_message(event.reply_token, imagemap_message)
        # line_bot_api.reply_message(event.reply_token,image_message)
    else:
        global Response
        Response = Send_Dialogflow(uid, text, "th")
        # print("Respone : {}".format(Response))

        if type(Response) == list:
            if Response[0] == 'Report_Lost_money':
                template_message = Tmp_Confirm('แจ้งเลยใช่หรือไม่', [
                                               ['Yes', 'Lost_Money_Y', 'แจ้ง'], ['No', 'Lost_Money_N', 'ไม่แจ้ง']])
                txt = 'ตอนนี้ยังไม่มีใครมาแจ้งว่าเจอเงิน '+Response[1]+' บาทนะ'
                line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
                    text=Response[2]), TextSendMessage(text=txt), template_message])

            if Response[0] == 'Report_Found_money':

                template_message = Tmp_Confirm('แจ้งเลยใช่หรือไม่', [
                                               ['ใช่', 'Found_Money_Y', 'แจ้ง'], ['ไม่', 'Found_Money_N', 'ไม่แจ้ง']])
                txt = 'ตอนนี้ยังไม่มีใครมาแจ้งว่าเงินหายจำนวน ' + \
                    Response[1]+' บาทนะครับ'
                line_bot_api.reply_message(
                    event.reply_token,  [TextSendMessage(text=txt), template_message])

            # if Response[0] == "JerMoneyNP_f1" :
            #     line_bot_api.reply_message(event.reply_token,  TextSendMessage(text='ตอนนี้มีคนมาแจ้งเก็บเงินจำนวน'+Response[1]+'บาทได้นะ แต่ไม่รู้สถานที่ ลองติดต่อที่ <สำนักงาน> ดูนะ'))
            #     reset_context(uid)
            if Response[0] == 'Map':
                imagemap_message = getimagemap()
                OP = Response[1]
                if type(OP) == str:
                    line_bot_api.reply_message(
                        event.reply_token,  [TextSendMessage(text=OP), imagemap_message])
                if type(OP) == list:
                    OP.append("กรุณาติ๊กที่ตัวเลขบนภาพในตำแหน่งที่จะแจ้งครับ")
                    if len(OP) == 1:
                        line_bot_api.reply_message(
                            event.reply_token, [TextSendMessage(text=OP[0]), imagemap_message])
                    if len(OP) == 2:
                        line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                            text=OP[0]), TextSendMessage(text=OP[1]), imagemap_message])
                    if len(OP) == 3:
                        line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                            text=OP[0]), TextSendMessage(text=OP[1]), TextSendMessage(text=OP[2]), imagemap_message])
                    if len(OP) == 4:
                        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=OP[0]), TextSendMessage(
                            text=OP[1]), TextSendMessage(text=OP[2]), TextSendMessage(text=OP[3]), imagemap_message])

            if Response[0] == 'Mapcolour':
                imagemap_message = getimagemapcolour()
                OP = Response[1]
                OP.append("คลิ๊กสีที่ใกล้เคียงได้เลยครับ")
                if type(OP) == str:
                    line_bot_api.reply_message(
                        event.reply_token,  [TextSendMessage(text=OP), imagemap_message])
                if type(OP) == list:
                    if len(OP) == 1:
                        line_bot_api.reply_message(
                            event.reply_token, [TextSendMessage(text=OP[0]), imagemap_message])
                    if len(OP) == 2:
                        line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                            text=OP[0]), TextSendMessage(text=OP[1]), imagemap_message])
                    if len(OP) == 3:
                        line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                            text=OP[0]), TextSendMessage(text=OP[1]), TextSendMessage(text=OP[2]), imagemap_message])
                    if len(OP) == 4:
                        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=OP[0]), TextSendMessage(
                            text=OP[1]), TextSendMessage(text=OP[2]), TextSendMessage(text=OP[3]), imagemap_message])

            if Response[0] == 'Finish':
                print("in22555")
                if Response[1] == 1:
                    tex = ['แจ้งไว้เรียบร้อยแล้วนะครับ',
                           'เดลวีทำรายการให้เรียบร้อยแล้วครับ', 'เสร็จแล้วครับ']
                    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
                        text=random.choice(tex)), StickerSendMessage(package_id='1', sticker_id='407')])
                    reset_context(uid)
                if Response[1] == 2:
                    tex = ['การแจ้งยกเลิก',
                           'ยกเลิกการแจ้งเรียบร้อย', 'เสร็จแล้วครับ']
                    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
                        text=random.choice(tex)), StickerSendMessage(package_id='1', sticker_id='407')])
                    reset_context(uid)
            if Response[0] == 'Cancel':
                txt = Response[1]['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
                line_bot_api.reply_message(
                    event.reply_token,  TextSendMessage(text=txt))
                reset_context(uid)
            if Response[0] == -1:
                OP = Response[1]
                if type(OP) == str:
                    line_bot_api.reply_message(
                        event.reply_token,  TextSendMessage(text=OP))
                if type(OP) == list:
                    if len(OP) == 1:
                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(text=OP[0]))
                    if len(OP) == 2:
                        line_bot_api.reply_message(
                            event.reply_token, [TextSendMessage(text=OP[0]), TextSendMessage(text=OP[1])])
                    if len(OP) == 3:
                        line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                            text=OP[0]), TextSendMessage(text=OP[1]), TextSendMessage(text=OP[2])])
            if Response[0] == -2:
                OP = Response[2]
                # print("len(OP ={}".format(len(OP)))
                if len(OP) == 1:
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text=OP[0]))
                if len(OP) == 2:
                    line_bot_api.reply_message(
                        event.reply_token, [TextSendMessage(text=OP[0]), TextSendMessage(text=OP[1])])
                if len(OP) == 3:
                    line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                        text=OP[0]), TextSendMessage(text=OP[1]), TextSendMessage(text=OP[2])])

                Send_Dialogflow(uid, Response[1], "th")
                if Response[1] == "jpg : <jpg-nophotoo.jpg>":
                    tex = ['ไม่ทราบว่าสะดวกให้คืนที่<สำนักงาน>หรือที่ตัวเองครับ']
                    Text1 = 'ให้ติดต่อคืนได้ที่' + \
                        line_bot_api.get_profile(
                            uid).display_name+'\nหรือติดต่อคืนได้ที่สำนักงาน'
                    template_message = tmp_Button('เลือกการทำงาน', Text1, [['ให้การติดต่อ', 'ที่ตัวเอง_F1', 'ให้การติดต่อ'], [
                                                  'ติดต่อคืนได้ที่ <สำนักงาน>', 'ติดต่อคืนได้ที่สำนักงาน', 'ติดต่อคืนได้ที่<สำนักงาน>']])
                    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
                        text='ไม่เป็นไรครับ'), TextSendMessage(text=random.choice(tex)), template_message])

            if Response[0] == 'show':
                temp = show_data(Response[1])
                # print("in show")
                #print(Response)
                OP = Response[2]
                template_message = Tmp_Confirm('แจ้งเลยใช่หรือไม่', [
                                               ['Yes', 'Lost_Money_Y', 'แจ้ง'], ['No', 'Lost_Money_N', 'ไม่แจ้ง']])
                line_bot_api.reply_message(
                    event.reply_token, [TextSendMessage(text=OP), template_message, temp])
                # reset_context()

            if Response[0] == 'donthave':
                tex = Response[1]
                template_message = Tmp_Confirm('แจ้งเลยใช่หรือไม่', [
                                               ['Yes', 'Lost_Money_Y', 'แจ้ง'], ['No', 'Lost_Money_N', 'ไม่แจ้ง']])
                line_bot_api.reply_message(
                    event.reply_token, [TextSendMessage(text=tex), template_message])
                # reset_context(uid)
            if Response[0] == "instructive-state8":
                tex = ['งั้นไม่เป็นไรนะครับ เดี๋ยวแจ้งผมไว้ก็ได้ครับ',
                       'งั้นเดี๋ยวแจ้งผมไว้ก็ได้ครับ']
                template_message = Tmp_Confirm('แจ้งเลยใช่หรือไม่', [
                                               ['Yes', 'Lost_Money_Y', 'แจ้ง'], ['No', 'Lost_Money_N', 'ไม่แจ้ง']])
                line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                    text=random.choice(tex)), template_message])
            if Response[0] == 'get-image':
                tex = Response[1]
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=tex, quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=CameraAction(
                                label="photo")
                        ),
                        QuickReplyButton(
                            action=CameraRollAction(
                                label="Gallary")
                        ),
                    ])))

        elif type(Response) == str:
            if Response == 'Want_More_infomation?':
                template_message = Tmp_Confirm(
                    'แจ้งเพิ่มเติม', [['ใช่', 'W_m_Y', 'ใช่'], ['ไม่', 'W_m_Y', 'ไม่']])
                line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
                    text='คุณเคยแจ้งข้อมูลมาแล้ว ต้องการแจ้งเพิ่มเติมหรือไม่?'), template_message])

            if Response == 'ReportYN_yes':
                tex = 'ไม่ทราบว่าสะดวกให้คืนที่<สำนักงาน>หรือที่คุณ' + \
                    line_bot_api.get_profile(uid).display_name+'ครับ'
                Text1 = 'ให้ติดต่อคืนได้ที่' + \
                    line_bot_api.get_profile(
                        uid).display_name+'\nหรือติดต่อคืนได้ที่สำนักงาน'
                template_message = tmp_Button('เลือกการทำงาน', Text1, [['ให้การติดต่อ', 'ที่ตัวเอง_F1', 'ให้การติดต่อ'], [
                                              'ติดต่อคืนได้ที่ <สำนักงาน>', 'ติดต่อคืนได้ที่สำนักงาน', 'ติดต่อคืนได้ที่<สำนักงาน>']])
                line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
                    text='ผมขอข้อมูลเพิ่มเติมนะ'), TextSendMessage(text=tex), template_message])
            if Response == 'ReportYN_yes_Found':
                tex = 'ไม่ทราบว่าสะดวกให้เจ้าตัวรับคืนได้ที่<สำนักงาน>หรือที่คุณ ' + \
                    line_bot_api.get_profile(uid).display_name+' ครับ'
                Text1 = 'ให้ติดต่อรับคืนได้ที่' + \
                    line_bot_api.get_profile(
                        uid).display_name+'\nหรือติดต่อรับคืนได้ที่สำนักงาน'
                template_message = tmp_Button('เลือกการทำงาน', Text1, [['ให้การติดต่อ', 'ที่ตัวเอง_F1', 'ให้การติดต่อ'], [
                                              'รับคืนได้ที่ <สำนักงาน>', 'ติดต่อคืนได้ที่สำนักงาน', 'รับคืนได้ที่<สำนักงาน>']])
                line_bot_api.reply_message(event.reply_token, [TextSendMessage(
                    text='ผมขอข้อมูลเพิ่มเติมนะ'), TextSendMessage(text=tex), template_message])
                # line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='ผมขอข้อมูลเพิ่มเติมนะ')])
            if Response == 'ReportYN_no':
                tex = ['การแจ้งยกเลิก', 'ยกเลิกการแจ้งเรียบร้อย', 'เสร็จแล้วครับ']
                line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
                    text=random.choice(tex)), StickerSendMessage(package_id='1', sticker_id='125')])
                reset_context(uid)

        elif type(Response) == dict:
            txt = Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
            if Response['queryResult']['intent']['displayName'] == 'report':
                template_message = tmp_Button('เลือกการทำงาน', 'อยากให้เดลวีช่วยไร?', [
                                              ['แจ้งของหาย', 'Flow1', "แจ้งของหาย"], ['เก็บได้ฝากแจ้ง', 'Flow2', 'เก็บได้ฝากแจ้ง']])
                if ChMeny(Response) == 1:
                    txt = Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
                    line_bot_api.reply_message(
                        event.reply_token,  [TextSendMessage(text=txt), template_message])
                elif ChMeny(Response) == 2:
                    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(text=Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]),
                                                                    TextSendMessage(
                                                                        text=Response['queryResult']['fulfillmentMessages'][1]['text']['text'][0]),
                                                                    template_message])

            if Response['queryResult']['intent']['displayName'] == 'Foundแล้ว':
                line_bot_api.reply_message(event.reply_token,  [TextSendMessage(text=Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]),
                                                                StickerSendMessage(package_id='11538', sticker_id='51626520')])

            if Response['queryResult']['intent']['displayName'] == 'check-state':
                data = load_data(uid)
                print("data {}".format(data))
                if data.count == 0:
                    line_bot_api.reply_message(event.reply_token,  TextSendMessage(
                        text='คุณยังไม่เคยแจ้งรายการไว้นะครับ'))
                else:
                    tmp = show_state(data)
                    line_bot_api.reply_message(event.reply_token,  tmp)

            if Response['queryResult']['intent']['displayName'] == 'what can you do':
                lis = [['แจ้งของหาย', 'Flow1', "แจ้งของหาย"], ['เก็บได้ฝากแจ้ง', 'Flow2', 'เก็บได้ฝากแจ้ง'], [
                    'เช็คสถานะ', 'เช็คสถานะ', 'เช็คสถานะ'], ['ปรึกษาของหาย', 'ปรึกษาของหาย', 'ปรึกษาของหาย']]
                template_message = tmp_Button(
                    'เลือกการทำงาน', 'อยากให้เดลวีช่วยไร?', lis)
                if ChMeny(Response) == 1:
                    txt = Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
                    line_bot_api.reply_message(
                        event.reply_token,  [TextSendMessage(text=txt), template_message])
                elif ChMeny(Response) == 2:
                    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(text=Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]),
                                                                    TextSendMessage(
                                                                        text=Response['queryResult']['fulfillmentMessages'][1]['text']['text'][0]),
                                                                    template_message])
            else:
                if ChMeny(Response) == 1:
                    txt = Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
                    line_bot_api.reply_message(
                        event.reply_token,  TextSendMessage(text=txt))
                elif ChMeny(Response) == 2:
                    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(text=Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]),
                                                                    TextSendMessage(
                                                                        text=Response['queryResult']['fulfillmentMessages'][1]['text']['text'][0])
                                                                    ])
                elif ChMeny(Response) == 3:
                    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(text=Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]),
                                                                    TextSendMessage(
                                                                        text=Response['queryResult']['fulfillmentMessages'][1]['text']['text'][0]),
                                                                    TextSendMessage(
                                                                        text=Response['queryResult']['fulfillmentMessages'][2]['text']['text'][0])
                                                                    ])
        else:
            if ChMeny(Response) == 1:
                txt = Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
                line_bot_api.reply_message(
                    event.reply_token,  TextSendMessage(text=txt))
            elif ChMeny(Response) == 2:
                line_bot_api.reply_message(event.reply_token,  [TextSendMessage(text=Response['queryResult']['fulfillmentMessages'][0]['text']['text'][0]),
                                                                TextSendMessage(
                                                                    text=Response['queryResult']['fulfillmentMessages'][1]['text']['text'][0])
                                                                ])


# detect image
@handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def IMAGE(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    elif isinstance(event.message, VideoMessage):
        ext = 'mp4'
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
    else:
        return

    static_tmp_path = image_path
    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)
    global uid
    tex = 'jpg : <'+dist_name+">"
    Response = Send_Dialogflow(uid, tex, "th")
    tex = ['ไม่ทราบว่าสะดวกให้คืนที่<สำนักงาน>หรือที่ตัวเองครับ']
    Text1 = 'ให้ติดต่อคืนได้ที่' + \
        line_bot_api.get_profile(uid).display_name + \
        '\nหรือติดต่อคืนได้ที่สำนักงาน'
    template_message = tmp_Button('เลือกการทำงาน', Text1, [['ให้การติดต่อ', 'ที่ตัวเอง_F1', 'ให้การติดต่อ'], [
                                  'ติดต่อคืนได้ที่ <สำนักงาน>', 'ติดต่อคืนได้ที่สำนักงาน', 'ติดต่อคืนได้ที่<สำนักงาน>']])
    line_bot_api.reply_message(event.reply_token,  [TextSendMessage(
        text='งั้นผมขอข้อมูลเพิ่มเติมนะ'), TextSendMessage(text=random.choice(tex)), template_message])
    # line_bot_api.reply_message(
    #     event.reply_token, [
    #         TextSendMessage(text='Save content.'),
    #         TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name)),
    #         TextSendMessage(text="เยี่ยม")
    #     ])


if __name__ == "__main__":
    app.run(port=3000)
