
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
        #send_dict = {"api":"getChatRoomLists"}
        #send_dict = {"api":"getLoginQrCode"}
        # 发送文本消息
        #send_dict = {"api":"sendTextMessage", "code":1, "wxid":"wxid_qg0saisth0r222", "text":"测试"}
        # 获取群成员列表
        #send_dict = {"api":"getChatRoomUserLists", "code":6, "wxid":"7510115058@chatroom"}
        # 获取所有群列表
        #send_dict = {"api":"getChatRoomLists", "code":47}
        # 发送消息到文件传输助手
        #send_dict = {"api":"sendTextMessage","code":1,"wxid":"filehelper","text":'asdd',"time":replytime}
        #res.append(send_dict)
        # 获取联系人列表
        send_dict = {"api":"initContact", "code":45}
        res.append(send_dict)
        
    cnt = 0

    return jsonify(res)

#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567, debug=True)