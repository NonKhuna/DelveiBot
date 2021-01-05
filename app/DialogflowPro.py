import dialogflow_v2
import os
import Mongo2,random
from google.protobuf.json_format import MessageToDict,MessageToJson
from config import project_id, credential_path

# Setup environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def reset_context(session_id) :
    client = dialogflow_v2.ContextsClient()
    parent = client.session_path(project_id, session_id)
    client.delete_all_contexts(parent)

def delete_Flow2_followup(session_id) :
    client = dialogflow_v2.ContextsClient()
    de1 = client.context_path(project_id, session_id,'flow2-followup')
    client.delete_context(de1)

def delete_Flow1_Lost_Itemfollowup(session_id) :
    client = dialogflow_v2.ContextsClient()
    de1 = client.context_path(project_id, session_id,'lost_item-followup')
    client.delete_context(de1)


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

def cnt_context(session_id) :
    client = dialogflow_v2.ContextsClient()
    parent = client.session_path(project_id, session_id)
    x=0
    for i in client.list_contexts(parent):
        x+=1
    return x
    
def Send_Dialogflow(session_id, text, language_code):
    session_client = dialogflow_v2.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    
    text_input = dialogflow_v2.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow_v2.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    Obj = MessageToDict(response)
    print(Obj)
    # reset_context(project_id, session_id)
    cnt=cnt_context(session_id)
    print("have context : {}".format(cnt))
    if cnt!=0 :
        flow1=Find_IDX('lost_item-followup',Obj,session_id)
        flow2=Find_IDX('flow2-followup',Obj,session_id)
        print("flow1 : {}".format(flow1[0]))
        print("flow2 : {}".format(flow2[0]))
        if flow2[1] and flow1[1] :
            tex=['ตกลงทำรายการไหนกันแน่ครับ แจ้งของหาย หรือ แจ้งตามหาเจ้าของ ผมสับสนแล้ว','ตกลงทำรายการแจ้งของหายหรือแจ้งตามหาเจ้าของครับ']
            reset_context(session_id)
            return [-1,[random.choice(tex),'รบกวนทำรายการใหม่ด้วยนะครับ']]

    intent=Obj['queryResult']['intent']['displayName']
    if intent in ['Lost_Money','Flow1_Lost_Item'] :
        delete_Flow2_followup(session_id)
    if intent in ['Report_Found_Money','Flow2_Report_Found'] :
        delete_Flow1_Lost_Itemfollowup(session_id)
    # print(response)
    # if intent == 'instructive-เจอแล้ว' :
    #     reset_context(session_id)
    #     return Obj
    test=Mongo2.MongoProcess(Obj,session_id,cnt)
            
    return test

# text = "แจ้งเจอหาเจ้าของครับ"
# text = "เงินสดครับ"
# p=Send_Dialogflow("s$@ski216zcddwsrd",text,"th")
# print(p)