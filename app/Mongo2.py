import pymongo,random,time
from pymongo import MongoClient
from DialogflowPro import * 
from Template import * 
# import linetest
cluster =MongoClient("localhost",27017)
db=cluster["admin"]
Maxdata = 1100
dbFlow1='Money_list_1'
dbFlow2='Money_list_2'
def checkTel(tel) :
    # print(type(tel))
    if len(tel) ==1 :
        # print(type(tel[0]))
        if len(tel[0]) ==10 :
            if tel[0][0] !='0' :
                return [-1,'หมายเลขไม่ถูกต้องนะครับ😤 ระบุเบอร์ที่ 0 นำหน้า']
            else :
                return tel[0]
        else :
            return [-1,"หมายเลขไม่ถูกต้องนะครับ😤"]
    if len(tel) == 3 :
        print(tel[0])
        print(tel[1])
        print(tel[2])
        if len(tel[0]) ==2 and len(tel[1]) ==4  and len(tel[2]) ==4:
            if tel[0][0] != '0' :
                return [-1,'หมายเลขไม่ถูกต้องนะครับ😤 ระบุเบอร์ที่ 0 นำหน้า']
            else : 
                return  tel[0]+tel[1]+tel[2]
        else :
            return [-1,'รบกวนระบุให้อยู่ในรูปแบบ 0X-XXX-XXXX นะครับ']


def Find_IDX(name,iput,UserId) :
    tmp=r'projects/delveibot-ver-4-gxfftn/agent/sessions/'+UserId+r'/contexts/' + name
    idx=0
    c=0
    for i in iput['queryResult']['outputContexts'] :
        if i['name']== tmp :
            c=1
            break
        idx+=1
    return [idx,c]

