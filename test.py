import easytrader
from hbyq import hbyq
import time
import pandas as pd

trade = ('162411','512880','159915')
#网格数据，参考numbers文件
hbqy = (0.84,0.816,0.793,0.771,0.749,0.728,0.708,0.688,0.668,0.649,0.631,0.613,0.596,0.579,0.563,0.547,0.532,0.517,0.502,0.488,0.474)
zqetf =(1.295,1.263,1.233,1.203,1.173,1.145,1.117,1.089,1.063,1.037,1.012,0.987,0.963,0.939,0.917,0.894)
cybetf = (1.951,1.9,1.85,1.801,1.754,1.708,1.663,1.619,1.576,1.535,1.495,1.455,1.417,1.380,1.344,1.308)

d = {
        '162411':pd.Series(hbqy,index=range(len(hbqy))),#华宝油气
        '512880':pd.Series(zqetf,index=range(len(zqetf))),#证券
        '159915':pd.Series(cybetf,index=range(len(cybetf))),#创业板
        }

df = pd.DataFrame(d)

# print(df)


# 设置网格交易量
amount = {
    '162411':300,
    '512880':600,
    '159915':200,
}


#获取行情
import easyquotation
## https://github.com/shidenggui/easyquotation

quotation = easyquotation.use( 'sina' )  # 新浪 ['sina'] 腾讯 ['tencent', 'qq']

now_pri={
    '162411': 0,
    '512880': 0,
    '159915': 0,
}

for _trade in trade:
    request = quotation.real( _trade )  # 支持直接指定前缀，如 'sh000001'
    now_pri[_trade] = request[_trade]['now']  ## 收盘价
    print(now_pri[_trade])


# 获取网格所在位置
try:
    (pos,pos_pri,up_pri,down_pri) = hbyq.position(now_pri,wangge)
    print( 'now:', now_pri, 'pos:', pos, 'pos_price', pos_pri, 'up:', up_pri, 'down:', down_pri )
    # 设置easytrader
    user = easytrader.use( 'yh_client' )  # 银河客户端支持 ['yh_client', '银河客户端']
    user.prepare( 'yh.json' )  # 配置文件路径

    try:
        import win32api
        import win32con

    except(ImportError):
        print( 'ModuleNotFoundError: No module named \'win32api\'' )

    # 买入卖出
    user.buy( '162411', down_pri, amount )
    win32api.keybd_event( 13, 0, 0, 0 )  # enter键位码是13
    win32api.keybd_event( 13, 0, win32con.KEYEVENTF_KEYUP, 0 )  # 释放按键
    time.sleep( 0.1 )
    win32api.keybd_event( 13, 0, 0, 0 )  # enter键位码是13
    win32api.keybd_event( 13, 0, win32con.KEYEVENTF_KEYUP, 0 )  # 释放按键

    user.sell( '162411', up_pri, amount )
    win32api.keybd_event( 13, 0, 0, 0 )  # enter键位码是13
    win32api.keybd_event( 13, 0, win32con.KEYEVENTF_KEYUP, 0 )  # 释放按键
    time.sleep( 0.1 )
    win32api.keybd_event( 13, 0, 0, 0 )  # enter键位码是13

except:
    print('error')


#完结
print("ok")

