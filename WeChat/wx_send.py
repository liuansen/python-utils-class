# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import re

import itchat

from settings import SEND_NAME


# 扫码登录
itchat.auto_login(enableCmdQR=2, hotReload=True)
# 将接收到的消息发送到指定用户
send_to_user = itchat.search_friends(name=SEND_NAME)[0]['UserName']


@itchat.msg_register(itchat.content.TEXT)
def send_message(msg):
    # 发送给我消息的用户信息
    # 微信ID
    wxid = msg.user['UserName']
    # 昵称
    nickname = msg.user['NickName']

    # 转发到我的主微信上
    # 文本消息
    text_msg = msg['Text']
    if wxid != send_to_user:
        # 拼接消息，暂时实现文本类消息
        message = {
            'wxid': wxid,
            'nickname': nickname,
            'msg': text_msg
        }
        print 'nickname:', nickname
        print 'message1:', message
        time.sleep(3)
        itchat.send(message, toUserName=send_to_user)
    else:
        wxid = re.findall(r"。(.+?)。", text_msg)
        if len(wxid) != 0:
            send_to_users = wxid[0]
        else:
            # 从主微信上接收消息发送到对应用户
            name = re.findall(r"！(.+?)！", text_msg)
            if len(name) != 0:
                # 发送到对应用户的微信id
                send_to_users = itchat.search_friends(name=name)[0]['UserName']
            else:
                # 获取送达用户异常， 将消息发回主微信
                text_msg = '获取送达用户信息异常，请重新编辑发送消息'
                send_to_users = send_to_user
            print 'name2:', name
        print 'message2:', text_msg
        time.sleep(3)
        itchat.send(text_msg, toUserName=send_to_users)


itchat.run()
