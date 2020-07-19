#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:13:45 2020

@author: thanhquynh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:00:26 2020

@author: thanhquynh
"""

import pandas as pd
import numpy as np
import array as arr
class N4_01_GL:
    a = []
    df_N4_01_GL = pd.DataFrame()
    b = []
    c = []
    a2 = []
    a3 = []
    rowa = 0
    ngay = []
    #d = []
    #e = []
    
    def __init__(self, a, ngay, row):
        self.a = a
        self.ngay = ngay
        self.rowa = row
        print("")
    def readFile(self):
        X = pd.ExcelFile('ho-chi-minh.xlsx')
        a = []
        b = []
        ngay = []
        for sheet in X.sheet_names:
            df_N4_01_GL = np.asarray(X.parse(sheet))
            rowdata = np.size(df_N4_01_GL,0)
            coldata = np.size(df_N4_01_GL,1)
            
            for i in range(0,rowdata):
                b = df_N4_01_GL[i,11:coldata]
                a.extend(b)
                ngay.append(df_N4_01_GL[i,1])
        c = len(a)
        a = np.asarray(a)
        shape = (int(c/19),19)
        self.a = a.reshape(shape)
        self.rowa = np.size(self.a,0)
        self.ngay = ngay[self.rowa - 1]
        
    def getN4_01_GLevent(self):
        k = self.rowa
        c = list()
        for i in range(k - 4, k):
            self.b.append(self.a[i,:])
        self.b = np.asarray(self.b)
        c = [k for k in self.b[1:4, 0]]
        self.b[:,].sort()
        #print(self.b)
        m = 0
        #n = 0
        for i in range(1, 4):
            for j in range(0, 19):
                if c[i-1] == self.b[i-1,j]:
                    m = m + 1
            if m != 0:
                print('Bien co N4_01_GL trong ngay ' + self.ngay + ' khong co.')
                break
        if m == 0:
            self.c = np.asarray(list(dict.fromkeys(self.b[3,:])))
            print('Dan cuoc ngay ' + self.ngay + ' cua bien co N4_01_GL:')
            print(self.c)
        
    def display(self):
        self.readFile()
        self.getN4_01_GLevent()

        
        
        
       
run = N4_01_GL()

run.display()