def MongoProcess(iput,UserId,cnt):
    
    intent=iput['queryResult']['intent']['displayName']
    listItem=[]
    if intent=='Cancel' :
        return ['Cancel',iput]       
    print("intent : {}".format(intent))
    # print("iput : {}".format(iput))
    
    if intent in ['Flow1-what item','Flow1-with item'] :
        da=Find_IDX('lost_item-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
            if item == 'เงิน' :
                tex=['เงินที่หายรวมกี่บาทครับ?','เงินหายรวมประมาณกี่บาทครับ','กี่บาทครับ?','หายกี่บาทครับ']
                listItem.append(random.choice(tex))
                return [-1,listItem]
            else :
                listItem.append(item+'สีอะไรครับ?')
                # listItem.append('ไม่ต้องละเอียดมากนะครับ ขอเป็นสีที่แยกออกง่ายๆเช่น ส้ม แดง เขียว ดำ ')
                return ["Mapcolour",listItem]
        else :
            print("ไม่เจอ context")

    if  intent in ['Flow1-where','flow1-item-place-money'] :
        da=Find_IDX('lost_item-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            if item == 'เงิน' :
                place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                number=iput['queryResult']['outputContexts'][da[0]]['parameters']['number']
                check=db[dbFlow2].count({'item' : item,"number":number,"state" : 0})
                if check == 0 :
                    if place=="Un" :
                            tex=['ไม่เป็นไรครับ ,อ๋อ จำสถานที่ไม่ได้นะครับ']
                            listItem.append(random.choice(tex))
                    else :
                        listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
                    return ['Report_Lost_money',str(number),listItem[0]]
                else :
                    check2=db[dbFlow2].count({'item' : item,"number":number,'place':place, "state" : 0})
                    if check2==0 :
                        data=db[dbFlow2].find({'item' : item,"number":number, "state" : 0})
                        return ['show',data,'มีคนเจอเงิน '+str(number)+'นะ แต่ไม่ได้เจอที่'+place]
                    else :
                        data=db[dbFlow2].find({"number":number,'place':place, "state" : 0}) 
                        # db[dbFlow2].update_one({"number":number,'place':place, "state" : 0},{ '$set' :{"state" : 1}})
                        return ['show',data,'มีคนนำมาแจ้งตามนี้นะ']
            else :
                brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
                colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
                place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                check=check=db[dbFlow2].count({'item' : item,"state" : 0})
                if check ==0 :
                    # print("in")
                    return ['donthave','ยังไม่มีใครมาแจ้งว่าเก็บ'+item+'ได้นะครับ']
                else :
                    if colour !='ไม่รู้' or colour !='ไม่มี':
                        check2=db[dbFlow2].count({'item' : item,'colour' : colour ,"state" : 0})
                        if check2 !=0 :
                            return ["donthave",'ยังไม่มีใครมาแจ้งว่าเก็บ'+item+colour+'ได้นะครับ']
                    elif brand !='ไม่รู้' or brand !='ไม่มี' :
                        check2=db[dbFlow2].find({'item' : item,'brand' : brand ,"state" : 0})
                        return ["have_f1",item,brand]
                    
                        
                
        else :
            print("ไม่เจอ context")

    if intent == 'Flow1- imageurl' :
        return 'ReportYN_yes'
    if intent == 'Flow1-where-yes' :
        da=Find_IDX('lost_item-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            if item== 'เงิน' :
                return 'ReportYN_yes'
            else :
                tex=['ผมขอรูปเพิ่มเติมด้วยนะครับ','ผมขอรูปของที่หายด้วยนะครับ']
                return ['get-image',random.choice(tex)]

    if intent in ['Flow1-where-no','Flow2-where-no'] :
        return ['Finish',2]

    if intent in ['Flow1-how much'] :
        # listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
        da=Find_IDX('lost_item-followup',iput,UserId)
        if 'fin' in iput['queryResult']['outputContexts'][da[0]]['parameters'] :
            tex=['หายอยู่แถวไหนครับ','จำได้ไหมครับ ว่าหายอยู่แถวไหน?','หายอยู่แถวไหนหรอครับ ?']
            listItem.append(random.choice(tex))
            return ["Map",listItem]
        else : 
            return [-1,random.choice(['เช็คตามตัวเอง ตามที่ต่างๆดีแล้วใช่ไหมครับ?','เช็คดีแล้วใช่ไหมครับ?'])]
    
    if intent == 'Flow1-how much - yes' :
        listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
        listItem.append(iput['queryResult']['fulfillmentMessages'][1]['text']['text'][0])
        return ["Map",listItem]

    if intent == 'Flow1-colour' :
        da=Find_IDX('lost_item-followup',iput,UserId)
        if da[1] :
            colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
            item=iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            if colour=='ไม่รู้' :
                tex=['อ่า งั้นไม่เป็นไรครับ','ไม่เป็นไรครับ']
                listItem.append(random.choice(tex))
            else :
                tex=item+colour+'นะครับ'
                listItem.append(tex)
            tex=['ของที่หายเป็นของแบรนด์ไรครับ?','ของที่หายมีชื่อแบรนด์ไหมครับ']
            listItem.append(random.choice(tex))
            return [-1,listItem]
    
    if intent == 'Flow1-brand' :
        da=Find_IDX('lost_item-followup',iput,UserId)
        if da[1] :
            brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
            item=iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
            if brand in ['ไม่รู้','ไม่มี'] :
                tex=['อ่า งั้นไม่เป็นไรครับ','ไม่เป็นไรครับ']
                listItem.append(random.choice(tex))
            else :
                tex=item+'ของ'+brand+'นะครับ'
                listItem.append(tex)
                # listItem.append(tex)
            tex2='หายที่ไหนหรอครับ?'
            listItem.append(tex2)
            # listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
            return ["Map",listItem]
    
    if intent == 'instructive-state5-body - no - custom' :
        return ["Map",['สามารถดูที่ต่างๆตามภาพด้านล่างได้เลยครับ']]
    if intent == 'Flow1-tel' :
        da=Find_IDX('lost_item-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            Retake =iput['queryResult']['outputContexts'][da[0]]['parameters']['Retake']
            tel =iput['queryResult']['outputContexts'][da[0]]['parameters']['tel']
            CC=checkTel(tel) 
            if type(CC) == list :
                return CC
            x=0
            for i in range(Maxdata) :
                Id=UserId+str(x)
                s=db[dbFlow1].count({"_id" : Id+'1'})
                if s==0 :
                    break
                x+=1
            if x==0 :
                Id=UserId+str(x)
                if item=='เงิน' :
                    number=iput['queryResult']['outputContexts'][da[0]]['parameters']['number']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow1].insert_one({"_id" : Id+'1',"souce": UserId, "tel" : CC, "place" : place , "number" : number, "retake" : Retake, "state" : 0 ,'item' : item ,'url' : 'coin', 'text' : 'แจ้งเงินหาย ' +str(number) +' บาท'})
                else :
                    url =iput['queryResult']['outputContexts'][da[0]]['parameters']['url']
                    brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
                    colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow1].insert_one({"_id" : Id+'1',"souce": UserId, "tel" : CC, "place" : place , 'brand' :brand ,'colour':colour , "retake" : Retake, "state" : 0 ,'item' : item,'url' : url,  'text' : 'แจ้ง' +item +'หาย' })
                return ["Finish",1]
            else :
                return "Want_More_infomation?"
        else :
            print("ไม่เจอ context")
    if intent == 'Flow1-tel-yes' :
        da=Find_IDX('lost_item-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            Retake =iput['queryResult']['outputContexts'][da[0]]['parameters']['Retake']
            tel =iput['queryResult']['outputContexts'][da[0]]['parameters']['tel']
            CC=checkTel(tel) 
            x=0
            for i in range(Maxdata) :
                Id=UserId+str(x)
                s=db[dbFlow1].count({"_id" : Id+'1'})
                if s==0 :
                    break
                x+=1
            print("CC :{}".format(CC)) 
            if item=='เงิน' :
                    number=iput['queryResult']['outputContexts'][da[0]]['parameters']['number']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow1].insert_one({"_id" : Id+'1',"souce": UserId, "tel" : CC, "place" : place , "number" : number, "retake" : Retake, "state" : 0,'item' : item,'url' : 'coin' ,'text' : 'แจ้งเงินหาย ' +str(number) +' บาท'})
            else :
                    url=iput['queryResult']['outputContexts'][da[0]]['parameters']['url']
                    brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
                    colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow1].insert_one({"_id" : Id+'1',"souce": UserId, "tel" : CC, "place" : place , 'brand' :brand ,'colour':colour , "retake" : Retake, "state" : 0 ,'url' : url,'item' : item ,'text' : 'แจ้ง' +item +'หาย'})
            return ["Finish",1]
        else :
            print("ไม่เจอ context")

    if intent == 'Flow1-where-yes - no' :
        tex=['งั้นไม่เป็นไรครับ']
        return [-2,"jpg : <jpg-nophotoo.jpg>",[]]
    
    #////////////////////////////////////////////////////////////////Found-item////////////////////////////////////////////////////////////////////
    
    
    if intent in ['Flow2-what item','Flow2-found item'] :
        da=Find_IDX('flow2-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
            if item == 'เงิน' :
                tex=['เก็บได้กี่บาทครับ','เก็บได้รวมกี่บาทครับ','กี่บาทครับ?','เจอเงินกี่บาทครับ']
                listItem.append(random.choice(tex))
                print(listItem)
                return [-1,listItem]
            else :
                listItem.append(item+'สีอะไรครับ?')
                listItem.append('เพื่อให้สามารถหาได้ง่าย เลือกสีตามนี้เลยครับ')
                return ["Mapcolour",listItem]
        else :
            print("ไม่เจอ context")
    if intent in ['Flow2-how much'] :
        listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
        return ["Map",iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0]]

    if  intent in ['Flow2-where','Flow2-item colour brand'] :
        da=Find_IDX('flow2-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            if item == 'เงิน' :
                place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                number=iput['queryResult']['outputContexts'][da[0]]['parameters']['number']
                check=db[dbFlow1].count({'item' : item,"number":number,"state" : 0})
                if check == 0 :
                    if place=="Un" :
                            tex=['ไม่เป็นไรครับ ,อ๋อ จำสถานที่ไม่ได้นะครับ']
                            listItem.append(random.choice(tex))
                    else :
                        listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
                    return ['Report_Found_money',str(number),listItem[0]]
                else :
                    check2=db[dbFlow1].count({'item' : item,"number":number,'place':place, "state" : 0})
                    if check2==0 :
                        data=db[dbFlow1].find({'item' : item,"number":number, "state" : 0})
                        return ['show',data]
                    else :
                        data=db[dbFlow1].find({'item' : item,"number":number,'place':place, "state" : 0}) 
                        # db[dbFlow1].update_one({"number":number,'place':place, "state" : 0},{ '$set' :{"state" : 1}})
                        return ['show',data]
            else :
                brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
                colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
                place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                check=db[dbFlow1].count({'item' : item,"state" : 0})
                if check ==0 :
                    # print("in")
                    return ['donthave','ยังไม่มีใครมาแจ้งว่า'+item+'หายนะครับ']
                else :
                    if colour !='ไม่รู้' and  colour !='ไม่มี':
                        check2=db[dbFlow1].count({'item' : item,'colour' : colour ,"state" : 0})
                        if check2 ==0 :
                            data =db[dbFlow1].find({'item' : item,"state" : 0})
                            return ["show",data,'ยังไม่มีใครมาแจ้งว่า'+item+colour+'หายนะครับ แต่มีคนแจ้ง'+item+'หาย']
                        else :
                            if brand!='ไม่รู้' and brand !='ไม่มี' :
                                check3=db[dbFlow1].count({'item' : item,'colour' : colour ,'brand' : brand,"state" : 0})
                                if check3==0 :
                                    data=data =db[dbFlow1].find({'item' : item,'colour' : colour,"state" : 0})
                                    return ["show",data,'ยังไม่มีใครมาแจ้งว่า'+item+colour+'ของ'+brand+'หายนะครับ แต่มีคนแจ้ง'+item+colour+'หาย']
                                else :
                                    data =db[dbFlow1].find({'item' : item,'colour' : colour ,'brand' : brand,"state" : 0})
                                    return ["show",data,'มีคนแจ้งว่าหายตามข้อมูลนะครับ']
                            else :
                                data =db[dbFlow1].find({'item' : item,'colour' : colour,"state" : 0})
                                return ["show",data,'มีคนแจ้ง'+item+colour+'หาย ตามนี้นะครับ']
                    elif brand !='ไม่รู้' and brand !='ไม่มี' :
                        check3=db[dbFlow1].count({'item' : item ,'brand' : brand,"state" : 0})
                        if check3==0 :
                            data =db[dbFlow1].find({'item' : item,"state" : 0})
                            return ["show",data,'ยังไม่มีใครมาแจ้งว่า'+item+'ของ'+brand+'หายนะครับ แต่มีคนแจ้ง'+item+'หาย']
                        else :
                            data=db[dbFlow1].find({'item' : item ,'brand' : brand,"state" : 0})
                            return ["show",data,'มีคนแจ้งว่า'+item+'หายตามนี้นะครับ']
                    else :
                        data =db[dbFlow1].find({'item' : item,"state" : 0})
                        return ["show",data,"มีคนแจ้ง"+item+'หายตามนี้ครับ']
                    
                        
                
        else :
            print("ไม่เจอ context")

    if intent == 'Flow2- imageurl' :
        return 'ReportYN_yes_Found'
    if intent == 'Flow2-where-yes' :
        da=Find_IDX('flow2-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            if item== 'เงิน' :
                return 'ReportYN_yes_Found'
            else :
                tex=['ผมขอรูปเพิ่มเติมด้วยนะครับ','ผมขอรูปของที่หายด้วยนะครับ']
                return ['get-image',random.choice(tex)]

    if intent in ['Flow2-where-no'] :
        return ['Finish',2]

    if intent == 'Flow2-colour' :
        da=Find_IDX('flow2-followup',iput,UserId)
        if da[1] :
            colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
            item=iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            if colour=='ไม่รู้' :
                tex=['อ่า งั้นไม่เป็นไรครับ','ไม่เป็นไรครับ']
                listItem.append(random.choice(tex))
            else :
                tex=item+colour+'นะครับ'
                listItem.append(tex)
            tex=['ของที่เก็บได้ป็นของแบรนด์ไรครับ?','ของที่เก็บได้มีชื่อแบรนด์ไหมครับ?']
            listItem.append(random.choice(tex))
            return [-1,listItem]
    
    if intent == 'Flow2-brand' :
        da=Find_IDX('flow2-followup',iput,UserId)
        if da[1] :
            brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
            item=iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
            if brand in ['ไม่รู้','ไม่มี'] :
                tex=['อ่า งั้นไม่เป็นไรครับ','ไม่เป็นไรครับ']
                listItem.append(random.choice(tex))
            else :
                tex=item+'ของ'+brand+'นะครับ'
                listItem.append(tex)
                # listItem.append(tex)
            tex2=['เก็บได้ที่ไหนหรอครับ?','เก็บได้อยู่ไหนครับ?']
            listItem.append(random.choice(tex2))
            # listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
            return ['Map',listItem]
    
    
    if intent == 'Flow2-tel' :
        da=Find_IDX('flow2-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            Retake =iput['queryResult']['outputContexts'][da[0]]['parameters']['Retake']
            tel =iput['queryResult']['outputContexts'][da[0]]['parameters']['tel']
            CC=checkTel(tel) 
            if type(CC) == list :
                return CC
            x=0
            for i in range(Maxdata) :
                Id=UserId+str(x)
                s=db[dbFlow2].count({"_id" : Id+'2'})
                if s==0 :
                    break
                x+=1
            if x==0 :
                Id=UserId+str(x)
                if item=='เงิน' :
                    number=iput['queryResult']['outputContexts'][da[0]]['parameters']['number']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow2].insert_one({"_id" : Id+'2',"souce": UserId, "tel" : CC, "place" : place , "number" : number, "retake" : Retake, "state" : 0 ,'item' : item ,'url' : 'coin', 'text' : 'แจ้งเงินหาย ' +str(number) +' บาท'})
                else :
                    url =iput['queryResult']['outputContexts'][da[0]]['parameters']['url']
                    brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
                    colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow2].insert_one({"_id" : Id+'2',"souce": UserId, "tel" : CC, "place" : place , 'brand' :brand ,'colour':colour , "retake" : Retake, "state" : 0 ,'item' : item,'url' : url,  'text' : 'แจ้ง' +item +'หาย' })
                return ["Finish",1]
            else :
                return "Want_More_infomation?"
        else :
            print("ไม่เจอ context")
    if intent == 'Flow2-tel-yes' :
        da=Find_IDX('flow2-followup',iput,UserId)
        if da[1] :
            item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
            Retake =iput['queryResult']['outputContexts'][da[0]]['parameters']['Retake']
            tel =iput['queryResult']['outputContexts'][da[0]]['parameters']['tel']
            CC=checkTel(tel) 
            x=0
            for i in range(Maxdata) :
                Id=UserId+str(x)
                s=db[dbFlow2].count({"_id" : Id+'2'})
                if s==0 :
                    break
                x+=1
            print("CC :{}".format(CC)) 
            if item=='เงิน' :
                    number=iput['queryResult']['outputContexts'][da[0]]['parameters']['number']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow2].insert_one({"_id" : Id+'2',"souce": UserId, "tel" : CC, "place" : place , "number" : number, "retake" : Retake, "state" : 0,'item' : item,'url' : 'coin' ,'text' : 'แจ้งเก็บเงินได้ ' +str(number) +' บาท'})
            else :
                    url=iput['queryResult']['outputContexts'][da[0]]['parameters']['url']
                    brand=iput['queryResult']['outputContexts'][da[0]]['parameters']['brand']
                    colour=iput['queryResult']['outputContexts'][da[0]]['parameters']['colour']
                    place=iput['queryResult']['outputContexts'][da[0]]['parameters']['place']
                    db[dbFlow2].insert_one({"_id" : Id+'2',"souce": UserId, "tel" : CC, "place" : place , 'brand' :brand ,'colour':colour , "retake" : Retake, "state" : 0 ,'url' : url,'item' : item ,'text' : 'แจ้งเก็บ' +item +'ได้'})
            return ["Finish",1]
        else :
            print("ไม่เจอ context")

    if intent == 'Flow2-where-yes - no' :
        tex=['งั้นไม่เป็นไรครับ']
        return [-2,"jpg : <jpg-nophotoo.jpg>",[]]
    

    #////////////////////////////////////////////////////////////////instructive///////////////////////////////////////////////////////////////////////////////////////
    if intent == 'Flow1-how much - no' :
        listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
        da=Find_IDX('lost_item-followup',iput,UserId)
        item = iput['queryResult']['outputContexts'][da[0]]['parameters']['item']
        if item in ['เงิน'] :
                listItem.append('ปกติได้พกกระเป๋าสตางค์ หรือ กระเป๋าเงินไหมครับ')
                return [-2,'<in-instructive-money>',listItem]
        elif item in ['แหวน','แว่นตา'] :
            tex=['ลองเช็คตัวเองดูยังว่าเราหลงใส่อยู่รึเปล่า เพราะก็เคยมีคนใส่เองแล้วหาไม่เจอนะ','หลงใส่เองอยู่รึปล่าวว ตามตัวเองไรงี้']
            listItem.append(random.choice(tex))
            return [-1,listItem]
        else :
            tex=['ได้หลงให้เพื่อนยืมรึเปล่าครับ?','มีเพื่อนหลงหยิบไปไม่บอกรึเปล่า?']
            listItem.append(random,choice(tex))
            return [-2,'<in-instructive-other>',listItem]
        
    if intent in ['instructive-state3-item','lost_item-what i cando'] :
        da=Find_IDX('instructive-state3-item-followup',iput,UserId)
        if da[1] : 
            item=get_param(iput,da,'item')
            listItem.append(iput['queryResult']['fulfillmentMessages'][0]['text']['text'][0])
            if item in ['เงิน'] :
                # tex=item+'หายนะครับ'
                listItem.append('ปกติได้พกกระเป๋าสตางค์ หรือ กระเป๋าเงินไหมครับ')
                return [-2,'<in-instructive-money>',listItem]
            elif item in ['แหวน','แว่นตา'] :
                tex=['ลองเช็คตัวเองดูยังว่าเราหลงใส่อยู่รึเปล่า เพราะก็เคยมีคนใส่เองแล้วหาไม่เจอนะ','หลงใส่เองอยู่รึปล่าวว ตามตัวเองไรงี้']
                listItem.append(random.choice(tex))
                return [-1,listItem]
            else :
                tex=['ได้หลงให้เพื่อนยืมรึเปล่าครับ?','มีเพื่อนหลงหยิบไปไม่บอกรึเปล่า?']
                listItem.append(random.choice(tex))
                return [-2,'<in-instructive-other>',listItem]
    if intent =='instructive-state8' :
        return ['instructive-state8']
    # if intent == 
    return iput
def disdata(_id) :
    flow=_id[len(_id)-1]
    if flow=='1' :
        data=list(db[dbFlow1].find({"_id" : _id}))
        data=data[0]
        if data['item'] == "เงิน" :
            tex='ของที่หาย :'+"เงิน\n"+'จำนวน :'+str(data['number'])+'\n'+'อยู่ที่ :'+data['place']
            # print('ของที่หาย :'+"เงิน")
            # print('จำนวน :'+data['number'])
            # print('อยู่ที่ :'+data['place'])
        else :
            tex='ของที่หาย : '+data['item']+'\nสี : '+data['colour']+'\nเป็นของแบรนด์ : '+data['brand']+'\n'+'หายอยู่ที่ :'+data['place']
        return tex
    if flow=='2' :
        # print(_id)
        data=list(db[dbFlow2].find({"_id" : _id}))
        data=data[0]
        if data['item'] == "เงิน" :
            tex='ของที่เก็บได้ :'+"เงิน\n"+'จำนวน :'+str(data['number'])+'\n'+'อยู่ที่ :'+data['place']
            # print('ของที่เก็บได้ :'+"เงิน")
            # print('จำนวน :'+data['number'])
            # print('อยู่ที่ :'+data['place'])
        else :
            tex='ของที่เก็บได้ : '+data['item']+'\nสี : '+data['colour']+'\nเป็นของแบรนด์ : '+data['brand']+'\n'+'เจออยู่ที่ :'+data['place']
        return tex


def distel(_id) :
    flow=_id[len(_id)-1]
    print(flow)
    if flow=='1' :
        data=list(db[dbFlow1].find({"_id" : _id}))
        print(_id)
        data=data[0]
        if data['retake'] == 'my' :
            tex='คนแจ้ง ไม่สะดวกรับเอง ให้ติดต่อคืนได้ที่สำนักกิจ\n' + 'เบอร์ติดต่อเพิ่มเติม '+ data['tel']
        else :
             tex='คนแจ้ง สะดวกคืนด้วยตัวเอง\n' + 'เบอร์ติดต่อเพิ่มเติม'+ data['tel']
        return tex
    if flow=='2' :
        # print(_id)
        data=list(db[dbFlow2].find({"_id" : _id}))
        data=data[0]
        print("tel2")
        if data['retake'] == 'my' :
            tex='คนแจ้ง ไม่สะดวกคืนด้วยตัวเอง ให้ติดต่อรับได้ที่สำนักกิจ\n' + 'เบอร์ติดต่อเพิ่มเติม '+ data['tel']
        else :
             tex='คนแจ้ง สะดวกรับคืนด้วยตัวเอง\n' + 'เบอร์ติดต่อเพิ่มเติม'+ data['tel']
        return tex

def load_data(_id):
    data=db[dbFlow1].find({"souce" : _id})
    return data

# tex = 'data:asdfpe445'
# texne=''
# x=0
# for i in tex :
#     x+=1
#     if x==len(tex) :
#         break
#     texne+=i
# print(texne)
# coll.insert_one({'_id' : 2 ,'num' : 200})
# db[dbFlow2].update_one({"number":300 ,'place':'สนามบาส', "state" : 1},{ '$set' :{"state" : 0,'item' : 'เงิน'}})
# db[dbFlow2].insert_one({"tel" : '0804782205', "place" : 'สนามบาส' , "number" : '300', "retake" : 'ตัวเอง', "state" : 0,'item' : 'เงิน'})
# ID='adsfe581'+'2'
# db[dbFlow2].insert_one({"_id" : 'adsfe5ฟหกดำ'+'2',"souce": "UserId", "tel" : '0804782205', "place" : "สนามบาส" , "number" : 500, "retake" : 'สำนักงาน', "state" : 0 ,'item' : 'เงิน' ,'url' : 'coin','text' : 'มีแจ้งเงินหาย ' +'500' +' บาท'})
# test=db[dbFlow2].find({"_id":"เadsfe5ฟหกดำ2"})