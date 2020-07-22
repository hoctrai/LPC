from main import Connect
import logging

class DataTest():

    db = object()
    def __init__(self):
        self.db = Connect.DB_connection()

    def test(self):
        file_logger = logging.FileHandler('data_test.log')
        FORMAT = '%(message)s'
        file_logger_format = logging.Formatter(FORMAT)
        file_logger.setFormatter(file_logger_format)

        sql_date = """   SELECT DISTINCT date
                    FROM lpc
                    ORDER BY date ASC"""
        sql_province = """   SELECT DISTINCT province
                            FROM lpc
                            WHERE lpc.date =%s """
        self.db.get_cur().execute(sql_date)
        list_dates = self.db.get_cur().fetchall()
        for date in list_dates:
            self.db.get_cur().execute(sql_province,[date])
            list_provinces = self.db.get_cur().fetchall()
            for province in list_provinces:
                sql = """   SELECT *
                            FROM lpc 
                            WHERE 
                                lpc.province = %s AND 
                                lpc.date = %s """
                self.db.cur.execute(sql, [province, date])
                if (self.db.cur.rowcount < 27 and province == 'truyen-thong') or (self.db.cur.rowcount < 19 and province != 'truyen-thong'):
                    self.db.rollback(province, date)
                    logging.info(str(province) + str(date) + "is not value!!")

    def display(self):
        self.test()
        print()

run = DataTest();
run.display()