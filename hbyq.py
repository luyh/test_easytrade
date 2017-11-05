import easyquotation
## https://github.com/shidenggui/easyquotation

import pandas as pd
import numpy as np
import json
import easytrader


class hbyq:
    def import_wg():    # 导入网格
        f = open( "hbyq.txt" )  # 返回一个文件对象

        lines = f.readlines()  # 读取全部内容
        f.close()

        hbyq = []

        for i in range( len( lines ) ):
            hbyq.append( (float( lines[i][:-1] )) )

        # print( (hbyq) )
        return hbyq

    def close_price():  # 获取华宝油气收盘价
        quotation = easyquotation.use( 'sina' )  # 新浪 ['sina'] 腾讯 ['tencent', 'qq']

        request =  quotation.real( '162411' )  # 支持直接指定前缀，如 'sh000001'
        #print(request)
        close = request['162411']['close']  ## 收盘价

        #print('close:',close)
        #print(type(close))
        return close

    def position(close,wangge):
        for i in range( len( wangge ) ):
            if close > wangge[i]:
                #print( i,wangge[i] )
                return i,wangge[i],wangge[i-1],wangge[i+1]




