# WeChat API 个人微信号API/微信协议/独家接口/PC hook
# 适配所有类型个人微信号及版本
# 支持傻瓜式二次开发
# WeQuick 接口规范
![alt logo](https://wequick-1257130190.cos.ap-shanghai.myqcloud.com/img/logo.png)

------
**商务合作请加微信：abcdefg_12345654321**

<img src="https://wequick-1257130190.cos.ap-shanghai.myqcloud.com/img/xiaore.jpg" width="120" align=center/>

**商务合作请加微信：DiscoveryUpup**

<img src="https://wequick-1257130190.cos.ap-shanghai.myqcloud.com/img/service.png" width="120" align=center/>

正常使用软件不会导致封号。

**杀毒软件会对软件的正常运行构成影响，导致各种问题，请在使用前关闭杀毒软件。**

------
# 注意事项
## 指令发出的方式有两种
1. 通过 send_msg 轮询接口发出
2. 通过 receive_msg 接口 return 发出

## 接口所用编码均为utf-8编码

## 服务端发出的指令格式应该是一个json数组，示例：
```json
[{"sendId":"","api":"sendTextMessage","option":{"wxid":"","text":""}}]
```

# receive_msg
一.监听微信内部发生的各种事件,并主动向回调接口发送这些事件的详细信息. 这些事件的种类有:  
### 登录登出
01. [上报登陆二维码(reportQrCodeMessage)](#reportQrCodeMessage)  
02. [上报当前登录微信详细信息(reportLoginUser)](#reportLoginUser)  
03. [上报退出登录事件(reportLogout)](#reportLogout)  
### 好友相关
04. [上报普通好友列表(reportContacts)](#reportContacts)  
05. [上报企业好友列表(reportImContacts)](#reportImContacts)  
06. [上报公众号列表(reportPublics)](#reportPublics)  
07. [上报单个普通好友信息(reportSingleContact)](#reportSingleContact)  
08. [上报任意普通微信反查详细信息(reportUpdateContact)](#reportUpdateContact)  
09. [上报联系人新增通知(reportContactAdd)](#reportContactAdd)  
10. [上报联系人删除通知(reportContactDel)](#reportContactDel)  
### 群相关
11. [上报普通群列表(reportChatRooms)](#reportChatRooms)  
12. [上报企业群列表(reportImRooms)](#reportImRooms)  
13. [上报单个普通群成员信息(reportSingleChatRoomMembers)](#reportSingleChatRoomMembers)  
14. [上报单个企业群成员信息(reportSingleImRoomMembers)](#reportSingleImRoomMembers)  
15. [上报通过二维码进群返回状态(reportAcceptQrCodeChatRoom)](#reportAcceptQrCodeChatRoom)  
16. [上报群成员新增通知(reportChatRoomMemberAdd)](#reportChatRoomMemberAdd)  
17. [上报群成员删除通知(reportChatRoomMemberDel)](#reportChatRoomMemberDel)  
18. [上报检测到的新群通知(reportNewChatRoom)](#reportNewChatRoom)  
19. [上报退群或被踢通知(reportChatRoomQuit)](#reportChatRoomQuit)  
### 消息相关
20. [上报文本消息(reportTextMessage)](#reportTextMessage)  
21. [上报图片消息(reportPicMessage)](#reportPicMessage)  
22. [上报文件消息(reportFileMessage)](#reportFileMessage)  
23. [上报视频消息(reportVideoMessage)](#reportVideoMessage)  
24. [上报语音消息(reportVoiceMessage)](#reportVoiceMessage)  
25. [上报GIF表情消息(reportGifMessage)](#reportGifMessage)  
26. [上报个人名片消息(reportCardMessage)](#reportCardMessage)  
27. [上报位置消息(reportLocationMessage)](#reportLocationMessage)  
28. [上报链接消息(网页或群邀请)(reportLinkMessage)](#reportLinkMessage)  
29. [上报小程序消息(reportMiniMessage)](#reportMiniMessage)  
30. [上报转账消息(reportTransferMessage)](#reportTransferMessage)  
31. [上报无痕清理僵尸粉消息(reportZombieCheckMessage)](#reportZombieCheckMessage)  
32. [上报解密图片消息(reportDecryptPicMessage)](#reportDecryptPicMessage)  
33. [上报二维码付款消息(reportQrCodeWcPay)](#reportQrCodeWcPay)  
34. [上报收藏列表(reportFavitems)](#reportFavitems)  
35. [上报系统消息(reportSystemMessage)](#reportSystemMessage)  
36. [上报其他消息(reportOtherMessage)](#reportOtherMessage)  
37. [上报其他接收应用未知消息(reportOtherAppMessage)](#reportOtherAppMessage)  
### 请求相关
38. [上报新的加好友请求(reportFriendAddRequest)](#reportFriendAddRequest)  
39. [上报加好友指令返回状态(reportAddFriendMessage)](#reportAddFriendMessage)  
40. [上报通过手机号/微信号/QQ号查询任意微信号信息(reportSearchContact)](#reportSearchContact)  
### 其他
41. [上报数据库查询结果(reportSqlData)](#reportSqlData)  
42. [上报扫描二维码结果(reportScanQrcodePic)](#reportScanQrcodePic)  
43. [上报当前聊天对象改变(reportTalkerChange)](#reportTalkerChange)  
44. [上报语音翻译结果(reportTransVoice)](#reportTransVoice)  
45. [上报URL访问状态(reportCheckUrlStatus)](#reportCheckUrlStatus)  
46. [上报上传客户端文件到服务端结果(resUploadFile)](#resUploadFile)  

# send_msg
二. 执行回调接口下发的指令: 这些指令包括:
### 登录登出
01. [打开微信(openWeChat)](#openWeChat)  
02. [获取二维码(getLoginQrCode)](#getLoginQrCode)  
03. [获取当前登录微信详细信息(getLoginUser)](#getLoginUser)  
04. [退出微信(logout)](#logout)  
### 好友相关
05. [获取普通好友列表(getContacts)](#getContacts)  
06. [获取企业好友列表(getImContacts)](#getImContacts)  
07. [获取公众号列表(getPublics)](#getPublics)  
08. [获取单个普通好友信息(getSingleContact)](#getSingleContact)  
09. [任意普通微信反查详细信息(updateContact)](#updateContact)  
10. [添加好友(addFriend)](#addFriend)  
11. [删除好友/取消关注公众号(delFriend)](#delFriend)  
12. [修改好友备注(updateRemark)](#updateRemark)  
13. [接收加好友请求(acceptFriend)](#acceptFriend)  
14. [接收好友转账(acceptBankTransfer)](#acceptBankTransfer)  
15. [退还好友转账(refuseFriendWcpay)](#refuseFriendWcpay)  
16. [自动同意加好友申请(autoAcceptFriend)](#autoAcceptFriend)  
17. [自动同意好友转帐(autoAcceptWcpay)](#autoAcceptWcpay)  
18. [自动加名片(autoAcceptCard)](#autoAcceptCard)  
19. [单向加好友(acceptOnewayFriend)](#acceptOnewayFriend)  
20. [通过手机号/微信号/QQ号查询任意微信号信息(searchContact)](#searchContact)  
21. [添加通过任意手机号/微信号/QQ号查询的联系人(addSearchContact)](#addSearchContact)  
### 群相关
22. [获取普通群列表(getChatRooms)](#getChatRooms)  
23. [获取企业群列表(getImRooms)](#getImRooms)  
24. [获取单个普通群成员信息(getSingleChatRoomMembers)](#getSingleChatRoomMembers)  
25. [获取单个企业群成员信息(getSingleImRoomMembers)](#getSingleImRoomMembers)  
26. [网络更新普通群成员信息(updateChatRoom)](#updateChatRoom)  
27. [发送40人以下群邀请(sendChatroomLow)](#sendChatroomLow)  
28. [发送40人以上群邀请(sendChatroomHigh)](#sendChatroomHigh)  
29. [接受群邀请(acceptChatroomInvite)](#acceptChatroomInvite)  
30. [踢群成员(delChatRoomMembers)](#delChatRoomMembers)  
31. [修改群名称(updateChatRoomName)](#updateChatRoomName)  
32. [修改群公告(sendChatRoomNotice)](#sendChatRoomNotice)  
33. [修改我在本群的昵称(updateChatRoomDisplayName)](#updateChatRoomDisplayName)  
34. [是否显示群昵称(showDisplayName)](#showDisplayName)  
35. [创建群聊(createChatRoom)](#createChatRoom)  
36. [退出并删除群(quitDelChatRoom)](#quitDelChatRoom)  
37. [自动接受群邀请(autoAcceptChatRoom)](#autoAcceptChatRoom)  
38. [通过二维码进群(acceptQrcodeChatRoom)](#acceptQrcodeChatRoom)  
39. [保存到/移出通讯录(saveRoomToContact)](#saveRoomToContact)  
### 消息相关
40. [任意消息转发(transAnyMessage)](#transAnyMessage)  
41. [发送文本消息(sendTextMessage)](#sendTextMessage)  
42. [发送群内@文本消息(sendAtTextMessage)](#sendAtTextMessage)  
43. [发送图片(sendPicMessage)](#sendPicMessage)  
44. [发送文件(sendFileMessage)](#sendFileMessage)  
45. [发送视频(sendVideoMessage)](#sendVideoMessage)  
46. [发送GIF表情(sendGifMessage)](#sendGifMessage)  
47. [发送链接消息(sendLinkMessage)](#sendLinkMessage)  
48. [发送名片(sendCardMessage)](#sendCardMessage)  
49. [发送小程序(sendMiniMessage)](#sendMiniMessage)  
50. [发送收藏(sendFavorite)](#sendFavorite)  
51. [发送xml消息(sendXmlMessage)](#sendXmlMessage)  
52. [发送名片xml消息(sendCardXmlMessage)](#sendCardXmlMessage)  
### 请求相关
53. [关注公众号(addPublic)](#addPublic)  
54. [获取收藏列表(getFavorites)](#getFavorites)  
55. [收藏指定消息(addFavoriteFrom)](#addFavoriteFrom)  
56. [语音翻译(transVoice)](#transVoice)  
57. [无痕清粉(zombieCheck)](#zombieCheck)  
58. [解密图片(decryptPic)](#decryptPic)  
59. [获取未读消息数量(unreadMsgCountChange)](#unreadMsgCountChange)  
60. [清理微信聊天记录(clearChatHistory)](#clearChatHistory)  
### 其他
61. [识别二维码(scanQrcodePic)](#scanQrcodePic)  
62. [开启/关闭消息免打扰(modRecvNotify)](#modRecvNotify)  
63. [置顶/取消置顶聊天(chatSessionTop)](#chatSessionTop)  
64. [打开内置浏览器(openBrowser)](#openBrowser)  
65. [开启/关闭防撤回功能(disableRevoke)](#disableRevoke)  
66. [检测URL在微信中是否有效(checkUrlStatus)](#checkUrlStatus)  
67. [查询微信数据库(getSqlData)](#getSqlData)  
68. [关闭进程(closeProcess)](#closeProcess)  
69. [把客户端所在PC的资料上传到指定服务器(uploadFile)](#uploadFile)  
70. [下载资料到客户端所在PC(downloadFile)](#downloadFile)  

# receive_msg
## 参数说明
|数据格式中的参数|参数的含义|
|:--------------|:-------|
|action         |上报的名称|
|cwxid          |当前登录微信账号的微信 ID|
|data           |上报的数据|

## 数据格式
```json
{
    "action" : "",
    "cwxid" : "",
    "data" : {}
}
```

### send_msg 任务下发到DLL的响应
```json
{
    "action":"",
    "cwxid":"",
    "data":{"errorReason":"","sendId":"","sendResult":""},
}
```

### 01. <span id="reportQrCodeMessage">上报登陆二维码(reportQrCodeMessage)</span>
#### 参数说明
|data中的参数|参数说明|
|:-----------|:-------|
|file        |二维码图片的保存地址|
|base64      |二维码图片的 base64 格式|

```json
{
    "data":{
        "action":"reportQrCodeMessage",
        "cwxid":"null",
        "data":{
            "file":"",
            "base64":""
        }
    }
}
```

### 02. <span id="reportLoginUser">上报当前登录微信详细信息(reportLoginUser)</span>
#### 参数说明
|data中的参数|参数说明|
|:-----------|:-------|
|wxid        |微信id|
|nick        |微信昵称|
|headPic     |头像的url地址|
|phone       |手机号|
|unreadmsg   |未读消息数量|
|wxdir       |该账号微信缓存文件夹|

```json
{
    "data":{
        "action":"reportLoginUser",
        "cwxid":"xxxxxx",
        "data":{
            "wxid":  "wxid",
            "nick": "xxxxx",
            "headPic":"xxxxx",
            "phone" :"xxxx",
            "unreadmsg":"http://xxxxxxxx",
            "wxdir" : 0
        }
    }
}
```

### 03. <span id="reportLogout">上报退出登录事件(reportLogout)</span>

```json
{
    "data":{
        "action":"reportLogout",
        "cwxid":"xxxxxx",
        "data":{}
    }
}
```

### 04. <span id="reportContacts">上报普通好友列表(reportContacts)</span>
#### 参数说明
|data中的参数|参数说明|
|:-----------|:-------|
|wxid        |微信id|
|alias       |微信号(有可能为空)|
|nick        |微信昵称|
|remark      |好友备注|
|headPic     |头像的url地址|
|sex         |性别:1男，2女,0(未知)|
|country     |祖国(可能为空)|
|province    |省份(可能为空)|
|city        |城市(可能为空)|

```json
{
    "data":{
        "action":"reportContacts",
        "cwxid":"xxxxxx",
        "data":{
            "friendList":[
                {
                    "wxid":  "wxid_xxxx",
                    "alias": "xxxxx",
                    "nick":"xxxxx",
                    "remark" :"xxxx",
                    "headPic":"http://xxxxxxxx",
                    "sex" : 1,
                    "country":"xxx",
                    "province":"xxxx",
                    "city":"xxxxx"
                }
            ]
        }
    }
}
```

### 05. <span id="reportImContacts">上报企业好友列表(reportImContacts)</span>
#### 参数说明
|data中的参数|参数说明|
|:-----------|:-------|
|wxid        |微信id|
|nick        |微信昵称|
|remark      |好友备注|
|headPic     |头像的url地址|

```json
{
    "data":{
        "action":"reportImContacts",
        "cwxid":"xxxxxx",
        "data":{
            "friendList":[
                {
                    "wxid":  "wxid_xxxx",
                    "nick":"xxxxx",
                    "remark" :"xxxx",
                    "headPic":"http://xxxxxxxx"
                }
            ]
        }
    }
}
```

### 06. <span id="reportPublics">上报公众号列表(reportPublics)</span>
#### 参数说明
|data中的参数|参数说明|
|:-----------|:-------|
|wxid        |某些公众号也可能以wxid_ 开头|
|nick        |公众号名称|
|headPic     |公众号头像的url地址|

```json
{
    "data":{
        "action" : "reportPublics",
        "cwxid" : "xxxxxx",
        "data" : {
            "publicList": [
                {
                    "wxid":  "wxid",
                    "nick":"xxxxx",
                    "headPic":"http://xxxxxxxx"
                }
            ]
        }
    }
}
```

### 07. <span id="reportSingleContact">上报单个普通好友信息(reportSingleContact)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信id|
|alias       |微信号(有可能为空)|
|nick        |微信昵称|
|remark      |好友备注|
|headPic     |头像的url地址|
|sex         |性别:1男，2女,0(未知)|
|country     |祖国(可能为空)|
|province    |省份(可能为空)|
|city        |城市(可能为空)|

```json
{
    "data":{
        "action":"reportSingleContact",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid":  "wxid_xxxx",
            "alias": "xxxxx",
            "nick":"xxxxx",
            "remark" :"xxxx",
            "headPic":"http://xxxxxxxx",
            "sex" : 1,
            "country":"xxx",
            "province":"xxxx",
            "city":"xxxxx"
        }
    }
}
```

### 08. <span id="reportUpdateContact">上报任意普通微信反查详细信息(reportUpdateContact)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信id|
|alias       |微信号(有可能为空)|
|nick        |微信昵称|
|remark      |好友备注|
|headPic     |高清头像的url地址|
|smallPic    |小头像的url地址|
|sex         |性别:1男，2女,0(未知)|
|country     |祖国(可能为空)|
|province    |省份(可能为空)|
|city        |城市(可能为空)|
|signature   |朋友圈个性签名|
|snspic      |朋友圈背景图片|
|scene       |来源类型|
|status      |是否成功 1成功,0失败|
|v1          |用户v1|
|v2          |用户v2|

|scene的值|参数的含义|
|:--------------|:---------|
|6              |好友验证, 加之前加过的人|
|14             |添加群好友|
|15             |通过查询添加|
|17             |通过名片添加，需要传v1值|

```json
{
    "data":{
        "action":"reportUpdateContact",
        "cwxid" : "xxxxx",
        "data" : { 
            "wxid": "xxx",  
            "alias": "",  
            "nick": "xxxx",  
            "remark": "",  
            "headPic": "http://wx.qlogo.cn/xxxxxxx",  
            "smallPic": "http://wx.qlogo.cn/xxxxxx",  
            "sex": 1,
            "country": "",   
            "province": "",    
            "city": "",       
            "signature": "",    
            "snspic": "http://szmmsns.qpic.cn/xxxxxx",   
            "scene": 6,     
            "status": 1,       
            "v1": "",               
            "v2": ""  
        }
    }
}
```

### 09. <span id="reportContactAdd">上报联系人新增通知(reportContactAdd)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信id|
|alias       |微信号(有可能为空)|
|nick        |微信昵称|
|remark      |好友备注|
|headPic     |头像的url地址|
|sex         |性别:1男，2女,0(未知)|
|country     |祖国(可能为空)|
|province    |省份(可能为空)|
|city        |城市(可能为空)|

```json
{
    "data":{
        "action":"reportContactAdd",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid": "xxx",  
            "alias": "",  
            "nick": "xxxx",  
            "remark": "",  
            "headPic": "http://wx.qlogo.cn/xxxxxxx",  
            "sex": 1,
            "country": "",   
            "province": "",    
            "city": ""
        }
    }
}
```

### 10. <span id="reportContactDel">上报联系人删除通知(reportContactDel)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信id|

```json
{
    "data":{
        "action":"reportContactDel",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid":"xxxx",
        }
    }
}
```

### 11. <span id="reportChatRooms">上报普通群列表(reportChatRooms)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:-------|
|wxid        |群的微信ID|
|nick        |群昵称|
|isowner     |是否为群主|
|owner       |群主的wxid|
|headPic     |群头像|
|roomCount   |群成员数量|
|userLists   |当前群的成员wxid的列表|

```json
{
    "data":{
        "action":"reportChatRooms",
        "cwxid" : "xxxxx",
        "data" : {
            "groupList":[
                {
                    "wxid":  "xxxxx@chatroom",
                    "nick":"xxxxx",
                    "isowner": 0,
                    "owner": "xxxx",
                    "headPic":"http://xxxxxxxx",
                    "roomCount" :"5",
                    "userLists":["xxx","xxx"]
                }
            ] 
        }
    }
}
```

### 12. <span id="reportImRooms">上报企业群列表(reportImRooms)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |群的微信 ID|
|owner       |群主 ID|
|nick        |群昵称|
|headPic     |群头像|
|roomCount   |群成员数量|

|userLists中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信 ID|
|username    |微信号(有可能为空)|
|nick        |昵称|
|headPic     |头像|
|sex         |性别:1男，2女,0未知 |
|country     |祖国(可能为空) |
|province    |省份(可能为空) |
|city        |城市(可能为空) |

```json
{
    "data":{
        "action":"reportImRooms",
        "cwxid" : "xxxxx",
        "data" : {
            "groupList":[
                {
                    "wxid":  "xxxxx@chatroom",
                    "nick":"xxxxx",
                    "isowner": 0,
                    "owner": "xxxx",
                    "headPic":"http://xxxxxxxx",
                    "roomCount" :"5",
                    "userLists":["xxx","xxx"]
                }
            ] 
        }
    }
}
```

### 13. <span id="reportSingleChatRoomMembers">上报单个普通群成员信息(reportSingleChatRoomMembers)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |群的微信 ID|
|roomCount   |群成员数量|

|userLists中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信ID|
|alias       |微信号(有可能为空)|
|nick        |昵称|
|displayname |群昵称|
|remark      |好友备注|
|headPic     |头像|
|sex         |性别:1男，2女,0未知 |
|country     |祖国(可能为空) |
|province    |省份(可能为空) |
|city        |城市(可能为空) |
```json
{
    "data":{
        "action":"reportSingleChatRoomMembers",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid":"xxx@chatroom",
            "roomCount":"",
            "userLists":[
               {
                    "wxid":"",
                    "alias":"",
                    "nick":"",
                    "displayname":"",
                    "remark":"",
                    "headPic":"",
                    "sex":"2",
                    "country":"xxx",
                    "province":"xxx",
                    "city":"xxx"
               }
           ]
        }
    }
}
```

### 14. <span id="reportSingleImRoomMembers">上报单个企业群成员信息(reportSingleImRoomMembers)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |群微信ID|
|owner       |群主 ID|
|nick        |群名|
|headPic     |群头像|
|roomCount   |群成员数量|

|userLists中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信 ID|
|nick        |昵称|
|headPic     |头像|
|remark      |备注|

```json
{
    "data":{
        "action":"reportSingleImRoomMembers",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid":"xxx@chatroom",
            "owner":"xxxxx",
            "nick":"",
            "headPic":"",
            "roomCount":"",
            "userLists":[
               {
                    "wxid":"",
                    "nick":"",
                    "headPic":"",
                    "sex":"2",
                    "country":"xxx",
                    "province":"xxx",
                    "city":"xxx"
               }
           ]
        }
    }
}
```

### 15. <span id="reportAcceptQrCodeChatRoom">上报通过二维码进群返回状态(reportAcceptQrCodeChatRoom)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|url         |二维码图片链接|
|status      |执行状态，0成功， 1该群已开启进群验证， 2二维码已过期|

```json
{
    "data":{
        "action":"reportAcceptQrCodeChatRoom",
        "cwxid" : "xxxxx",
        "data" : {
            "url": "http:///xxxxx",
            "status":"0"
        }
    }
}
```

### 16. <span id="reportChatRoomMemberAdd">上报群成员新增通知(reportChatRoomMemberAdd)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |群微信 ID|
|nick        |群昵称|
|isowner     |是否为群主|
|owner       |群主 ID|
|headPic     |群头像|
|roomCount   |群成员数量|

|userLists中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信 ID|
|nick        |昵称|
|inviteBy    |邀请人微信ID|

```json
{
    "data":{
        "action":"reportChatRoomMemberAdd",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid":"xxx@chatroom",
            "nick":"",
            "headPic":"",
            "isowner": "",
            "owner":"xxxxx",
            "roomCount":"",
            "userLists":[
               {
                    "wxid":"",
                    "nick":"",
                    "inviteBy":""
               }
           ]
        }
    }
}
```

### 17. <span id="reportChatRoomMemberDel">上报群成员删除通知(reportChatRoomMemberDel)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |群的微信 ID|
|nick        |群昵称|
|headPic     |群头像|
|isowner     |是否为群主|
|owner       |群主 ID|
|roomCount   |群成员数量|

|userLists中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信 ID|
|nick        |昵称|

```json
{
    "data":{
        "action":"reportChatRoomMemberDel",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid":"xxx@chatroom",
            "nick":"",
            "headPic":"",
            "isowner":"xxxxx",
            "owner":"xxxxx",
            "roomCount":"",
            "userLists":[
               {
                    "wxid":"",
                    "nick":""
               }
           ]
        }
    }
}
```

### 18. <span id="reportNewChatRoom">上报检测到的新群通知(reportNewChatRoom)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|wxid        |群的微信 ID|
|nick        |群昵称|
|headPic     |群头像|
|isowner     |是否为群主|
|owner       |群主 ID|
|roomCount   |群成员数量|

|userLists中的参数|参数的含义|
|:-----------|:---------|
|wxid        |微信ID|
|nick        |昵称|

```json
{
    "data":{
        "action":"reportNewChatRoom",
        "cwxid" : "xxxxx",
        "data" : {
            "wxid":"xxx@chatroom",
            "nick":"",
            "headPic":"",
            "isowner":"xxxxx",
            "owner":"xxxxx",
            "roomCount":"",
            "userLists":[
               {
                    "wxid":"",
                    "nick":""
               }
           ]
        }
    }
}
```

### 19. <span id="reportChatRoomQuit">上报退群或被踢通知(reportChatRoomQuit)</span>
#### 参数说明
|data中的参数|参数的含义|
|:-----------|:---------|
|roomWxid        |群的微信ID|

```json
{
    "data":{
        "action":"reportChatRoomQuit",
        "cwxid" : "xxxxx",
        "data" : {
            "roomWxid":"xxx@chatroom",
        }
    }
}
```

### 20. <span id="reportTextMessage">上报文本消息(reportTextMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|message    |消息内容，纯文本格式|
|atlist     |群内发送消息@用户列表|
|timestamp  |消息时间戳|

```json
{
    "data":{
        "action":"reportTextMessage",
        "cwxid":"",
        "data":{
            "msgType": 1,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "2970283551233214898",
            "roomWxid":"xxx@chatroom",
            "wxidFrom"  : "wxid_sadkwqlXXX",
            "wxidTo" :"wxid_sadkwqlkq",
            "message" : "XXXX",
            "atlist" : ["wxid_1fd41f9u22", "wxid_1fd41f9"],
            "timestamp":1597736976
        }
    }
}
```

### 21. <span id="reportPicMessage">上报图片消息(reportPicMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|image      |图片本地路径|
|imagethumb |缩略图本地路径|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的xml信息|

```json
{
    "data":{
        "action":"reportPicMessage",
        "cwxid":"xxxxx",
        "data":{
            "msgType": 3,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid": "xxxxxxxx@chatroom",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "image" : "XXXX",
            "imagethumb" : "XXXX",
            "timestamp" : "XXXX",
            "xmlmsg" : ""
        }
    }
}
```

### 22. <span id="reportFileMessage">上报文件消息(reportFileMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|fileIndex  |文件下载后的本地路径|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportFileMessage",
        "cwxid":"xxxxx",
        "data":{
            "msgType": "4906",
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid": "xxxxxxxx@chatroom",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "fileIndex":"",
            "timestamp" : "XXXX",
            "xmlmsg": "xxxxxxx"
        }
    }
}
```

### 23. <span id="reportVideoMessage">上报视频消息(reportVideoMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|coverIndex |视频文件封面图片的本地路径|
|videoIndex |视频文件下载后的本地路径|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportVideoMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "msgType": 43,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid": "xxxxxxxx@chatroom",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "coverIndex":"",
            "videoIndex":"",
            "timestamp":"",
            "xmlmsg": "xxxxxxx"
        }
    }
}
```

### 24. <span id="reportVoiceMessage">上报语音消息(reportVoiceMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|voiceIndex |语音文件下载后的本地路径|
|mp3Index   |语音转换后的本地路径|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportVoiceMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "msgType": 34,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid": "xxxxxxxx@chatroom",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "voiceIndex" : "XXXX",
            "mp3Index" : "XXXX",
            "timestamp":"",
            "xmlmsg": "xxxxxxx"
        }
    }
}
```

### 25. <span id="reportGifMessage">上报GIF表情消息(reportGifMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportGifMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "msg_type":47,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid": "xxxxxxxx@chatroom",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo": "xxxxxxxxx",
            "xmlmsg": "xxxxxxx",
            "timestamp" : ""
        }
    }
}
```

### 26. <span id="reportCardMessage">上报个人名片消息(reportCardMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportCardMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "msgType": 42,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid" : "",
            "wxidFrom"  : "",
            "wxidTo" :"wxid_sadkwqlkq",
            "xmlmsg": "xxxxxxx",
            "timestamp" : ""
        }
    }
}
```

### 27. <span id="reportLocationMessage">上报位置消息(reportLocationMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportCardMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "msgType": 48,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid" : "",
            "wxidFrom"  : "",
            "wxidTo" :"wxid_sadkwqlkq",
            "xmlmsg": "xxxxxxx",
            "timestamp" : ""
        }
    }
}
```

### 28. <span id="reportLinkMessage">上报链接消息(网页或群邀请)(reportLinkMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportLinkMessage",
        "cwxid":"xxxxx",
        "data":{
            "msgType": 4905,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid" : "",
            "wxidFrom"  : "",
            "wxidTo" :"wxid_sadkwqlkq",
            "xmlmsg": "xxxxxxx",
            "timestamp" : ""
        }
    }
}
```

### 29. <span id="reportMiniMessage">上报小程序消息(reportMiniMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

```json
{
    "data":{
        "action":"reportMiniMessage",
        "cwxid":"xxxxx",
        "data":{
            "msgType": 4933,
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "roomWxid" : "",
            "wxidFrom"  : "",
            "wxidTo" :"wxid_sadkwqlkq",
            "xmlmsg": "xxxxxxx",
            "timestamp" : ""
        }
    }
}
```

### 30. <span id="reportTransferMessage">上报转账消息(reportTransferMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|wxidFrom   |消息发送者的wxid 如果是自己发的消息这里的wxid就是自己的微信号|
|wxidTo     |消息的接收者的wxid 如果发往群的消息,这个值就是群的wxid  如果是别人私聊给自己的消息,这里就是自己的微信号|
|timestamp  |消息时间戳|
|xmlmsg     |微信原始的 xml 信息|

|xml中的参数| 参数的含义|
|:----------|:---------|
|paysubtype |这笔账单的状态，1:发起转账(包括我转账给他人，他人转账给我)；3:确认收账(包括我确认收账，他人确认收账);4:退还转账(包括我退还转账，他人退还转账给我)|
|paymemo    |这笔账单的备注|
|feedesc    |这笔账单的金额|
|transferid |转账的ID|

```json
{
    "data":{
        "action":"reportTransferMessage",
        "cwxid":"xxxxx",
        "data":{
            "msgType": "4920",
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "12314324243",
            "wxidFrom"  : "",
            "wxidTo" :"wxid_sadkwqlkq",
            "xmlmsg": "xxxxxxx",
            "timestamp" : ""
        }
    }
}
```

### 31. <span id="reportZombieCheckMessage">上报无痕清理僵尸粉消息(reportZombieCheckMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|wxid       |被检测得微信ID|
|status     |检测状态|

|status状态参数|参数的含义|
|:----------|:---------|
|0          |非僵尸粉|
|1          |僵尸粉(对方把我拉黑了)|
|2          |僵尸粉(对方把我删除了)|
|3          |僵尸粉(未知原因,对方微信号被腾讯注销等)|

```json
{
    "data":{
        "action":"reportTransferMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "wxid":  "wxid_xxxxx",
            "status" : "0"
        }
    }
}
```

### 32. <span id="reportDecryptPicMessage">上报解密图片消息(reportDecryptPicMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|srcfile    |待解密文件dat格式|
|tarfile    |解密后的jpg图片|
|status     |1为解密成功，0为失败|

```json
{
    "data":{
        "action":"reportDecryptPicMessage",
        "cwxid":"xxxxx",
        "data":{
            "srcfile": "c:\\test.dat",
            "tarfile" : "c:\\out.jpg",
            "status": "1"
        }
    }
}
```

### 33. <span id="reportQrCodeWcPay">上报二维码付款消息(reportQrCodeWcPay)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|wxid       |付款者的微信ID|
|nick       |付款者的昵称|
|fee        |支付金额 ( 单位分)|
|feetype    |支付类型|
|orderno    |订单号|
|timestamp  |消息时间戳|

```json
{
    "data":{
        "action":"reportQrCodeWcPay",
        "cwxid":"xxxxx",
        "data":{
            "wxid" : "xxxxx",
            "nick" : "XXXX",
            "fee": "",
            "feetype": "",
            "orderno": "",
            "timestamp": ""
        }
    }
}
```

### 34. <span id="reportFavitems">上报收藏列表(reportFavitems)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|items      |收藏列表|
|status     |获取状态|

```json
{
    "data":{
        "action":"reportFavitems",
        "cwxid":"xxxxx",
        "data":{
            "items": [{
                "fromUser" : "",
                "localId": "",
                "roomMember":  "",
                "title" : "",
                "type": "",
                "updateTime": "",
                "xml": ""
            }],
            "status": 1
        }
    }
}
```

### 35. <span id="reportSystemMessage">上报系统消息(reportSystemMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid|
|wxidTo     |消息的接收者的wxid|
|message    |系统消息|
|timestamp  |消息时间戳|

```json
{
    "data":{
        "action":"reportSystemMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "msgType": "10000",
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "1231413213123",
            "roomWxid": "",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "message": "",
            "timestamp": "12312313123"
        }
    }
}
```

> 相关系统消息示例:  
    1.有红包出没时:"发出红包，请在手机上查看"  
    2.发消息-被对方拉黑之后,message 为"消息已发出，但被对方拒收了"  
    3.修改群名称后:xxxxx修改群名为xxxxxxx  
    4.群主已恢复默认进群方式。  
    5.群主已启用"群聊邀请确认"，群成员需群主确认才能邀请朋友进群。  
    6.你已成为新群主  
    7.xxxxxx已成为新群主  
    8.你邀请xxxx加入了群聊  
    9.xxxx邀请xxxx加入了群聊  
    10.xxxxx通过扫描你分享的二维码加入群聊  
    11.xxxxx通过扫描xxxxxx分享的二维码加入群聊  

### 36. <span id="reportOtherMessage">上报其他消息(reportOtherMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid|
|wxidTo     |消息的接收者的wxid|
|message    |系统消息|
|timestamp  |消息时间戳|

```json
{
    "data":{
        "action":"reportOtherMessage",
        "cwxid":"xxxxx",
        "data":{
            "msgType": "x",
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "1231413213123",
            "roomWxid": "",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "message": "",
            "timestamp": "12312313123"
        }
    }
}
```

### 37. <span id="reportOtherAppMessage">上报其他接收应用未知消息(reportOtherAppMessage)</span>
#### 参数说明
|data中的参数| 参数的含义|
|:----------|:---------|
|msgType    |消息类型标记|
|myMsg      |是否是本人发出的消息，1为是，0为不是|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid|
|wxidTo     |消息的接收者的wxid|
|message    |系统消息|
|timestamp  |消息时间戳|

```json
{
    "data":{
        "action":"reportTransferMessage",
        "cwxid":"wxid_qg0saisth0r222",
        "data":{
            "msgType": "49x",
            "myMsg" : "0",
            "ispc" : "0",
            "msgid" : "1231413213123",
            "roomWxid": "",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "message": "",
            "timestamp": "12312313123"
        }
    }
}
```

### 38. <span id="reportFriendAddRequest">上报新的加好友请求(reportFriendAddRequest)</span>
#### 个别参数说明，未给出的则参考其他接口的说明
|data中的参数|参数的含义|
|:----------|:--------|
|msgType    |消息类型标记|
|ispc       |是否由PC端发出，1为是，0为不是|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid|
|wxidTo     |消息的接收者的wxid|
|xmlmsg     |加好友请求xml数据|
|timestamp  |消息时间戳|

> 相关说明:  
    xmlmsg包含v1,v2信息，使用v1,v2可以直接调用同意好友请求接口来同意添加好友  

```json
{
    "data":{
        "action":"reportFriendAddRequest",
        "cwxid":"xxxxx",
        "data" : {
            "msgType": 37,
            "ispc" : "0",
            "msgid" : "1231413213123",
            "roomWxid": "",
            "wxidFrom": "wxid_xxxxxx",
            "wxidTo":  "wxid_xxxxx",
            "xmlmsg": "",
            "timestamp": "12312313123"
        }
    }
}
```

### 39. <span id="reportAddFriendMessage">上报加好友指令返回状态(reportAddFriendMessage)</span>
#### 个别参数说明，未给出的则参考其他接口的说明
|data中的参数|参数的含义|
|:----------|:--------|
|wxid       |添加的微信ID|
|status     |状态|

|status状态参数|参数的含义|
|:----------|:--------|
|0          |成功|
|1          |失败，由于对方的隐私设置|
|2          |失败, 操作频繁|
|3          |失败, 获取V2数据失败|
|-x         |失败, 未知错误码|

```json
{
    "data":{
        "action":"reportAddFriendMessage",
        "cwxid":"xxxxx",
        "data" : {
            "wxid":"",
            "status":0
        }
    }
}
```

### 40. <span id="reportSearchContact">上报通过手机号/微信号/QQ号查询任意微信号信息(reportSearchContact)</span>
#### 参数说明
|data中的参数|参数的含义|
|:----------|:--------|
|wxid        |查询到的微信ID|
|alias       |微信号(有可能为空)|
|nick        |微信昵称|
|headPic     |高清头像的url地址|
|smallPic    |小头像的url地址|
|sex         |性别:1男，2女,0(未知)|
|country     |祖国(可能为空)|
|province    |省份(可能为空)|
|city        |城市(可能为空)|
|search      |查询内容|
|signature   |朋友圈个性签名|
|status      |是否成功 1成功,0失败|
|isFriend    |是否好友|
|v1          |用户v1|
|v2          |用户v2|

```json
{
    "data":{
        "action":"reportSearchContact",
        "cwxid":"xxxxx",
        "data" : {
            "wxid":"",
            "alias":"",
            "nick":"",
            "headPic":"",
            "smallPic":"",
            "sex":"2",
            "country":"xxx",
            "province":"xxx",
            "city":"xxx",
            "search":"xxx",
            "signature":"xxx",
            "status":"xxx",
            "isFriend":"xxx",
            "v1":"xxxxxx",
            "v2":"xxxxxxx"
        }
    }
}
```

### 41. <span id="reportSqlData">上报数据库查询结果(reportSqlData)</span>
#### 参数说明
|data中的参数|参数的含义|
|:----------|:--------|
|result     |查询结果|
|extend     |指令附加标记，可空|

```json
{
    "data":{
        "action":"reportSqlData",
        "cwxid":"xxxxx",
        "data" : {
            "result":"",
            "extend":"search_test"
        }
    }
}
```

### 42. <span id="reportScanQrcodePic">上报扫描二维码结果(reportScanQrcodePic)</span>
#### 参数说明
|data中的参数|参数的含义|
|:----------|:--------|
|pic        |二维码图片地址|
|content    |二维码内容|
|type       |二维码类型  |
|status     |扫描结果状态，1成功，0失败|

```json
{
    "data":{
        "action":"reportScanQrcodePic",
        "cwxid":"xxxxx",
        "data" : {
            "pic":"",
            "content":"",
            "type":"",
            "status":""
        }
    }
}
```

### 43. <span id="reportTalkerChange">上报当前聊天对象改变(reportTalkerChange)</span>
#### 参数说明
|data中的参数|参数的含义|
|:----------|:--------|
|user       |当前对象|
|type       |当前对象类型，1为好友，2为群，3为公众号|
|status     |状态  |

|user中的参数|参数的含义|
|:----------|:--------|
|wxid       |当前对象微信ID|
|nick       |当前对象昵称|
|headPic    |当前对象头像|
|isowner    |是否为群主|
|owner      |群主微信ID|
|roomcount  |群成员个数|

```json
{
    "data":{
        "action":"reportTalkerChange",
        "cwxid":"xxxxx",
        "data" : {
            "user": {
                "wxid":"",
                "nick":"",
                "headPic":"",
                "isowner":"",
                "owner":"",
                "roomcount":""
            },
            "type":"",
            "status":""
        }
    }
}
```

### 44. <span id="reportTransVoice">上报语音翻译结果(reportTransVoice)</span>
#### 参数说明
|data中的参数|参数的含义|
|:----------|:--------|
|msgType    |消息类型标记|
|msgid      |消息ID，可用于转发|
|roomWxid   |聊天消息发生在哪个群(如果是私聊则为空)|
|wxidFrom   |消息发送者的wxid|
|wxidTo     |消息的接收者的wxid|
|text       |翻译后的文本|
|status     |状态|

```json
{
    "data":{
        "action":"reportTransVoice",
        "cwxid":"xxxxx",
        "data" : {
            "msgType": "",
            "msgId": "",
            "roomWxid": "",
            "wxidFrom": "",
            "wxidTo": "",
            "text": "",
            "status": ""
        }
    }
}
```

### 45. <span id="reportCheckUrlStatus">上报URL访问状态(reportCheckUrlStatus)</span>
#### 参数说明
|data中的参数|参数的含义|
|:----------|:--------|
|url        |待测试url|
|realUrl    |真实url|
|status     |访问状态，0可以访问，负值不能访问|

```json
{
    "data":{
        "action":"reportCheckUrlStatus",
        "cwxid":"xxxxx",
        "data" : {
            "url": "",
            "realUrl": "",
            "status": ""
        }
    }
}
```

### 46. <span id="resUploadFile">上报上传客户端文件到服务端结果(resUploadFile)</span>
#### 参数说明
|data中的参数|参数的含义|
|:----------|:--------|
|sendResult |服务端接收文件的返回值|

```json
{
    "data":{
        "action":"resUploadFile",
        "cwxid":"xxxxx",
        "data" : {
                    "errorReason": "",
                    "sendId": "8859663",
                    "sendResult": ""
        }
    }
}
```

# send_msg
## 数据格式
```json
{
    "api" : "",
    "sendId":"",
    "option" : {}
}
```

### 01. <span id="openWeChat">打开微信(openWeChat)</span>
```json
{
    "api" : "openWeChat",
    "sendId":"",
    "option" : {}
}
```

### 02. <span id="getLoginQrCode">获取二维码(getLoginQrCode)</span>
```json
{
    "api" : "getLoginQrCode",
    "sendId":"",
    "option" : {}
}
```

### 03. <span id="getLoginUser">获取当前登录微信详细信息(getLoginUser)</span>
```json
{
    "api" : "getLoginUser",
    "sendId":"",
    "option" : {}
}
```

### 04. <span id="logout">退出微信(logout)</span>
```json
{
    "api" : "logout",
    "sendId":"",
    "option" : {}
}
```

### 05. <span id="getContacts">获取普通好友列表(getContacts)</span>
```json
{
    "api" : "getContacts",
    "sendId":"",
    "option" : {}
}
```

### 06. <span id="getImContacts">获取企业好友列表(getImContacts)</span>
```json
{
    "api" : "getImContacts",
    "sendId":"",
    "option" : {}
}
```

### 07. <span id="getPublics">获取公众号列表(getPublics)</span>
```json
{
    "api" : "getPublics",
    "sendId":"",
    "option" : {}
}
```

### 08. <span id="getSingleContact">获取单个普通好友信息(getSingleContact)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |微信id|

```json
{
    "api" : "getSingleContact",
    "sendId":"",
    "option" : {
        "wxid":"xxxxx"
    }
}
```

### 09. <span id="updateContact">任意普通微信反查详细信息(updateContact)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |微信id|

```json
{
    "api" : "updateContact",
    "sendId":"",
    "option" : {
        "wxid":"xxxxx"
    }
}
```

### 10. <span id="addFriend">添加好友(addFriend)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要添加的微信id|
|remark       |打招呼消息|
|scene        |来源类型|
|roomWxid     |来自哪个群，可空|

|scene的值|参数的含义|
|:--------------|:---------|
|6              |好友验证, 加之前加过的人|
|14             |添加群好友|
|15             |通过查询添加|
|17             |通过名片添加，需要传v1值|

```json
{
    "api" : "addFriend",
    "sendId":"",
    "option" : {
        "wxid": "", 
        "remark": "",
        "scene": "",
        "roomWxid": ""
    }
}
```

### 11. <span id="delFriend">删除好友/取消关注公众号(delFriend)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |微信id|

```json
{
    "api" : "delFriend",
    "sendId":"",
    "option" : {
        "wxid":"xxxxx"
    }
}
```

### 12. <span id="updateRemark">修改好友备注(updateRemark)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid      |需要修改备注的好友的微信id|
|remark    |好友备注|

```json
{
    "api" : "updateRemark",
    "sendId":"",
    "option" : {
        "wxid":"",
        "remark":""
    }
}
```

### 13. <span id="acceptFriend">接收加好友请求(acceptFriend)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|v1           |对方V1|
|v2           |对方V2|
|scene        |好友来源，接收到的加好友请求XML信息中有|

|scene的值|参数的含义|
|:--------------|:---------|
|6              |好友验证, 加之前加过的人|
|14             |添加群好友|
|15             |通过查询添加|
|17             |通过名片添加，需要传v1值|

```json
{
    "api" : "acceptFriend",
    "sendId":"",
    "option" : {
        "v1":"",
        "v2":"",
        "scene":""
    }
}
```

### 14. <span id="acceptBankTransfer">接收好友转账(acceptBankTransfer)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|transferid   |收哪一笔转账(收到转账xml信息 中的 transferid)|

```json
{
    "api":"acceptBankTransfer",
    "sendId":"",
    "option":{
        "transferid":""
    }
}
```

### 15. <span id="refuseFriendWcpay">退还好友转账(refuseFriendWcpay)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|transferid   |退还哪一笔转账(收到转账xml信息 中的 transferid)|

```json
{
    "api":"refuseFriendWcpay",
    "sendId":"",
    "option":{
        "transferid":""
    }
}
```

### 16. <span id="autoAcceptFriend">自动同意加好友申请(autoAcceptFriend)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|auto         |0是取消自动，1自动|

```json
{
    "api":"autoAcceptFriend",
    "sendId":"",
    "option":{
        "auto":1
    }
}
```

### 17. <span id="autoAcceptWcpay">自动同意好友转帐(autoAcceptWcpay)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|auto         |0是取消自动，1自动|

```json
{
    "api":"autoAcceptWcpay",
    "sendId":"",
    "option":{
        "auto":1
    }
}
```

### 18. <span id="autoAcceptCard">自动加名片(autoAcceptCard)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|auto         |0是取消自动，1自动|

```json
{
    "api":"autoAcceptCard",
    "sendId":"",
    "option":{
        "auto":1
    }
}
```

### 19. <span id="acceptOnewayFriend">单向加好友(acceptOnewayFriend)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要添加的微信id|

> 注意:  
    当设置成添加时不需要验证，有好友添加，还需要再次确认添加  

```json
{
    "api":"acceptOnewayFriend",
    "sendId":"",
    "option":{
        "wxid":""
    }
}
```

### 20. <span id="searchContact">通过手机号/微信号/QQ号查询任意微信号信息(searchContact)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|search       |要查询的手机号/微信号/QQ号|

```json
{
    "api":"searchContact",
    "sendId":"",
    "option":{
        "search":""
    }
}
```

### 21. <span id="addSearchContact">添加通过任意手机号/微信号/QQ号查询的联系人(addSearchContact)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|v1           |对方V1|
|v2           |对方V2|
|remark       |加好友申请语|
|scene        |好友来源，接收到的加好友请求XML信息中有|

|scene的值|参数的含义|
|:--------------|:---------|
|6              |好友验证, 加之前加过的人|
|14             |添加群好友|
|15             |通过查询添加|
|17             |通过名片添加，需要传v1值|

```json
{
    "api":"addSearchContact",
    "sendId":"",
    "option":{
        "v1":"",
        "v2":"",
        "remark":"",
        "scene":15
    }
}
```

### 22. <span id="getChatRooms">获取普通群列表(getChatRooms)</span>
#### 参数说明

```json
{
    "api" : "getChatRooms",
    "sendId":"",
    "option" : { }
}
```

### 23. <span id="getImRooms">获取企业群列表(getImRooms)</span>
#### 参数说明

```json
{
    "api" : "getImRooms",
    "sendId":"",
    "option" : { }
}
```

### 24. <span id="getSingleChatRoomMembers">获取单个普通群成员信息(getSingleChatRoomMembers)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|

```json
{
    "api" : "getSingleChatRoomMembers",
    "sendId":"",
    "option" : {
        "roomWxid":""
    }
}
```

### 25. <span id="getSingleImRoomMembers">获取单个企业群成员信息(getSingleImRoomMembers)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|

```json
{
    "api" : "getSingleImRoomMembers",
    "sendId":"",
    "option" : {
        "roomWxid":""
    }
}
```

### 26. <span id="updateChatRoom">网络更新普通群成员信息(updateChatRoom)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|

```json
{
    "api" : "updateChatRoom",
    "sendId":"",
    "option" : {
        "roomWxid":""
    }
}
```

### 27. <span id="sendChatroomLow">发送40人以下群邀请(sendChatroomLow)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|wxidList     |要邀请的微信id|

> 注意:  
    人数少于40人的群，调用该接口，不需要好友同意即可直接拉入群

```json
{
    "api" : "sendChatroomLow",
    "sendId":"",
    "option" : {
        "roomWxid":"",
        "wxidList":["", ""]
    }
}
```

### 28. <span id="sendChatroomHigh">发送40人以上群邀请(sendChatroomHigh)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|wxidList     |要邀请的微信id|

> 注意:  
    对于人多的群，调用该接口，需要好友同意

```json
{
    "api" : "sendChatroomHigh",
    "sendId":"",
    "option" : {
        "roomWxid":"",
        "wxidList":["", ""]
    }
}
```

### 29. <span id="acceptChatroomInvite">接受群邀请(acceptChatroomInvite)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |好友的微信id|
|inviteurl    |好友发来的入群链接的地址 (该值从上报的入群链接消息的url字段中获取)|

```json
{
    "api":"acceptChatroomInvite",
    "sendId":"",
    "option":{
        "wxid":"",
        "inviteurl":"https://support...."
    }
}
```

### 30. <span id="delChatRoomMembers">踢群成员(delChatRoomMembers)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|wxidList     |要邀请的微信id|

> 注意:  
    当前微信必须有踢人权限  

```json
{
    "api":"delChatRoomMembers",
    "sendId":"",
    "option":{
        "roomWxid":"",
        "wxidList":["", ""]
    }
}
```

### 31. <span id="updateChatRoomName">修改群名称(updateChatRoomName)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|name         |要修改成的群名|

```json
{
    "api":"updateChatRoomName",
    "sendId":"",
    "option":{
        "roomWxid":"",
        "name":""
    }
}
```

### 32. <span id="sendChatRoomNotice">修改群公告(sendChatRoomNotice)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|notice       |群公告内容|

```json
{
    "api":"sendChatRoomNotice",
    "sendId":"",
    "option":{
        "roomWxid":"",
        "notice":""
    }
}
```

### 33. <span id="updateChatRoomDisplayName">修改我在本群的昵称(updateChatRoomDisplayName)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|nick         |我在本群的昵称|

```json
{
    "api" : "updateChatRoomDisplayName",
    "sendId":"",
    "option" : {
        "roomWxid":"",
        "nick":""
    }
}
```

### 34. <span id="showDisplayName">是否显示群昵称(showDisplayName)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|code         |0不显示，1显示|

```json
{
    "api":"showDisplayName",
    "sendId":"",
    "option":{
        "roomWxid":"",
        "code":1
    }
}
```

### 35. <span id="createChatRoom">创建群聊(createChatRoom)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxidLists    |要添加群聊的人员的微信id(由于群聊必须至少3个人, 因此必须包含至少2个好友的wxid)|

```json
{
    "api":"createChatRoom",
    "sendId":"",
    "option":{
        "wxidLists":""
    }
}
```

### 36. <span id="quitDelChatRoom">退出并删除群(quitDelChatRoom)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|

```json
{
    "api":"quitDelChatRoom",
    "sendId":"",
    "option":{
        "roomWxid":""
    }
}
```

### 37. <span id="autoAcceptChatRoom">自动接受群邀请(autoAcceptChatRoom)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|auto         |0是取消自动，1自动|

```json
{
    "api":"autoAcceptChatRoom",
    "sendId":"",
    "option":{
        "auto":1
    }
}
```

### 38. <span id="acceptQrcodeChatRoom">通过二维码进群(acceptQrcodeChatRoom)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|url          |二维码地址|

```json
{
    "api":"acceptQrcodeChatRoom",
    "sendId":"",
    "option":{
        "url":""
    }
}
```

### 39. <span id="saveRoomToContact">保存到/移出通讯录(saveRoomToContact)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|roomWxid     |群的微信id|
|code         |0移出通讯录，1保存到通讯录|

```json
{
    "api":"saveRoomToContact",
    "sendId":"",
    "option":{
        "roomWxid":"",
        "code":1
    }
}
```

### 40. <span id="transAnyMessage">任意消息转发(transAnyMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|msgid        |消息id|

```json
{
    "api" : "transAnyMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "msgid":""
    }
}
```

### 41. <span id="sendTextMessage">发送文本消息(sendTextMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|text         |消息文本|

```json
{
    "api" : "sendTextMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "text":"",
    }
}
```

### 42. <span id="sendAtTextMessage">发送群内@文本消息(sendAtTextMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|text         |消息文本|
|atlist       |@人的wxid|

> 注意:  
    文本消息text的内容中设置占位符{$@},代表被@群成员，占位符的数量必须和atlist中的微信号数量相等。

```json
{
    "api" : "sendAtTextMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "text":"你好{$@},你好{$@},哈哈哈",
        "atlist":["wxid_xxx","wxid_xxx"]
    }
}
```

### 43. <span id="sendPicMessage">发送图片(sendPicMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|imgPath      |图片地址(客户端所在主机的本地图片地址)|

> 注意:  
    在线图片需要调用接口下载到本地，再发出

```json
{
    "api" : "sendPicMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "imgPath":""
    }
}
```

### 44. <span id="sendFileMessage">发送文件(sendFileMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|filePath     |文件地址(客户端所在主机的本地文件地址)|

> 注意:  
    在线文件需要调用接口下载到本地，再发出

```json
{
    "api" : "sendFileMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "filePath":""
    }
}
```

### 45. <span id="sendVideoMessage">发送视频(sendVideoMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|videoPath    |视频地址(客户端所在主机的本地视频文件地址)|

> 注意:  
    在线视频需要调用接口下载到本地，再发出

```json
{
    "api" : "sendVideoMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "videoPath":""
    }
}
```

### 46. <span id="sendGifMessage">发送GIF表情(sendGifMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|gifPath      |本地gif图片地址|

```json
{
    "api" : "sendGifMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "gifPath":""
    }
}
```

### 47. <span id="sendLinkMessage">发送链接消息(sendLinkMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|title        |标题|
|url          |url链接|
|desc         |描述|
|pic          |在线图片url链接|

```json
{
    "api" : "sendLinkMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "title":"标题",
        "url":"url链接",
        "desc":"描述",
        "pic":"图片url链接"
    }
}
```

### 48. <span id="sendCardMessage">发送名片(sendCardMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|wxidCard     |要发送的名片的微信id|

```json
{
    "api" : "sendCardMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "wxidCard":""
    }
}
```

### 49. <span id="sendMiniMessage">发送小程序(sendMiniMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|msgid        |小程序的消息id|

```json
{
    "api" : "sendMiniMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "msgid":""
    }
}
```

### 50. <span id="sendFavorite">发送收藏(sendFavorite)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|localId      |从获取收藏列表处，获取localId|

```json
{
    "api" : "sendFavorite",
    "sendId":"",
    "option" : {
        "wxid":"",
        "localId":""
    }
}
```

### 51. <span id="sendXmlMessage">发送xml消息(sendXmlMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|xml          |要发送的xml数据|

```json
{
    "api" : "sendXmlMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "xml":""
    }
}
```

### 52. <span id="sendCardXmlMessage">发送名片xml消息(sendCardXmlMessage)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|xml          |要发送的名片的xml数据|

```json
{
    "api" : "sendCardXmlMessage",
    "sendId":"",
    "option" : {
        "wxid":"",
        "xml":""
    }
}
```

### 53. <span id="addPublic">关注公众号(addPublic)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|scene        |添加来源，可空|

```json
{
    "api" : "addPublic",
    "sendId":"",
    "option" : {
        "wxid":"",
        "scene":""
    }
}
```

### 54. <span id="getFavorites">获取收藏列表(getFavorites)</span>
#### 参数说明

```json
{
    "api" : "getFavorites",
    "sendId":"",
    "option" : { }
}
```

### 55. <span id="addFavoriteFrom">收藏指定消息(addFavoriteFrom)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|msgid        |要收藏的消息的消息id|

```json
{
    "api" : "addFavoriteFrom",
    "sendId":"",
    "option" : {
        "wxid":"",
        "msgid":""
    }
}
```

### 56. <span id="transVoice">语音翻译(transVoice)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |要发送的对象的微信id|
|msgid        |要翻译的语音消息的消息id|

```json
{
    "api" : "transVoice",
    "sendId":"",
    "option" : {
        "wxid":"",
        "msgid":""
    }
}
```

### 57. <span id="zombieCheck">无痕清粉(zombieCheck)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |待检测的微信id|

```json
{
    "api" : "zombieCheck",
    "sendId":"",
    "option" : {
        "wxid":""
    }
}
```

### 58. <span id="decryptPic">解密图片(decryptPic)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|srcfile      |微信加密图片dat路径|
|tarfile      |指定解密后的jpg图片路径|

```json
{
    "api" : "decryptPic",
    "sendId":"",
    "option" : {
        "srcfile":"",
        "tarfile":""
    }
}
```

### 59. <span id="unreadMsgCountChange">获取未读消息数量(unreadMsgCountChange)</span>
#### 参数说明

```json
{
    "api" : "unreadMsgCountChange",
    "sendId":"",
    "option" : { }
}
```

### 60. <span id="clearChatHistory">清理微信聊天记录(clearChatHistory)</span>
#### 参数说明

```json
{
    "api" : "clearChatHistory",
    "sendId":"",
    "option" : { }
}
```

### 61. <span id="scanQrcodePic">识别二维码(scanQrcodePic)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|pic          |要识别的本地二维码文件路径|

```json
{
    "api" : "scanQrcodePic",
    "sendId":"",
    "option" : {
        "pic":""
    }
}
```

### 62. <span id="modRecvNotify">开启/关闭消息免打扰(modRecvNotify)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |微信id|
|code         |0是关闭，1开启|

```json
{
    "api" : "modRecvNotify",
    "sendId":"",
    "option" : {
        "wxid":"",
        "code":""
    }
}
```

### 63. <span id="chatSessionTop">置顶/取消置顶聊天(chatSessionTop)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|wxid         |微信id|
|code         |0是取消置顶，1置顶|

```json
{
    "api" : "chatSessionTop",
    "sendId":"",
    "option" : {
        "wxid":"",
        "code":""
    }
}
```

### 64. <span id="openBrowser">打开内置浏览器(openBrowser)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|url          |要打开的网页链接|

```json
{
    "api" : "openBrowser",
    "sendId":"",
    "option" : {
        "url":""
    }
}
```

### 65. <span id="disableRevoke">开启/关闭防撤回功能(disableRevoke)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|code         |1是开启防撤回，0是关闭|

```json
{
    "api" : "disableRevoke",
    "sendId":"",
    "option" : {
        "code":""
    }
}
```

### 66. <span id="checkUrlStatus">检测URL在微信中是否有效(checkUrlStatus)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|url          |要检测的网页链接|

```json
{
    "api" : "checkUrlStatus",
    "sendId":"",
    "option" : {
        "url":""
    }
}
```

### 67. <span id="getSqlData">查询微信数据库(getSqlData)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|sql          |数据库查询语句|
|db           |数据库id|
|extend       |查询语句标记字段|

|相关查询|sql语句|数据库|
|:------------|:--------|:--------|
|查询企业好友  |select UserName,NickName,SmallHeadImgUrl,Remark from OpenIMContact where UserName like '%openim' and Type%2=1|db:7|
|查询全部企业群|select UserName,NickName,SmallHeadImgUrl from OpenIMContact where UserName like '%@im.chatroom' and Type !=0|db:7|
|查询企业群群主|select RoomName,Owner from OpenIMChatroomData|db:7|
|查询企业群成员微信ID|select RoomName,UserName from OpenIMChatroomMember|db:7|
|查询单个企业微信群信息|select UserName,NickName,SmallHeadImgUrl from OpenIMContact where UserName='12321321@im.chatroom'|db:7|
|查询企业群中的企业微信用户信息|select UserName,NickName,SmallHeadImgUrl from OpenIMContact where UserName in ('wxid0','wxid1')|db:7|
|查询企业群中的非企业微信用户信息|select UserName,Alias,NickName,Remark from Contact where UserName in ('wxid0','wxid1')|db:1|
|查询企业群中的非企业微信用户头像信息|select usrName,smallHeadImgUrl from ContactHeadImgUrl where usrName in ('wxid0','wxid1')|db:1|

|db示例|参数的含义|数据库|
|:------------|:--------|:--------|
|1            |好友和群信息数据库|MicroMsg.db|
|2            |头像数据库|Misc.db|
|3            |多媒体数据库|Media.db|
|4            |聊天相关数据库|ChatMsg.db|
|5            |收藏相关数据库|Favorite.db|
|6            |消息相关数据库|MSG.db|
|7            |企业相关数据库|OpenIMContact.db|

```json
{
    "api" : "getSqlData",
    "sendId":"",
    "option" : {
        "sql":"",
        "db":1,
        "extend":"test"
    }
}
```

### 68. <span id="closeProcess">关闭进程(closeProcess)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|pid          |进程id(send_msg 接口中收到的 pid)|

```json
{
    "api":"closeProcess",
    "sendId":"",
    "option":{
        "pid":""
    }
}
```

### 69. <span id="uploadFile">把客户端所在PC的资料上传到指定服务器(uploadFile)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|cwxid        |当前登陆微信ID|
|filepath     |本地文件地址（如：C:/work/demo.md）|
|url          |文件上传的地址（如：http://xxx/upload）|

> 注意:  
    接受上传文件的服务器要自己搭建

```json
{
    "api":"uploadFile",
    "sendId":"",
    "option":{
        "cwxid":"xxxx",
        "filepath":"",
        "url":""
    }
}
```

### 70. <span id="downloadFile">下载资料到客户端所在PC(downloadFile)</span>
#### 参数说明
|option中的参数|参数的含义|
|:------------|:--------|
|cwxid        |当前登陆微信ID|
|url          |下载文件地址（如：http://xxx/test.txt）|

```json
{
    "api":"downloadFile",
    "sendId":"",
    "option":{
        "cwxid":"xxxxx",
        "url":""
    }
}
```

**商务合作请加微信：abcdefg_12345654321**

<img src="https://wequick-1257130190.cos.ap-shanghai.myqcloud.com/img/xiaore.jpg" width="200" align=center/>

**商务合作请加微信：DiscoveryUpup**

<img src="https://wequick-1257130190.cos.ap-shanghai.myqcloud.com/img/service.png" width="200" align=center/>
