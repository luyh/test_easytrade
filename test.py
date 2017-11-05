import easytrader
from hbyq import hbyq
import time
import win32api
import win32con

#导入网格
wangge = hbyq.import_wg()


# 设置网格交易量
amount = 300

#获取行情
now_pri = hbyq.now_price()


# 获取网格所在位置
(pos,pos_pri,up_pri,down_pri) = hbyq.position(close,wangge)

print('now:',now_pri,'pos:',pos,'pos_price',pos_pri, 'up:',up_pri,'down:',down_pri)

#设置easytrader
user = easytrader.use('yh_client') # 银河客户端支持 ['yh_client', '银河客户端']
user.prepare('yh.json') # 配置文件路径


#买入卖出
user.buy('162411',down_pri,amount)
win32api.keybd_event(13,0,0,0)  #enter键位码是13
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
time.sleep(0.1)
win32api.keybd_event(13,0,0,0)  #enter键位码是13
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键


user.sell('162411',up_pri,amount)
win32api.keybd_event(13,0,0,0)  #enter键位码是13
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
time.sleep(0.1)
win32api.keybd_event(13,0,0,0)  #enter键位码是13


#完结
print("ok")

