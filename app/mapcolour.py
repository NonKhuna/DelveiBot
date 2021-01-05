from config import *
from linebot.models import MessageImagemapAction, ImagemapSendMessage, BaseSize, ImagemapArea

url = root_path + r"/get-image/color_circle.png"


def getimagemapcolour():
    print(url)
    return ImagemapSendMessage(
        base_url=url+r'?_ignore=',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            MessageImagemapAction(
                text='สีส้มเหลือง',
                area=ImagemapArea(
                    x=469, y=121, width=137, height=119
                )
            ),
            MessageImagemapAction(
                text='สีส้ม',
                area=ImagemapArea(
                    x=650, y=171, width=106, height=117
                )
            ),
            MessageImagemapAction(
                text='สีส้มแดง',
                area=ImagemapArea(
                    x=780, y=293, width=107, height=110
                )
            ),
            MessageImagemapAction(
                text='สีแดง',
                area=ImagemapArea(
                    x=825, y=471, width=100, height=106
                )
            ),
            MessageImagemapAction(
                text='สีแดงอมม่วง',
                area=ImagemapArea(
                    x=777, y=637, width=99, height=114
                )
            ),
            MessageImagemapAction(
                text='สีดำ',
                area=ImagemapArea(
                    x=560, y=397, width=208, height=245
                )
            ),
            MessageImagemapAction(
                text='สีขาว',
                area=ImagemapArea(
                    x=309, y=396, width=213, height=248
                )
            ),
            MessageImagemapAction(
                text='สีแดงอมม่วง',
                area=ImagemapArea(
                    x=656, y=772, width=113, height=92
                )
            ),
            MessageImagemapAction(
                text='สีม่วง',
                area=ImagemapArea(
                    x=468, y=794, width=120, height=113
                )
            ),
            MessageImagemapAction(
                text='ีสีน้ำเงิน',
                area=ImagemapArea(
                    x=309, y=756, width=114, height=117
                )
            ),
            MessageImagemapAction(
                text='สีฟ้า',
                area=ImagemapArea(
                    x=183, y=641, width=105, height=111
                )
            ),
            MessageImagemapAction(
                text='สีเขียว',
                area=ImagemapArea(
                    x=133, y=460, width=126, height=123
                )
            ),
            MessageImagemapAction(
                text='สีเขียวอ่อน',
                area=ImagemapArea(
                    x=188, y=295, width=106, height=108
                )
            ),
            MessageImagemapAction(
                text='สีเหลือง',
                area=ImagemapArea(
                    x=308, y=172, width=124, height=105
                )
            ),
        ]
    )
