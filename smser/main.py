#! /usr/bin/env python2
# encoding:utf-8

import json
import Qcloud.Sms.sms as SmsSender

appid = 123456
appkey = "1234567890abcdef1234567890abcdef"    

# 普通单发
def sendSms(phone, content):  
    sender = SmsSender.SmsSingleSender(appid, appkey)
    result = sender.send(0, "86", phone, content, "", "")
    rsp = json.loads(result)
    print result

# 普通模板单发
def sendSmsWithParam(phone, templ_id, params):
    sender = SmsSender.SmsSingleSender(appid, appkey)
    result = sender.send_with_param("86", phone, templ_id, params, "", "", "")
    rsp = json.loads(result)
    print result

def main_handler(event, context):
    cmqMsg = None
    if event is not None and "Records" in event.keys():
        if len(event["Records"]) >= 1 and "CMQ" in event["Records"][0].keys():
            cmqMsgStr = event["Records"][0]["CMQ"]["msgBody"]
            cmqMsg = json.loads(cmqMsgStr)
    print cmqMsg
    if 'templ_id' in cmqMsg:
        sendSmsWithParam(cmqMsg['phone'], cmqMsg['templ_id'], cmqMsg['params'])
    else:
        sendSms(cmqMsg['phone'], cmqMsg['content'])
    return "send sms success"
