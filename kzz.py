#coding=utf-8
import urllib
import time

users = ['luyh','heml']

stokc = ''
amount = 10000
price = 100


import easytrader
    # 设置easytrader,需在windows下安装银河客户端，详见easystockr说明
user = easytrader.use( 'yh_client' )  # 银河客户端支持 ['yh_client', '银河客户端']

try:
    for _user in users:
        user.prepare( 'users/%s.json'%_user )  # 配置文件路径
        #user.buy( stock, price, amount )       
        print(_user)
        time.sleep(25)


except:
    print(u'请检查客户端或easystockr设置')

