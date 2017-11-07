import time
import pandas as pd

stock = ['162411','512880','159915']
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

print(u'网格表:',df)


# 设置网格交易量
amount = {
    '162411':300,
    '512880':600,
    '159915':200,
}
print('amount',amount)

#获取行情
import easyquotation
## https://github.com/shidenggui/easyquotation

quotation = easyquotation.use( 'sina' )  # 新浪 ['sina'] 腾讯 ['tencent', 'qq']

now_pri={
    '162411': 0,
    '512880': 0,
    '159915': 0,
}


request = quotation.real( stock )  # 支持直接指定前缀，如 'sh000001'

for _stock in stock:
    now_pri[_stock] = request[_stock]['now']  ## 收盘价

print('now_pri',now_pri)


# 获取网格所在位置

position ={
    '162411': 0,
    '512880': 0,
    '159915': 0,
}

for _stock in stock:
    for pos in range( len( df[_stock] ) -1):
        if now_pri[_stock] > df[_stock][pos]:
            position[_stock] = pos
            break

print('position',position)

# 下单网格价
trade = {
    '162411': {'buy':0,'sell':0},
    '512880': {'buy':0,'sell':0},
    '159915': {'buy':0,'sell':0},
}

for _stock in stock:
    trade[_stock]['buy'] = ('%.3f' % df[_stock][position[_stock]+1])
    trade[_stock]['sell'] = ('%.3f' % (df[_stock][position[_stock] - 1]))

print('trade',trade)

try:
    import easystockr
    # 设置easystockr,需在windows下安装银河客户端，详见easystockr说明
    user = easystockr.use( 'yh_client' )  # 银河客户端支持 ['yh_client', '银河客户端']
    user.prepare( 'yh.json' )  # 配置文件路径
except:
    print(u'请检查客户端或easystockr设置')


# 自动下单失灵，为下单，引入回车确认下单
try:
    import win32api
    import win32con
except(ImportError):
    print(u'自动下单失灵，为下单，引入回车确认下单')
    print( u'加载win32api异常：ModuleNotFoundError: No module named \'win32api\'' )

def key_enter():
    win32api.keybd_event( 13, 0, 0, 0 )  # enter键位码是13
    win32api.keybd_event( 13, 0, win32con.KEYEVENTF_KEYUP, 0 )  # 释放按键
    time.sleep( 0.2 )

# 买入卖出
try:
    for _stock in stock:
        user.buy( _stock, trade[_stock]['buy'], amount[_stock] )
        key_enter()

        user.sell( _stock, trade[_stock]['sell'], amount[_stock] )
        key_enter()
except:
    print(u'下单异常')
else:
    print(u'网格已成功下单')

