#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:53:04 2020

@author: thanhquynh
"""

#not yet evaluation criteria good or not good of the events.

import pandas as pd
import numpy as np
import array as arr
import matplotlib.pyplot as plt
# from main import BridgingDatabaseToAlgorithmStrategy


class parrot_r:
    TS = []
    HS = []
    G1 = []
    data = []
    row_data = 0
    # column_data = 0

    def __init__(self, HS, TS, G1):
        self.TS = TS
        self.HS = HS
        self.G1 = G1
        self.row_data = len(TS)
        self.all = np.transpose(np.asarray([self.TS, self.HS, self.G1]))


    # def __init__(self):
    #     print()

    def readFile(self):
        # data = BridgingDatabaseToAlgorithmStrategy.Main_Bridge()
        # df_01_GL = np.asarray(data.get_table('truyen-thong'))

        X = pd.ExcelFile('truyenthong.xlsx')
        a = []

        for sheet in X.sheet_names:
            df_01_GL = np.asarray(X.parse(sheet))
            rowdata = np.size(df_01_GL, 0)
            coldata = np.size(df_01_GL, 1)

            for i in range(0, rowdata):
                b = df_01_GL[i, 7:coldata]
                # d = df_01_GL[i,8:coldata]
                a.extend(b)
                # e.extend(d)
                # ngay.append(df_B4_01_GL[i,1])
        c = len(a)
        # f = len(e)
        a = np.asarray(a)
        #        e = np.asarray(e)
        shape_HS = (int(c / 28), 28)
        # shape = (int(f/27), 27)
        self.data = a.reshape(shape_HS)
        self.row_data = np.size(self.data, 0)
        # self.column_data = np.size(self.data, 1)
        self.TS = self.data[:, 1]
        self.HS = self.data[:, 0]
        self.G1 = self.data[:, 2]
        self.all = np.transpose(np.asarray([self.TS, self.HS, self.G1]))
        self.row_data = np.size(self.data, 0)
        # self.column_data = np.size(self.data, 1)
        # self.ngay = ngay[self.row_B4 - 1]

    def get_queue(self, num_condition, queue):
        if (num_condition == 1):
            return [k for k in queue if (k >= 50)]
        elif (num_condition == 2):
            return [k for k in queue if (k < 50)]
        elif (num_condition == 3):
            return [k for k in queue if (k % 2 == 0)]
        elif (num_condition == 4):
            return [k for k in queue if (k % 2 != 0)]
        elif (num_condition == 5):
            return [k for k in queue if ((k % 2 == 0 and (k // 10) % 2 == 0) or (k % 2 != 0 and (k // 10) % 2 != 0))]
        else:
            return [k for k in queue if ((k % 2 == 0 and (k // 10) % 2 != 0) or (k % 2 != 0 and (k // 10) % 2 == 0))]

    def check_conditions(self, num_condition, a):
        if (num_condition == 1, a >= 50):
            return True
        elif (num_condition == 2, a < 50):
            return True
        elif (num_condition == 3, a % 2 == 0):
            return True
        elif (num_condition == 4, a % 2 != 0):
            return True
        elif (a % 2 == 0 and (a // 10) % 2 == 0) or (a % 2 != 0 and (a // 10) % 2 != 0):
            return True
        elif (a % 2 == 0 and (a // 10) % 2 != 0) or (a % 2 != 0 and (a // 10) % 2 == 0):
            return True

        return False

    def check_event(self, event):
        if event == 'B1':
            return self.G1
        elif event == 'B3':
            return self.TS
        elif event == 'B4':
            return self.HS
        else:
            return self.all
        
    def display_bet(self, event):
        if event == 'B1':
            return 'B1'
        elif event == 'B3':
            return 'B1'
        elif event == 'B4':
            return 'B4'
        else:
            return 'a'
            
    
    def display_name(self, num_condition):
        if num_condition == 1:
            return (' UP')
        if num_condition == 2:
            return str(' DOWN')
        if num_condition == 3:
            return str(' EVEN')
        if num_condition == 4:
            return str(' ODD')
        if num_condition == 5:
            return str(' EE or OO')
        if num_condition == 6:
            return str(' EO or OE')
        return 'aaa'

    def getQueue(self):
        event = input('Nhap Kieu Cuoc (B1: cuoc giai nhat, B3: cuoc Tail Special, B4: cuoc Head Special, Ball: tat ca cac kieu cuoc): ')
        type_repeat = int(input('Nhap kieu lap lai (1: up, 2: down, 3: even, 4: odd, 5: ee or oo, 6: oe or eo, 7: all): '))
        #index = 1
        #list_event = self.check_event(event)
        #print(list_event)
        if (event == 'Ball' or event == 'ball') and type_repeat == 7:
            c = ('B1', 'B3', 'B4')
            table = []
            for i in range(0,3):
                for k in range (1,7):
                    type_repeat = k        
                    index = 1
                    event1 = c[i]
                    #print(event1)
                    list_event = self.check_event(event1)
                    n = 100
                    ngay = 1
                    while index < n:
                        
                        lose = 0
                        win = 0
                        j = 0
                        while j < self.row_data - index:
                            queue1 = self.get_queue(type_repeat, list_event[j:(j + index)])
                            
                            if len(queue1) == index:
                                a = list_event[j + index]
                                b = list()
                                b.append(a)
                                if len(self.get_queue(type_repeat, b)) == 1:
                                    win = win + 1
                                    j = j + index
                                else:
                                    lose = lose + 1
                                    j = j + index
                            # prin
            
                            j = j + 1
                        if win == 0 and lose == 0:
                            break
                        total = win + lose
                        profit1 = win * 49 - lose * 50
                        table.append(event1)
                        name1 = self.display_name(type_repeat)
                        table.append(name1)
                        table.append(ngay)
                        table.append(lose)
                        table.append(win)
                        table.append(total)
                        prob = round(win / (win + lose),3)
                        # profit2 = 99*prob - 27
                        table.append(prob)
                        table.append(profit1)
                        # table.append(profit2)
                        index = index + 1
                        ngay = ngay + 1
            table = np.asarray(table)
            shape = (int(len(table) / 8), 8)
            table = table.reshape(shape)
            f = np.size(table, 0)
            table = pd.DataFrame(table)
            table.columns = ['Local','Parrot', 'Days', 'Lose', 'Win', 'Total', 'Prob', 'Profit1']
            table.insert(0, "Province", "TT", True)
            name2 = '50'
            table.insert(7, "Ar.Length", name2, True)
            print('')
                #print('Table of number of days corresponding with '+ str(event) + name)
            print(table)
            
        elif event == 'Ball' or event == 'ball' and type_repeat != 7:
            c = ('B1', 'B3', 'B4')
            table = []
            for i in range(0,3):
                index = 1
                event1 = c[i]
                #print(event1)
                list_event = self.check_event(event1)
                n = 100
                ngay = 1
                while index < n:
                    table.append(ngay)
                    lose = 0
                    win = 0
                    j = 0
                    while j < self.row_data - index:
                        queue1 = self.get_queue(type_repeat, list_event[j:(j + index)])
                        
                        if len(queue1) == index:
                            a = list_event[j + index]
                            b = list()
                            b.append(a)
                            if len(self.get_queue(type_repeat, b)) == 1:
                                win = win + 1
                                j = j + index
                            else:
                                lose = lose + 1
                                j = j + index
                        # prin
        
                        j = j + 1
                    if win == 0 and lose == 0:
                        break
                    total = win + lose
                    profit1 = win * 49 - lose * 50
                    table.append(lose)
                    table.append(win)
                    table.append(total)
                    prob = round(win / (win + lose),3)
                    # profit2 = 99*prob - 27
                    table.append(prob)
                    table.append(profit1)
                    # table.append(profit2)
                    index = index + 1
                    ngay = ngay + 1
            table = np.asarray(table)
            shape = (int(len(table) / 6), 6)
            table = table.reshape(shape)
            f = np.size(table, 0)
            table = pd.DataFrame(table)
            table.columns = ['Days', 'Lose', 'Win', 'Total', 'Prob', 'Profit1']
            table.insert(0, "Province", "TT", True)
            table.insert(1, "Local", self.display_bet(event), True)
            name1 = self.display_name(type_repeat)
            table.insert(2, "Parrot", name1, True)
            name2 = '50'
            table.insert(7, "Ar.Length", name2, True)
            print('')
                #print('Table of number of days corresponding with '+ str(event) + name)
            print(table)

        elif (event != 'Ball' or event != 'ball') and type_repeat != 7:
            list_event = self.check_event(event)
            n = 100
            index = 1
            table = []
            while index < n:
                lose = 0
                win = 0
                j = 0
                while j < self.row_data - index:
                    queue1 = self.get_queue(type_repeat, list_event[j:(j + index)])
                    
                    if len(queue1) == index:
                        a = list_event[j + index]
                        b = list()
                        b.append(a)
                        if len(self.get_queue(type_repeat, b)) == 1:
                            win = win + 1
                            j = j + index
                        else:
                            lose = lose + 1
                            j = j + index
                    # prin
    
                    j = j + 1
                if win == 0 and lose == 0:
                    break
                total = win + lose
                profit1 = win * 49 - lose * 50
                table.append(lose)
                table.append(win)
                table.append(total)
                prob = round(win / (win + lose),3)
                # profit2 = 99*prob - 27
                table.append(prob)
                table.append(profit1)
                # table.append(profit2)
                index = index + 1
            table = np.asarray(table)
            shape = (int(len(table) / 5), 5)
            table = table.reshape(shape)
            f = np.size(table, 0)
            table = pd.DataFrame(table)
            table.columns = ['Lose', 'Win', 'Total', 'Prob', 'Profit1']
            table.insert(0, "Province", "TT", True)
            table.insert(1, "Local", self.display_bet(event), True)
            name1 = self.display_name(type_repeat)
            table.insert(2, "Parrot", name1, True)
            table.insert(3, "Days", range(1, f + 1), True)
            name2 = '50'
            table.insert(7, "Ar.Length", name2, True)
            print('')
                #print('Table of number of days corresponding with '+ str(event) + name)
            print(table)
        
        elif event != 'Ball' and type_repeat == 7:
            table = []
            for k in range (1,7):
                type_repeat = k        
                index = 1
                #print(event1)
                list_event = self.check_event(event)
                n = 100
                ngay = 1
                while index < n:
                    lose = 0
                    win = 0
                    j = 0
                    while j < self.row_data - index:
                        queue1 = self.get_queue(type_repeat, list_event[j:(j + index)])
                        
                        if len(queue1) == index:
                            a = list_event[j + index]
                            b = list()
                            b.append(a)
                            if len(self.get_queue(type_repeat, b)) == 1:
                                win = win + 1
                                j = j + index
                            else:
                                lose = lose + 1
                                j = j + index
                        # prin
        
                        j = j + 1
                    if win == 0 and lose == 0:
                        
                        break
                    total = win + lose
                    profit1 = win * 49 - lose * 50
                    name1 = self.display_name(type_repeat)
                    table.append(name1)
                    table.append(ngay)
                    table.append(lose)
                    table.append(win)
                    table.append(total)
                    prob = round(win / (win + lose),3)
                    # profit2 = 99*prob - 27
                    table.append(prob)
                    table.append(profit1)
                    # table.append(profit2)
                    index = index + 1
                    ngay = ngay + 1
            table = np.asarray(table)
            shape = (int(len(table) / 7), 7)
            table = table.reshape(shape)
            f = np.size(table, 0)
            table = pd.DataFrame(table)
            table.columns = ['Parrot', 'Days', 'Lose', 'Win', 'Total', 'Prob', 'Profit1']
            table.insert(0, "Province", "TT", True)
            table.insert(1, "Local", self.display_bet(event), True)
            name2 = '50'
            table.insert(7, "Ar.Length", name2, True)
            print('')
                #print('Table of number of days corresponding with '+ str(event) + name)
            print(table)

    def display(self):
        # self.readFile()
        self.getQueue()


# run = parrot_r()
# run.display()
