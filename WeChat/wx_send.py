# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import re
import json

import itchat

from settings import SEND_NAME


itchat.auto_login(enableCmdQR=2, hotReload=True)
send_to_user = itchat.search_friends(name=SEND_NAME)[0]['UserName']


@itchat.msg_register(itchat.content.TEXT)
def send_message(msg):
    print msg.user
    wxid = msg.user['UserName']
    nickname = msg.user['NickName']
    remark_name = msg.user['RemarkName']
    text_msg = msg['Text']
    if wxid != send_to_user:
        text_msg = 'nick_name:{nick_name}, remark_name:{remark_name}, msg:{msg}'.format(
            nick_name=nickname, remark_name=remark_name, msg=text_msg
        )
        time.sleep(3)
        to_user = send_to_user

    else:
        nick_name = re.findall(r"！(.+?)！", text_msg)[0]
        try:
            try:
                text_msg = re.findall(r"0(.+?)0", text_msg)[0]
            except:
                text_msg = 'not get message!'
            wx = itchat.search_friends(name=nick_name)
            to_user = wx[0]['UserName']
        except:
            to_user = send_to_user
            text_msg = 'sorry, to user id is error, please edit message!'
        time.sleep(3)
    itchat.send(text_msg, toUserName=to_user)


itchat.run()
