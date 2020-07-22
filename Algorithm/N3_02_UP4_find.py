#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:19:42 2020

@author: thanhquynh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:17:14 2020

@author: thanhquynh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:19:09 2020

@author: thanhquynh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:23:08 2020

@author: thanhquynh
"""

import pandas as pd
import numpy as np
import array as arr
class N3_02_UP4:
    a = []
    df_N3_02_UP4 = pd.DataFrame()
    b = []
    c = []
    a2 = []
    a3 = []
    rowa = 0
    ngay = []
    #d = []
    #e = []
    
    def __init__(self, ngay):
        self.rowa = len(ngay)
        self.ngay = ngay
        print("")
    def readFile(self):
        X = pd.ExcelFile('truyenthong.xlsx')
        #aa = []
        b = []
        ngay = []
        for sheet in X.sheet_names:
            df_N3_02_UP4 = np.asarray(X.parse(sheet))
            rowdata = np.size(df_N3_02_UP4,0)
            
            for i in range(0,rowdata):
                b = df_N3_02_UP4[i,12]
                self.a.append(b)
                ngay.append(df_N3_02_UP4[i,1])
        
        self.rowa = len(self.a)
        self.ngay = ngay[self.rowa - 1]
        
    def getN3_02_UP4event(self):
        k = self.rowa
        b = []
        c = [k for k in range(0,50)]
        for i in range(k - 4, k):
            self.b.append(self.a[i])
        b = [k for k in self.b if (k >= 50)]
        if len(b) == 4:
            print('Dan cuoc ngay ' + self.ngay + ' cua bien co N3_02_UP4:')
            print(c)
        else:
            print('Bien co N3_02_UP4 trong ngay ' + self.ngay + ' khong co.')
        #print(self.b)
        
    def display(self):
        self.readFile()
        self.getN3_02_UP4event()

        
        
        
       
# run = N3_02_UP4()

# run.display()