
# -*- coding: utf-8 -*-
import os
import operator
import logging

from flask import Flask
from flask import request
from flask import jsonify

from random import choice
import random
import requests
from datetime import datetime
import json
import time

from const import *

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

cnt = 1

#-------------------------------------------------------------------------------------------
def writelog(fpath, data):
    f = open(fpath,'a+',encoding='utf-8')
    f.write(data)
    f.write('\n\n')
    f.close()

#-------------------------------------------------------------------------------------------
@app.route('/admin', methods=['GET'])
def hello_world():
    return 'Hello dear!!'

#-------------------------------------------------------------------------------------------
@app.route('/recieve_msg', methods=['POST'])
def recieve_msg():
    res = []
    
    if request.method=='POST':
        request_object = json.dumps(request.json)
        print (request_object)
        app.logger.info("request_object = %s\n", request_object)
        print (request_object)
        
        writelog('./recieve.log', str(request_object))

        return  jsonify(res)
    else:
        app.logger.info("recv data is:%s", str(request.get_data()))
        return jsonify(["暂时只支持Post方式"])
    
#-------------------------------------------------------------------------------------------
@app.route('/send_msg', methods=['GET'])
def send_msg():
    cwxid  = request.args.get('wxid')
    pid = request.args.get('pid')

    res = []
    global cnt
    if cnt == 1:
        send_dict = {};
        # 打开微信    
        # send_dict = {"api":"openWeChat","sendId":"8859663","option":{}}
      
        # 获取登录二维码
        # send_dict = {"api":"getLoginQrCode","sendId":"8859663","option":{}} 
         
        # 获取登陆状态
        # send_dict = {"api":"getLoginStatus","sendId":"8859663","option":{}}   
        
        # 微信退出登录
        # send_dict = {"api":"logout","sendId":"8859663","option":{}} 

        # 获取联系人
        # send_dict = {"api":"getContact", "sendId":"8859663","option":{"flag":1}} 

        # 获取联系人 wxid
        # send_dict = {"api":"getUsersWxid", "sendId":"8859663","option":{}} 

        # 通过wxid获取好友或公众号详细信息()       
        # send_dict = {"api":"getUsersInfo", "sendId":"8859663","option":{"wxidLists":["","","",""]}}

        # 获取某个群内全部成员详细信息列表
        # send_dict = {"api":"getChatRoomUsers", "sendId":"8859663","option":{"wxid":"xxxxxx@chatroom"}}  

        # 获取单个群成员的群昵称
        # send_dict = {"api":"getChatRoomUserNick", "sendId":"8859663","option":{"chatroom":"xxxxxx@chatroom", "wxid":""}} 

        # 发送文本消息      
        #send_dict = {"api":"sendTextMessage", "sendId":"8859663","option":{"wxid":"filehelper", "text":"\ue41d\ue14c\ue312\ue112[\u7ea2\u5305][\u9e21]\ue056\ue057\ue414\ue405\ue106\ue418\ue417\ue404\ue40a\ue105\ue402\ue108\ue058\ue407\ue401\ue40f\ue40b\ue406\ue413\ue411\ue410\ue059\ue416\ue408"}}

        # 发送图片
        # 在线图片
        #send_dict = {"api":"sendPicMessage", "sendId":"8859663","option":{"wxid":"filehelper", "imgPath":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2381272227,3301346360&fm=26&gp=0.jpg"}}           
        # 客户端所在PC本地图片地址
        #send_dict = {"api":"sendPicMessage", "sendId":"8859663","option":{"wxid":"filehelper", "imgPath":"C:\\图片\\029.jpg"}}
         
        # 发送文件
        # 客户端所在PC本地文件地址，文件内容不可为空，否则发不出去
        #send_dict = {"api":"sendFileMessage", "sendId":"8859663","option":{"wxid":"filehelper", "filePath":"C:\\文件\\测试.pdf"}} 

        # 发送xml链接消息     
        #send_dict = {"api":"sendXmlMessage", "sendId":"8859663","option":{"wxid":"filehelper", "title":"标题", "url":"https://www.baidu.com", "desc":"描述", "pic":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2381272227,3301346360&fm=26&gp=0.jpg"}}

        # 发送名片    
        #send_dict = {"api":"sendCardMessage", "sendId":"8859663","option":{"wxid":"filehelper","wxidCard":"xxxx"}} 

        # 发送群邀请
        #send_dict = {"api":"sendChatroom", "sendId":"8859663","option":{"wxid":"filehelper", "chatroom":"xxxxx@chatroom"}} 
                 
        # 删除好友
        #send_dict = {"api":"delUser", "sendId":"8859663","option":{"wxid":"xxxxxx"}}

        # 同意新好友,通过好友验证       
        # send_dict = {"api":"acceptFriend", "sendId":"8859663","option":{"v1":v1, "v2":v2}}

        # 修改好友备注
        #send_dict = {"api":"updateAsName","sendId":"8859663","option":{"wxid":"xxxxxx","asName":"大大"}}

        # 修改群名称
        #send_dict = {"api":"updateChatRoomName", "sendId":"8859663","option":{"chatroom":"xxxx@chatroom","name":"测试群"}}

        # 踢群成员，当前微信必须有踢人权限(为群主或者群管理员)
        #send_dict = {"api":"delChatRoomUser", "sendId":"8859663","option":{"chatroom":"xxxxxx@chatroom", "wxid":"xxxxxxx"}}

        # 修改群备注名称(我在本群的昵称)
        #send_dict = {"api":"updateRoomAsName", "sendId":"8859663","option":{"chatroom":"xxxxx@chatroom", "name":"测试测试"}} 

        # 加群成员为好友
        #send_dict = {"api":"addRoomFriend","sendId":"8859663","option":{"chatroom":"xxxxx@chatroom","wxid":"xxxxx","noticeWord":"我是多啦A梦"}}
        
        # 创建群聊
        #send_dict = {"api":"createChatRoom","sendId":"8859663","option":{"wxidLists":['xxxx','xxxx','xxxxxx']}}

        # 退群
        #send_dict = {"api":"exitChatRoom","sendId":"8859663","option":{"chatroom":"xxxxxx@chatroom"}}

        # 接受转账
        # send_dict = {"api":"acceptBankTransfer", "sendId":"8859663","option":{"transferid":"2132131232131232131", "wxid":"xxxxxx"}}

        # 关闭进程
        # send_dict = {"api":"closeProcess","sendId":"8859663","option":{"pid":pid}}

        res.append(send_dict)
        
    cnt = 0

    return jsonify(res)

#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567, debug=True)