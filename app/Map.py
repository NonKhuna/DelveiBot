
from config import *
from linebot.models import ImagemapSendMessage, BaseSize, MessageImagemapAction, ImagemapArea

url = root_path + r"/get-image/imagemap.jpg"

def getimagemap():
    return ImagemapSendMessage(
        base_url=url+r'?_ignore=',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            MessageImagemapAction(
                text='หอพักหญิง2',
                area=ImagemapArea(
                    x=109, y=89, width=78, height=73
                )
            ),
            MessageImagemapAction(
                text='หอพักหญิง1',
                area=ImagemapArea(
                    x=237, y=200, width=65, height=63
                )
            ),
            MessageImagemapAction(
                text='หอพักหญิง3',
                area=ImagemapArea(
                    x=245, y=46, width=74, height=69
                )
            ),
            MessageImagemapAction(
                text='สำนักกิจ',
                area=ImagemapArea(
                    x=338, y=308, width=58, height=48
                )
            ),
            MessageImagemapAction(
                text='เรือนพยาบาล',
                area=ImagemapArea(
                    x=289, y=344, width=63, height=61
                )
            ),
            MessageImagemapAction(
                text='โรงประกอบอาหาร',
                area=ImagemapArea(
                    x=360, y=162, width=70, height=64
                )
            ),
            MessageImagemapAction(
                text='7',
                area=ImagemapArea(
                    x=472, y=130, width=61, height=63
                )
            ),
            MessageImagemapAction(
                text='อาคารศูนย์กีฬา',
                area=ImagemapArea(
                    x=462, y=241, width=63, height=58
                )
            ),
            MessageImagemapAction(
                text='ร้านสวัสดิการ',
                area=ImagemapArea(
                    x=399, y=294, width=55, height=53
                )
            ),
            MessageImagemapAction(
                text='หอพักหญิง4',
                area=ImagemapArea(
                    x=121, y=278, width=58, height=61
                )
            ),
            MessageImagemapAction(
                text='หอพักชาย2',
                area=ImagemapArea(
                    x=29, y=313, width=69, height=62
                )
            ),
            MessageImagemapAction(
                text='หอพักชาย1',
                area=ImagemapArea(
                    x=73, y=421, width=62, height=60
                )
            ),
            MessageImagemapAction(
                text='โรงซักรีด',
                area=ImagemapArea(
                    x=15, y=468, width=58, height=58
                )
            ),
            MessageImagemapAction(
                text='เรือนพักครู1',
                area=ImagemapArea(
                    x=220, y=521, width=60, height=64
                )
            ),
            MessageImagemapAction(
                text='เรือนพักครู2',
                area=ImagemapArea(
                    x=352, y=743, width=55, height=61
                )
            ),
            MessageImagemapAction(
                text='เรือนพักครู3',
                area=ImagemapArea(
                    x=558, y=910, width=60, height=70
                )
            ),
            MessageImagemapAction(
                text='อาคารผลิตน้ำดื่มโรงเรียน',
                area=ImagemapArea(
                    x=586, y=801, width=57, height=59
                )
            ),
            MessageImagemapAction(
                text='สวนป่า',
                area=ImagemapArea(
                    x=405, y=578, width=63, height=66
                )
            ),
            MessageImagemapAction(
                text='ฐานพระ',
                area=ImagemapArea(
                    x=465, y=464, width=69, height=63
                )
            ),
            MessageImagemapAction(
                text='เรือนพักรองผอ.',
                area=ImagemapArea(
                    x=653, y=675, width=61, height=59
                )
            ),
            MessageImagemapAction(
                text='Mathzone1',
                area=ImagemapArea(
                    x=675, y=604, width=60, height=62
                )
            ),
            MessageImagemapAction(
                text='Mathzone2',
                area=ImagemapArea(
                    x=712, y=467, width=60, height=61
                )
            ),
            MessageImagemapAction(
                text='อาคารคลินิกคณิตศาสตร์',
                area=ImagemapArea(
                    x=584, y=477, width=57, height=54
                )
            ),
            MessageImagemapAction(
                text='อาคารศิลปะ',
                area=ImagemapArea(
                    x=643, y=414, width=58, height=53
                )
            ),
            MessageImagemapAction(
                text='ตึกคอม',
                area=ImagemapArea(
                    x=603, y=311, width=58, height=64
                )
            ),
            MessageImagemapAction(
                text='อาคารรวมราชวิทย์',
                area=ImagemapArea(
                    x=710, y=215, width=58, height=55
                )
            ),
            MessageImagemapAction(
                text='อาคารรวม',
                area=ImagemapArea(
                    x=778, y=312, width=61, height=57
                )
            ),
            MessageImagemapAction(
                text='อาคารอำนวยการ',
                area=ImagemapArea(
                    x=846, y=236, width=58, height=55
                )
            ),
            MessageImagemapAction(
                text='อาคารโรงจอดรถ',
                area=ImagemapArea(
                    x=812, y=443, width=63, height=59
                )
            ),
            MessageImagemapAction(
                text='อาคารสถานที่',
                area=ImagemapArea(
                    x=773, y=526, width=61, height=57
                )
            ),
            MessageImagemapAction(
                text='หอสมุด',
                area=ImagemapArea(
                    x=965, y=472, width=58, height=60
                )
            )
        ]
    )
