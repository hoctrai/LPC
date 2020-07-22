from datetime import date, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd
from main import Connect
import unidecode
# import schedule


class Web_S():
    driver = object()
    db = object()

    # specialNumbers=[] #List to store specialNumber of the product
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.db = Connect.DB_connection()
        print()

    def setStation(self):
        strLink = 'http://ketqua.net/lich-quay-thuong'
        self.driver.get(strLink)
        content = self.driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find('table', attrs={
            'class': 'table table-bordered table-condensed table-hover kqbackground'
                     + ' table-kq-bold-border table-bordered qtk-hover'})
        try:
            tr = table.find('tr', attrs={'class': 'success'})
            list_a_tag = tr.findAll('a')
            lNone_support = ['Hôm nay', 'Điện Toán 123', 'Điện Toán 6x36', 'Thần Tài']

            for a in [k for k in list_a_tag if (k.text not in lNone_support)]:
                link = unidecode.unidecode(a.attrs['href']).replace('/', '').lower()
                web = object()
                if 'truyen-thong' in link:
                    web = TT_Translation_Datas()
                else:
                    web = South_Translation_Datas()

                web.display(link, self.driver, self.db)
                # self.getDay(link.replace('/','').lower())
                print(str(link).replace('/', '').lower())

        except ValueError:
            print('there are issues')

    def display(self):
        # schedule.every().day.at("16:10").do(self.setStation,'')
        self.setStation()
        # self.driver.close()


# (self.driver.page_source, self.db)
class South_Translation_Datas:
    delta = timedelta(days=7)

    def __init__(self):
        print()

    def getData(self, date_time, province, driver, db):
        content = driver.page_source
        soup = BeautifulSoup(content)

        a = soup.find('table', attrs={
            'class': 'table table-condensed kqcenter kqvertimarginw table-kq-border table-kq-hover table-kq-north-west table-bordered kqbackground table-kq-bold-border'})
        if a:
            try:
                redNumb = a.find('td', attrs={'id': 'rs_0_0'})
                headNumb = int(int(redNumb.text) / 10000)
                tailNumb = int(redNumb.text) % 100
                if (db.is_none_exist_lpc(province, date_time, "HS", headNumb)
                        and db.is_none_exist_lpc(province, date_time, "TS", tailNumb)):
                    db.insert_lpc(province, date_time, "HS", False, headNumb)
                    db.insert_lpc(province, date_time, "TS", False, tailNumb)

                    # giai 1
                    greenNumb = int(a.find('td', attrs={'id': 'rs_1_0'}).text) % 100
                    db.insert_lpc(province, date_time, "rs_1", False, greenNumb)

                    # giai 4
                    for i in range(0, 7):
                        strTdOfId = 'rs_4_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': strTdOfId}).text) % 100
                        db.insert_lpc(province, date_time, "rs_4", False, greenNumb)

                    # giai 8
                    greenNumb = int(a.find('td', attrs={'id': 'rs_8_0'}).text) % 100
                    db.insert_lpc(province, date_time, "rs_8", False, greenNumb)

                    # giai 2
                    greenNumb = int(a.find('td', attrs={'id': 'rs_2_0'}).text) % 100
                    db.insert_lpc(province, date_time, "rs_2", False, greenNumb)

                    # giai 3
                    for i in range(0, 2):
                        strTdOfId = 'rs_3_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': strTdOfId}).text) % 100
                        db.insert_lpc(province, date_time, "rs_3", False, greenNumb)

                    # giai 5
                    greenNumb = int(a.find('td', attrs={'id': 'rs_5_0'}).text) % 100
                    db.insert_lpc(province, date_time, "rs_5", False, greenNumb)

                    # giai 6
                    for i in range(0, 3):
                        strTdOfId = 'rs_6_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': strTdOfId}).text) % 100
                        db.insert_lpc(province, date_time, "rs_6", False, greenNumb)

                    # giai 7
                    greenNumb = int(a.find('td', attrs={'id': 'rs_7_0'}).text) % 100
                    db.insert_lpc(province, date_time, "rs_7", False, greenNumb)
                    # listDates.append(date.strftime("%d-%m-%Y"))

                else:
                    return timedelta(days=1000000000)
            except:
                print(str(date_time.strftime("%d-%m-%Y")) + province)
                db.rollback(date_time)
                return timedelta(days=1000000000)

        return timedelta(days=7)

    def getLink(self, strID, strStation, driver):
        if strID != "":
            strDate = "ngay=" + strID
        else:
            strDate = strID
        strLink = "http://ketqua.net/" + strStation + ".php?" + strDate
        driver.get(strLink)

    def getDay(self, province, driver, db):
        a = date(2017, 1, 1)
        date_time = date.today()

        while a < date_time:
            self.getLink(date_time.strftime('%d-%m-%Y'), province, driver)
            self.delta = self.getData(date_time, province.replace('xo-so-', ''), driver, db)
            date_time = date_time - self.delta

    def display(self, province, driver, db):
        self.getDay(province, driver, db)


