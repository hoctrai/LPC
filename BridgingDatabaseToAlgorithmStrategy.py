from main import Connect
import unidecode


class Main_Bridge():
    db = object()
    cur = object()

    def __init__(self):
        self.db = Connect.DB_connection()
        # self.db.connect();
        # self.cur =
        print()

    # def get_table(self, province):
    #     sql = """
    #             SELECT date, type, value
    #             FROM lpc
    #             WHERE lpc.province = %s
    #     """
    #     self.db.get_cur().execute(sql, [province])
    #     print(self.db.get_cur().fetchall())
    def get_table(self, province):
        sql = """
                SELECT date, type, value
                FROM lpc
                WHERE   lpc.province = %s
        """
        self.db.get_cur().execute(sql, [province])
        ldb = self.db.get_cur().fetchall()
        return ldb
    def getData(self, province, start_day, delta_day, type):
        print()
run = Main_Bridge()
run.get_table('truyen-thong')