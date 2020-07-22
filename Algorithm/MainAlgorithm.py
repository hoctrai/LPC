from main import Connect
from main.Algorithm import Parrot_r, N1_01_GL_find, N1_02_UP4_find, N3_01_GL_find, N3_02_UP4_find, B4_01_GL_find
from datetime import date, timedelta
import numpy as np


class Algorithm():
    # bridge = object()

    db_table = []
    ldb = []
    HS = []
    TS = []
    rs_1 = []
    count_list_in_arr = 0

    def __init__(self):
        self.db = Connect.DB_connection()

        self.set_data()

        self.HS = self.get_sub_data('HS')
        self.TS = self.get_sub_data('TS')
        self.rs_1 = self.get_sub_data('rs_1')
        self.data_per_date = self.get_data_per_date()

        print()

    def set_data(self):
        sql =   """
                    SELECT date, type, value
                    FROM lpc
                    WHERE   lpc.province = %s
                """
        self.db.get_cur().execute(sql, ['truyen-thong'])
        self.db_table = self.db.get_cur().fetchall()
        # return ldb
    def get_sub_data(self, str_type):
        list_sub_data = [k[2] for k in self.db_table if (k[1] == str_type)] #and (k[2].is_integer())]
        return list_sub_data

    def get_data_per_date(self):
        arr_data = np.empty((0,19), int)
        date_time = date.today()- timedelta(days = 6)
        while date_time > date(2017,1,1):
            try:
                list_sub_data = [k[2] for k in self.db_table if (k[0] == date_time)]
                arr_data = np.concatenate((arr_data, [list_sub_data]),axis=0)
                date_time = date_time - timedelta(days = 7)
                self.count_list_in_arr = self.count_list_in_arr + 1
            except:
                print (date_time)
                break

        return arr_data

    def run(self):
        algorithm = input("chose algorithm: ")
        if algorithm == '1':
            par_r = Parrot_r.parrot_r(self.HS, self.TS, self.rs_1)
            par_r.display()
        elif algorithm == '2':
            algor = N1_01_GL_find.N1_01_GL(self.data_per_date, self.count_list_in_arr)
            algor.display()
        elif algorithm == '3':
            algor = N1_02_UP4_find.N1_02_UP4(self.rs_1)
            algor.display()
        elif algorithm == '4':
            algor = N3_01_GL_find.N3_01_GL(self.data_per_date, self.count_list_in_arr)
            algor.display()
        # elif algorithm == '5':
        #     algor = N3_02_UP4_find.N3_02_UP4(self.rs_1)
        #     algor.display()
        # elif algorithm == '6':
        #     algor = N4_01_GL_find.N4_01_GL(self.rs_1)
        #     algor.display()
        elif algorithm =='7':
            algor = B4_01_GL_find.B4_01_GL(self.data_per_date, self.count_list_in_arr)
            algor.display()
run = Algorithm()
run.run()