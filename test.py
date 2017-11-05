import easytrader
from hbyq import hbyq
import time
#导入网格
wangge = hbyq.import_wg()


# 设置网格交易量
amount = 300

#获取行情
close = hbyq.close_price()


# 获取网格所在位置
(pos,pos_pri,up_pri,down_pri) = hbyq.position(close,wangge)

print('close:',close,'pos:',pos,'pos_price',pos_pri, 'up:',up_pri,'down:',down_pri)

#设置easytrader
user = easytrader.use('yh_client') # 银河客户端支持 ['yh_client', '银河客户端']
user.prepare('/path/to/your/yh_client.json') # 配置文件路径

#买入卖出
user.buy('162411',down_pri,amount)
time.sleep(5)

user.sell('162411',up_pri,amount)
time.sleep(5)

#完结
print("ok")

