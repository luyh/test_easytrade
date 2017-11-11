import time
import pandas as pd
import json

stock = ['162411','512880','159915']

#网格数据，参考numbers文件
## 初始化数据，只需配置一次


def save_data(filename,data):
    with open( '%s.json'%filename,"w" ) as json_file:
        json.dump( data,json_file )
        print(u'写入数据%s.json'%filename)


def load_data(filename):
    with open( "%s.json"%filename, 'r' ) as load_f:
        data = json.load( load_f )
    print( u'读出数据%s.json' % filename)
    return data


def data_init():
    data = {
        '162411': (
        0.84, 0.816, 0.793, 0.771, 0.749, 0.728, 0.708, 0.688, 0.668, 0.649, 0.631, 0.613, 0.596, 0.579, 0.563, 0.547,
        0.532, 0.517, 0.502, 0.488, 0.474),
        '512880': (
        1.295, 1.263, 1.233, 1.203, 1.173, 1.145, 1.117, 1.089, 1.063, 1.037, 1.012, 0.987, 0.963, 0.939, 0.917, 0.894),
        '159915': (
        1.951, 1.9, 1.85, 1.801, 1.754, 1.708, 1.663, 1.619, 1.576, 1.535, 1.495, 1.455, 1.417, 1.380, 1.344, 1.308),
    }

    pos = {
        '162411': 12,
        '512880': 8,
        '159915': 3,
    }
    # 保存网格表为josn文件
    save_data('data',data)
    # 保存当前网格位置为josn文件
    save_data('pos',pos)

#初始化网格数据,第一次配置后不用再配置
#data_init()

# 读取网格
data = load_data('data')
print(u'载入网表')

#对应DataFrame，
d = {
        '162411':pd.Series(data['162411']),#华宝油气
        '512880':pd.Series(data['512880']),#证券
        '159915':pd.Series(data['159915']),#创业板
    }

df = pd.DataFrame(d)

print(u'网格表:\n',df)


#获取行情
import easyquotation
## https://github.com/shidenggui/easyquotation

quotation = easyquotation.use( 'sina' )  # 新浪 ['sina'] 腾讯 ['tencent', 'qq']

request_dic = quotation.real( stock )  # 支持直接指定前缀，如 'sh000001'
#print('request:',request_dic)

request_df = pd.DataFrame(request_dic)
#print(u'行情:\n',request_df)

request = request_df.loc[['name','now','high','low']]
print(u'行情:\n',request)


# 获取及调整网格所在位置
pos = load_data('pos')
print( u'初始网格位置', pos )

for _stock in stock:
    if request[_stock]['high'] > df[_stock][pos[_stock]-1]:
        pos[_stock]=pos[_stock]-1
        break
    elif request[_stock]['low'] < df[_stock][pos[_stock]+1]:
        pos[_stock]=pos[_stock]+1
        break

save_data('pos',pos)
print(u'调整网格位置',pos)

# 初始化交易数据
amount = {
    '162411':300,
    '512880':600,
    '159915':200
}

print(u'交易量：',amount)


# 下单网格价
trade = {
    '162411': {'buy':-1,'sell':-1},
    '512880': {'buy':-1,'sell':-1},
    '159915': {'buy':-1,'sell':-1},
}

for _stock in stock:
    trade[_stock]['buy'] = ('%.3f' % df[_stock][pos[_stock]+1])
    trade[_stock]['sell'] = ('%.3f' % (df[_stock][pos[_stock] - 1]))

print('trade',trade)

try:
    import easytrader
    # 设置easytrader,需在windows下安装银河客户端，详见easystockr说明
    user = easytrader.use( 'yh_client' )  # 银河客户端支持 ['yh_client', '银河客户端']
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

