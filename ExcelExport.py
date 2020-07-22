from main import Connect
import logging
import pandas as pd

class ExcelExport():
    db = object()

    def __init__(self):
        self.db = Connect.DB_connection()

    def outputFile(self):
        df = pd.DataFrame({'Date': self.lIDs, 'special': self.specialNumbers, 'in 7st_1': self.rs_7_Numb1,
                           'in 7st_2': self.rs_7_Numb2, 'in 7st_3': self.rs_7_Numb3, 'in 7st_4': self.rs_7_Numb4})
        df.to_csv('TicketNumber.csv', index=False, encoding='utf-8')

        df.close()
        pass

    def display(self):
        sql_province = """  SELECT DISTINCT province
                        FROM lpc """
        sql_date = """  SELECT date
                            FROM lpc
                            WHERE lpc.province =%s 
                            ORDER BY date ASC """

        self.db.get_cur().execute(sql_province)
        list_provinces = self.db.get_cur().fetchall()
        for province in list_provinces:
            self.db.get_cur().execute(sql_date, [province])
            list_dates = self.db.get_cur().fetchall()
            for date in list_dates:
                print()

