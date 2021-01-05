
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


linkurl= root_path + r'/get-image/'

def show_state(Listdata) :
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
                                        label='ยกเลิก',
                                        # display_text='postback text1',
                                        data=r'delete:'+Listdata[0]['_id']
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
                                        label='ยกเลิก',
                                        # display_text='postback text1',
                                        data=r'delete:'+Listdata[0]['_id']
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
                                        label='ยกเลิก',
                                        # display_text='postback text1',
                                        data=r'delete:'+Listdata[1]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[0]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[1]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[2]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[0]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[1]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[2]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[3]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[0]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[1]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[2]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[3]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[4]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[0]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[1]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[2]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[3]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[4]['_id']
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
                                    label='ยกเลิก',
                                    # display_text='postback text1',
                                    data=r'delete:'+Listdata[5]['_id']
                                ),
                            ]
                        )
                    ]
                )
            )