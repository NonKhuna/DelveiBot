from google.protobuf.json_format import MessageToDict,MessageToJson
import json
import ast 
# text=input("")

data="""
{
  "type": "imagemap",
  "baseUrl": "PROVIDE_URL_FROM_YOUR_SERVER",
  "altText": "This is an imagemap",
  "baseSize": {
    "width": 1040,
    "height": 1040
  },
  "actions": [
    {
      "type": "message",
      "area": {
        "x": 469,
        "y": 121,
        "width": 137,
        "height": 119
      },
      "text": "สีส้มเหลือง"
    },
    {
      "type": "message",
      "area": {
        "x": 650,
        "y": 171,
        "width": 106,
        "height": 117
      },
      "text": "สีส้ม"
    },
    {
      "type": "message",
      "area": {
        "x": 780,
        "y": 293,
        "width": 107,
        "height": 110
      },
      "text": "สีส้มแดง"
    },
    {
      "type": "message",
      "area": {
        "x": 825,
        "y": 471,
        "width": 100,
        "height": 106
      },
      "text": "สีแดง"
    },
    {
      "type": "message",
      "area": {
        "x": 777,
        "y": 637,
        "width": 99,
        "height": 114
      },
      "text": "สีแดงอมม่วง"
    },
    {
      "type": "message",
      "area": {
        "x": 560,
        "y": 397,
        "width": 208,
        "height": 245
      },
      "text": "สีดำ"
    },
    {
      "type": "message",
      "area": {
        "x": 309,
        "y": 396,
        "width": 213,
        "height": 248
      },
      "text": "สีขาว"
    },
    {
      "type": "message",
      "area": {
        "x": 656,
        "y": 772,
        "width": 113,
        "height": 92
      },
      "text": "สีแดงอมม่วง"
    },
    {
      "type": "message",
      "area": {
        "x": 468,
        "y": 794,
        "width": 120,
        "height": 113
      },
      "text": "สีม่วง"
    },
    {
      "type": "message",
      "area": {
        "x": 309,
        "y": 756,
        "width": 114,
        "height": 117
      },
      "text": "ีสีน้ำเงิน"
    },
    {
      "type": "message",
      "area": {
        "x": 183,
        "y": 641,
        "width": 105,
        "height": 111
      },
      "text": "สีฟ้า"
    },
    {
      "type": "message",
      "area": {
        "x": 133,
        "y": 460,
        "width": 126,
        "height": 123
      },
      "text": "สีเขียว"
    },
    {
      "type": "message",
      "area": {
        "x": 188,
        "y": 295,
        "width": 106,
        "height": 108
      },
      "text": "สีเขียวอ่อน"
    },
    {
      "type": "message",
      "area": {
        "x": 308,
        "y": 172,
        "width": 124,
        "height": 105
      },
      "text": "สีเหลือง"
    }
  ]
}
"""
dd=ast.literal_eval(data)
for i in dd['actions'] :
    print("MessageImagemapAction(")
    print("\ttext=\'"+i['text']+'\',')
    print("\tarea=ImagemapArea(")
    print("\t\tx="+str(i['area']['x'])+', y='+str(i['area']['y'])+', width='+str(i['area']['width'])+', height='+str(i['area']['height']))
    print("\t)")
    print("),")
