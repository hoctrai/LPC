

import pandas as pd
import numpy as np
import array as arr
from main import Connect
from datetime import datetime


class Data_from_file:


    db = Connect.DB_connection()

    def __init__(self):
        print("")

    def readFile(self):
        X = pd.ExcelFile('C:/Users/nhtrai/Downloads/an-giang.xlsx')
        # aa = []
        b = []
        Province = 'an-giang'
        ngay = []
        for sheet in X.sheet_names:
            df = np.asarray(X.parse(sheet))
            rowdata = np.size(df, 0)
            coldata = len(df[0])

            for j in range(7, coldata):
                type = self.get_trans_type(str(df[0,j]))
                for i in range(1, rowdata):
                    date = datetime.strptime(df[i, 1], '%d-%m-%Y').date()
                    value = int(df[i,j])
                    self.db.insert_lpc(Province, date, type, False, value)
                    print(df[i, j])

    def get_trans_type(self):
        print()

    def get_trans_type(self,sType):

        if 'Head' in sType:
            return "HS"
        elif 'tail' in sType:
            return 'TS'
        elif '1st' in  sType:
            return "1st"
        elif 'in rs_' in sType:
                return 'rs_' + sType[6]
        else :
            return 'rs_' + sType[3]


run = Data_from_file()
run.readFile()