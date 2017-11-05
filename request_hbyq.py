# 获取华宝油气收盘价

import easyquotation
## https://github.com/shidenggui/easyquotation

import pandas as pd
import numpy as np

quotation = easyquotation.use('sina') # 新浪 ['sina'] 腾讯 ['tencent', 'qq']

request = pd.DataFrame(quotation.real('162411')) # 支持直接指定前缀，如 'sh000001'

close = request[21:22]  ## 收盘价