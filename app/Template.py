
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,ImageSendMessage
)
from config import *
domainname=parturl
linkurl=domainname+r'/get-image/'
def Tmp_Confirm(title,List_Op) :
    if len(List_Op) == 1 :
        buttons_template = ConfirmTemplate(
                        text=title, actions=[
                            PostbackAction(label=List_Op[0][0], data=List_Op[0][1], text=List_Op[0][2]),
                        ])
    if len(List_Op) == 2 :
        buttons_template = ConfirmTemplate(
                        text=title, actions=[
                            PostbackAction(label=List_Op[0][0], data=List_Op[0][1], text=List_Op[0][2]),
                            PostbackAction(label=List_Op[1][0], data=List_Op[1][1], text=List_Op[1][2])
                        ])
    return TemplateSendMessage(alt_text='Confirm template', template=buttons_template)



def tmp_Button(title , tex, List_Op) :
    if len(List_Op) == 2:
        buttons_template = ButtonsTemplate(
                        title=title, text=tex, actions=[
                            PostbackAction(label=List_Op[0][0], data=List_Op[0][1], text=List_Op[0][2]),
                            PostbackAction(label=List_Op[1][0], data=List_Op[1][1], text=List_Op[1][2]),
                        ])
    if len(List_Op) == 3:
        buttons_template = ButtonsTemplate(
                        title=title, text=tex, actions=[
                            PostbackAction(label=List_Op[0][0], data=List_Op[0][1], text=List_Op[0][2]),
                            PostbackAction(label=List_Op[1][0], data=List_Op[1][1], text=List_Op[1][2]),
                            PostbackAction(label=List_Op[2][0], data=List_Op[2][1], text=List_Op[2][2]),
                        ])
    if len(List_Op) == 4  :
        buttons_template = ButtonsTemplate(
                        title=title, text=tex, actions=[
                            PostbackAction(label=List_Op[0][0], data=List_Op[0][1], text=List_Op[0][2]),
                            PostbackAction(label=List_Op[1][0], data=List_Op[1][1], text=List_Op[1][2]),
                            PostbackAction(label=List_Op[2][0], data=List_Op[2][1], text=List_Op[2][2]),
                            PostbackAction(label=List_Op[3][0], data=List_Op[3][1], text=List_Op[3][2]),
                        ])
    if len(List_Op) == 5  :
        buttons_template = ButtonsTemplate(
                        title=title, text=tex, actions=[
                            PostbackAction(label=List_Op[0][0], data=List_Op[0][1], text=List_Op[0][2]),
                            PostbackAction(label=List_Op[1][0], data=List_Op[1][1], text=List_Op[1][2]),
                            PostbackAction(label=List_Op[2][0], data=List_Op[2][1], text=List_Op[2][2]),
                            PostbackAction(label=List_Op[3][0], data=List_Op[3][1], text=List_Op[3][2]),
                            PostbackAction(label=List_Op[4][0], data=List_Op[4][1], text=List_Op[4][2]),
                        ])
    return TemplateSendMessage(alt_text='Buttons alt text', template=buttons_template)
def quick_SendMessage(OP) :
    if type(OP) == str :
        return TextSendMessage(text=OP)
    if type(OP) == list :
        if len(OP)==2 :
            return [TextSendMessage(text=OP[0]),TextSendMessage(text=OP[1])]
        if len(OP)==3 :
            return [TextSendMessage(text=OP[0]),TextSendMessage(text=OP[1]),TextSendMessage(text=OP[2])]

def get_param(iput,da,str):
    return iput['queryResult']['outputContexts'][da[0]]['parameters'][str]