# TT_Translation_Datas class is chill of Class South_Translation_Datas.
class TT_Translation_Datas(South_Translation_Datas):
    delta = timedelta(days=1)

    def __init__(self):
        print()

    def getData(self, date_time, province, driver, db):
        content = driver.page_source
        soup = BeautifulSoup(content)

        a = soup.find('table', attrs={
            'class': 'table table-condensed kqcenter kqvertimarginw table-kq-border' +
                     ' table-kq-hover table-kq-north-west table-bordered kqbackground table-kq-bold-border tb-phoi-border watermark'})
        if a:
            try:
                redNumb = a.find('td', attrs={'id': 'rs_0_0'})
                headNumb = int(int(redNumb.text) / 1000)
                tailNumb = int(redNumb.text) % 100
                if (db.is_none_exist_lpc(province, date_time, "HS", headNumb)
                        and db.is_none_exist_lpc(province, date_time, "TS", tailNumb)):
                    db.insert_lpc(province, date_time, "HS", False, headNumb)
                    db.insert_lpc(province, date_time, "TS", False, tailNumb)

                    # giai 1
                    greenNumb = int(a.find('td', attrs={'id': 'rs_1_0'}).text) % 100
                    db.insert_lpc(province, date_time, "rs_1", False, greenNumb)

                    # giai 2
                    for i in range(0, 2):
                        strTdOfId = 'rs_6_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': 'rs_2_0'}).text) % 100
                        db.insert_lpc(province, date_time, "rs_2", False, greenNumb)

                    # giai 3
                    for i in range(0, 6):
                        strTdOfId = 'rs_3_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': strTdOfId}).text) % 100
                        db.insert_lpc(province, date_time, "rs_3", False, greenNumb)

                    # giai 4
                    for i in range(0, 4):
                        strTdOfId = 'rs_4_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': strTdOfId}).text) % 100
                        db.insert_lpc(province, date_time, "rs_4", False, greenNumb)

                    # giai 5
                    for i in range(0, 6):
                        strTdOfId = 'rs_6_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': 'rs_5_0'}).text) % 100
                        db.insert_lpc(province, date_time, "rs_5", False, greenNumb)

                    # giai 6
                    for i in range(0, 3):
                        strTdOfId = 'rs_6_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': strTdOfId}).text) % 100
                        db.insert_lpc(province, date_time, "rs_6", False, greenNumb)

                    # giai 7
                    for i in range(0, 4):
                        strTdOfId = 'rs_6_' + str(i)
                        greenNumb = int(a.find('td', attrs={'id': 'rs_7_0'}).text) % 100
                        db.insert_lpc(province, date_time, "rs_7", False, greenNumb)
                    # listDates.append(date.strftime("%d-%m-%Y"))

                else:
                    return timedelta(days= 1000)
            except:
                print(str(date_time.strftime("%d-%m-%Y")))
        return timedelta(days=1)


run = Web_S()
run.display()
