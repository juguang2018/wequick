
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
    res = []
    global cnt
    if cnt == 1:
        # send_dict = {};
        # 打开微信    
        # send_dict = {"api":"openWeChat","sendId":"8859663","option":{}}
        # 获取登陆状态
        # send_dict = {"api":"getLoginStatus","sendId":"8859663","option":{}}       
        # 获取登录二维码
        #send_dict = {"api":"getLoginQrCode","sendId":"8859663","option":{}}
        # 微信退出登录
        
        # if request.args.get('wxid') == 'wxid_qg0saisth0r222':
        #     send_dict = {"api":"logout","sendId":"8859663","option":{}}             


        # 发送文本消息      
        # send_dict = {"api":"sendTextMessage", "sendId":"8859663","option":{"wxid":"filehelper", "text":"\ue41d\ue14c\ue312\ue112[\u7ea2\u5305][\u9e21]\ue056\ue057\ue414\ue405\ue106\ue418\ue417\ue404\ue40a\ue105\ue402\ue108\ue058\ue407\ue401\ue40f\ue40b\ue406\ue413\ue411\ue410\ue059\ue416\ue408"}}
        # 发送图片
        # send_dict = {"api":"sendPicMessage", "sendId":"8859663","option":{"wxid":"filehelper", "imgPath":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2381272227,3301346360&fm=26&gp=0.jpg"}}           
        # send_dict = {"api":"sendPicMessage", "sendId":"8859663","option":{"wxid":"filehelper", "imgPath":"C:\\22.jpg"}}
                            
        # 发送文件(文件地址为客户端的地址)       
        # send_dict = {"api":"sendFileMessage", "sendId":"8859663","option":{"wxid":"filehelper", "filePath":"C:\\test.md"}} 
        # 发送xml链接消息     
        # send_dict = {"api":"sendXmlMessage", "sendId":"8859663","option":{"wxid":"filehelper", "title":"标题", "url":"https://www.baidu.com", "desc":"描述", "pic":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2381272227,3301346360&fm=26&gp=0.jpg"}}
        
        # 发送名片    
        # send_dict = {"api":"sendCardMessage", "sendId":"8859663","option":{"wxid":"filehelper","wxidCard":"wxid_yfng437lnlyg22"}} 
        # 发送群邀请
        # send_dict = {"api":"sendChatroom", "sendId":"8859663","option":{"wxid":"filehelper", "chatroom":"233XXXX3@chatroom"}} 
        # 获取联系人
        # send_dict = {"api":"getContact", "sendId":"8859663","option":{"flag":2}}                  
        # 获取联系人 wxid
        # send_dict = {"api":"getUsersWxid", "sendId":"8859663","option":{}}      
        # 通过wxid获取好友或公众号详细信息()       
        # send_dict = {"api":"getUsersInfo", "sendId":"8859663","option":{"wxidLists":["xyz1sss53","wxid_ekXXXXXea12","wxid_kx9t7nb5jt0j22","wxid_kuey5cgldotq22"]}}           # 删除好友
        # send_dict = {"api":"delUser", "sendId":"8859663","option":{"wxid":"xyz103053"}}
        # 同意新好友,通过好友验证
        # send_dict = {"api":"acceptFriend", "sendId":"8859663","option":{"v1":"v1_c52face4bc84555a06877e72a1541a199b0207e7bc214f56abf27c6968302dcbc3771ddecc7749bc810ce60ba28800cf@stranger", "v2":"v2_86e849fd9f32c618d763b386253d7bed47c953beba61e6522811d26b426cdbda21df7b2fdd1c8f66d8ba724ff93410940a71ac6c4cb38879b3656a2d0f14c355dcc00bc8a6bd26b5b2dd7586881fb142@stranger"}}
        # if v1:
        #     send_dict = {"api":"acceptFriend", "sendId":"8859663","option":{"v1":v1, "v2":v2}}
        # 修改好友备注
        # send_dict = {"api":"updateAsName","sendId":"8859663","option":{"wxid":"wxid_qg0sXXXXXr222","asName":"苏大强"}}
        # 获取某个群成员详细信息列表
        # send_dict = {"api":"getChatRoomUsers", "sendId":"8859663","option":{"wxid":"175XXXX1544@chatroom"}}  
        # 修改群名称
        # send_dict = {"api":"updateChatRoomName", "sendId":"8859663","option":{"chatroom":"23058XXXX1@chatroom","name":"假装有群名2"}}
        # 踢群成员，当前微信必须有踢人权限(为群主或者群管理员)
        # send_dict = {"api":"delChatRoomUser", "sendId":"8859663","option":{"chatroom":"230580XXXX1@chatroom", "wxid":"xyz1XXXXX"}}
        # 修改群备注名称(我在本群的昵称)
        # send_dict = {"api":"updateRoomAsName", "sendId":"8859663","option":{"chatroom":"2305XXXX@chatroom", "name":"XXX33"}} 
        # 加群成员为好友
        # send_dict = {"api":"addRoomFriend","sendId":"8859663","option":{"chatroom":"23058XXXX1@chatroom","wxid":"wxid_qg0sXXXXX0r222","noticeWord":"我是多啦A梦"}}
        # 退群
        # send_dict = {"api":"exitChartRoom","sendId":"8859663","option":{"chatroom":"1911XXXX@chatroom"}}
        res.append(send_dict)
        
    cnt = 0

    return jsonify(res)

#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567, debug=True)