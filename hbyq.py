import easyquotation
## https://github.com/shidenggui/easyquotation

import pandas as pd
import numpy as np
import json
import easytrader


class hbyq:

    def position(now_pri,wangge):
        for i in range( len( wangge ) ):
            if now_pri > wangge[i]:
                #print( i,wangge[i] )
                return i,wangge[i],wangge[i-1],wangge[i+1]