def show_data(Listdata) :
    # print(Listdata)
    size=len(Listdata[0]['_id'])-1
    flow=Listdata[0]['_id'][size]
    if Listdata.count() == 1 :
        return TemplateSendMessage(alt_text='Carousel template',template=CarouselTemplate(columns=[
                            CarouselColumn(
                                thumbnail_image_url=linkurl+Listdata[0]['url']+r'.jpg',
                                title=Listdata[0]['item'],
                                text=Listdata[0]['text'],
                                actions=[
                                    PostbackAction(
                                        label='รายละเอียด',
                                        # display_text='postback text1',
                                        data=r'info:'+Listdata[0]['_id']
                                    ),
                                    PostbackAction(
                                        label='ขอการติดต่อ',
                                        # display_text='postback text1',
                                        data=r'tel:'+Listdata[0]['_id']
                                    ),
                                ]
                            )
                        ]
                    )
                )
    if Listdata.count() == 2 :
        return TemplateSendMessage(alt_text='Carousel template',template=CarouselTemplate(columns=[
                            CarouselColumn(
                                thumbnail_image_url=linkurl+Listdata[0]['url']+r'.jpg',
                                title=Listdata[0]['item'],
                                text=Listdata[0]['text'],
                                actions=[
                                    PostbackAction(
                                        label='รายละเอียด',
                                        # display_text='postback text1',
                                        data=r'info:'+Listdata[0]['_id']
                                    ),
                                    PostbackAction(
                                        label='ขอการติดต่อ',
                                        # display_text='postback text1',
                                        data=r'tel:'+Listdata[0]['_id']
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                thumbnail_image_url=linkurl+Listdata[1]['url']+r'.jpg',
                                title=Listdata[1]['item'],
                                text=Listdata[1]['text'],
                                actions=[
                                    PostbackAction(
                                        label='รายละเอียด',
                                        # display_text='postback text1',
                                        data=r'info:'+Listdata[1]['_id']
                                    ),
                                    PostbackAction(
                                        label='ขอการติดต่อ',
                                        # display_text='postback text1',
                                        data=r'tel:'+Listdata[1]['_id']
                                    ),
                                ]
                            )
                        ]
                    )
                )
    if Listdata.count() == 3 :
        return TemplateSendMessage(alt_text='Carousel template',template=CarouselTemplate(columns=[
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[0]['url']+r'.jpg',
                            title=Listdata[0]['item'],
                            text=Listdata[0]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[0]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[0]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[1]['url']+r'.jpg',
                            title=Listdata[1]['item'],
                            text=Listdata[1]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[1]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[1]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[2]['url']+r'.jpg',
                            title=Listdata[2]['item'],
                            text=Listdata[2]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[2]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[2]['_id']
                                ),
                            ]
                        )
                    ]
                )
            )
    if Listdata.count() == 4 :
        return TemplateSendMessage(alt_text='Carousel template',template=CarouselTemplate(columns=[
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[0]['url']+r'.jpg',
                            title=Listdata[0]['item'],
                            text=Listdata[0]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[0]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[0]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[1]['url']+r'.jpg',
                            title=Listdata[1]['item'],
                            text=Listdata[1]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[1]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[1]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[2]['url']+r'.jpg',
                            title=Listdata[2]['item'],
                            text=Listdata[2]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[2]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[2]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[3]['url']+r'.jpg',
                            title=Listdata[3]['item'],
                            text=Listdata[3]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[3]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[3]['_id']
                                ),
                            ]
                        )
                    ]
                )
            )
    if  Listdata.count() == 5 :
        return TemplateSendMessage(alt_text='Carousel template',template=CarouselTemplate(columns=[
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[0]['url']+r'.jpg',
                            title=Listdata[0]['item'],
                            text=Listdata[0]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[0]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[0]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[1]['url']+r'.jpg',
                            title=Listdata[1]['item'],
                            text=Listdata[1]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[1]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[1]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[2]['url']+r'.jpg',
                            title=Listdata[2]['item'],
                            text=Listdata[2]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[2]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[2]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[3]['url']+r'.jpg',
                            title=Listdata[3]['item'],
                            text=Listdata[3]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[3]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[3]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[4]['url']+r'.jpg',
                            title=Listdata[4]['item'],
                            text=Listdata[4]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[4]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[4]['_id']
                                ),
                            ]
                        )
                    ]
                )
            )
    if  Listdata.count() == 6 :
        return TemplateSendMessage(alt_text='Carousel template',template=CarouselTemplate(columns=[
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[0]['url']+r'.jpg',
                            title=Listdata[0]['item'],
                            text=Listdata[0]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[0]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[0]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[1]['url']+r'.jpg',
                            title=Listdata[1]['item'],
                            text=Listdata[1]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[1]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[1]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[2]['url']+r'.jpg',
                            title=Listdata[2]['item'],
                            text=Listdata[2]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[2]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[2]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[3]['url']+r'.jpg',
                            title=Listdata[3]['item'],
                            text=Listdata[3]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[3]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[3]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[4]['url']+r'.jpg',
                            title=Listdata[4]['item'],
                            text=Listdata[4]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[4]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[4]['_id']
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=linkurl+Listdata[5]['url']+r'.jpg',
                            title=Listdata[5]['item'],
                            text=Listdata[5]['text'],
                            actions=[
                                PostbackAction(
                                    label='รายละเอียด',
                                    # display_text='postback text1',
                                    data=r'info:'+Listdata[5]['_id']
                                ),
                                PostbackAction(
                                    label='ขอการติดต่อ',
                                    # display_text='postback text1',
                                    data=r'tel:'+Listdata[5]['_id']
                                ),
                            ]
                        )
                    ]
                )
            )

# def getimageMap() :
#     return '''