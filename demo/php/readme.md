# weHelper 项目介绍

## 数据库
### wxq_friends_list 表
"id":"",
"cwxid":"",
"wxid":"5565811606@chatroom", //wxid
"nick":"招财进8", //昵称
"username":"(null)", //微信账号 用户设置的
"asName":"(null)", //备注名
"headPic":"http://wx.qlogo.cn/mmcrhead/PiajxSqBRaEJ4UnsZgXPGwah6FmInDCxibeuVFw8XwXZxBbVQyhFIfCG91grETccQMvJZvq9wbL3Pjp5DxSY3GuaMvUghCgRCP/0", //头像
"sex":"1", //性别
"nationality":"CN", //国籍
"province":"湖北", //省份
"city":"武汉", //城市
"type":2, //类型 1个人号 2群 3公众号
"groupId":"如果是群成员，这个字段用来放群id" //群成员关联的群wxid
"created_date":"",
"updated_date":""

### wxq_config 表
id
cwxid
config_json //配置的json字符串长度不限
config_name //配置的名称
status //配置开关1开 0关 默认1

### wxq_white_black_lists 表
cwxid //所属人wxid
wxid //被加入到黑白名单中的人
type //用来区分是白名单还是黑名单 0(默认不在黑白名单中) 1白名单 2黑名单
chatroom //所在群id 可为空
nick //昵称
headPic //头像地址
auth //权限字段 保留字段 里面保存的是json字符串 给个不限制长度的字

### wxq_zombies 表
"id":"",
"webUser":"",
"cwxid":"",
"wxid":"5565811606@chatroom", //wxid
"nick":"招财进8", //昵称
"username":"(null)", //微信账号 用户设置的
"asName":"(null)", //备注名
"headPic":"http://wx.qlwCgRCP/0", //头像
"sex":"1", //性别
"created_date":"",
"updated_date":""

str = "qwqw1qw61qw1q6w151a1sd65^*(^%$#$@+)#(#&#^!%@asd1as1da1s65d5re5re15rere51er1@@#UI*#*(@*&!@@!&)(!@#&$*$&*"

## 请求
### 所有请求的返回值类型
 [
    "code" : 200,
    "message" : null,
    "data" => []
  ];
code = 200 代表通过
code = 400 代表未通过

#### 好友相关

url : /friend/add
请求方式 : post
作用：添加好友 或 修改好友信息，若没有查到该好友则添加，否则修改
参数：data(json数据,json中的数据的key需和以上表字段相同)
签名 key：cc
签名 value：（data + str） 的 MD5 值

url : /friendslist/{cwxid}/{type?}
请求方式 : get
作用：获取好友列表
参数：cwxid,type(可以没有)
签名 key：ff （验证未开启）
签名 value：（cwxid + str）的 MD5 值

url : /friendsnum/{cwxid}
请求方式 : get
作用：获取好友数量
参数：cwxid

url : /friend/destroy
请求方式 : post
作用：删除好友
参数：cwxid, wxid
签名 key：gg
签名 value：（cwxid + str）的 MD5 值

#### 配置相关

url : /config/add
请求方式 : post
作用：添加配置 或 修改配置信息
参数：data（json数据,json中的数据的key需和以上表字段相同）
签名 key：aa（验证未开启）
签名 value：（data + str） 的 MD5 值

url : /config/{cwxid}/{config_name}
请求方式 : get
作用：获取配置信息
参数：cwxid,config_name
签名 key：bb
签名 value：（config_name + str）的 MD5 值

url : /config/destroy
请求方式 : post
作用：删除配置
参数：cwxid,config_name
签名 key：dd
签名 value：（config_name + str）的 MD5 值

#### 黑白名单相关

url： /auth/add
请求方式：post
参数：data(json数据,json中的数据的key需和以上表字段相同)
作用：添加或更新黑白名单
签名 key：hba
签名value：（data + str） 的 MD5 值

url： /authlist/{cwxid}/{type}
请求方式：get
参数： cwxid, type
作用：查询黑白名单
签名 key：hbl
签名 value：（cwxid + str） 的 MD5 值

url：/auth/destory
请求方式：post
参数：cwxid, wxid
作用：删除某人在黑白名单中的记录
签名 key：hbd
签名 value：（cwxid + str） 的 MD5 值

#### 僵尸粉相关
url : /zombie/add
请求方式 : post
作用：添加僵尸粉 或 修改僵尸粉信息，若没有查到该僵尸粉则添加，否则修改
参数：data(json数据,json中的数据的key需和以上表字段相同)
签名 key：zba
签名 value：（data + str） 的 MD5 值

url : /zombieslist/{webuser}/{cwxid}
请求方式 : get
作用：获取僵尸粉列表
参数：cwxid

url : /zombiesnum/{webuser}/{cwxid}
请求方式 : get
作用：获取僵尸粉数量
参数：cwxid
