import sqlite3
import random
import os
import re
import math

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QWidget, QAction, QRadioButton, QMessageBox, \
    QPushButton, QLineEdit, QLabel, QFileDialog, QTextEdit
from PyQt5.QtGui import QIcon, QPalette, QBrush, QImage, QPixmap, QColor
from PyQt5.QtCore import QSize


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.database()
        self.database2()

    def initUI(self):

        self.setFixedSize(900, 900)
        self.style = "border:2px solid green; color: blue"
        self.label1 = QLabel(self)
        self.label1.setFixedSize(280, 350)
        self.label1.move(100, 250)
        self.label1.setStyleSheet(self.style)

        self.button_1 = QPushButton("SHOW DATA", self)
        self.button_1.setGeometry(400, 280, 150, 40)
        self.button_1.clicked.connect(self.putItem)

        self.button_2 = QPushButton("LARGE LETTERS", self)
        self.button_2.setGeometry(400, 320, 150, 40)
        self.button_2.clicked.connect(self.bigLetters)

        self.button_3 = QPushButton("> AVER. NUMBERS", self)
        self.button_3.setGeometry(400, 360, 150, 40)
        self.button_3.clicked.connect(self.moreThenAverageNumber)

        self.button_4 = QPushButton("RUN", self)
        self.button_4.setGeometry(200, 200, 150, 40)
        self.button_4.clicked.connect(self.run)

        self.textedit_1=QTextEdit('Address:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 70, 90, 30)

        self.textedit_1=QTextEdit('# connections:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 100, 90, 30)

        self.textedit_1=QTextEdit('# tries:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 130, 90, 30)

        self.textedit_1=QTextEdit('-w:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 160, 90, 30)

        self.lineedit_1 = QLineEdit(self)
        self.lineedit_1.move(100, 70)
        self.lineedit_1.setGeometry(200, 70, 220, 30)

        self.lineedit_2 = QLineEdit( self)
        self.lineedit_2.move(100, 70)
        self.lineedit_2.setGeometry(200, 100, 220, 30)

        self.lineedit_3 = QLineEdit(self)
        self.lineedit_3.move(100, 70)
        self.lineedit_3.setGeometry(200, 130, 220, 30)

        self.lineedit_4 = QLineEdit(self)
        self.lineedit_4.move(100, 70)
        self.lineedit_4.setGeometry(200, 160, 220, 30)

    def run(self):
        self.address = str(self.lineedit_1.text())
        self.concurent_connections = str(self.lineedit_2.text())
        self.number_of_requests = str(self.lineedit_3.text())
        self.timelimit = str(self.lineedit_4.text())
        self.timeout = str(self.lineedit_5.text())
        self.cookie = str(self.lineedit_6.text())
        self.basic_auth = str(self.lineedit_7.text())
        self.arbitary_header = str(self.lineedit_8.text())
        self.content_type = str(self.lineedit_9.text())
        os.system("ab -n "+ self.number_of_requests + " -c " + self.concurent_connections + " " + self.address)
        self.show()

    def buttonReply(self):
        buttonReplyD = QMessageBox.question(self, 'PyQt5 message', "Please choose DB!", QMessageBox.Ok)
        if buttonReplyD == QMessageBox.Ok:
            print('Ok clicked.')
        self.show()

    def database(self):
        try:
            os.remove("database.db")
        except:
            pass
        self.conn = sqlite3.connect('database.db')

        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS TEST (                   
                    id INTEGER PRIMARY KEY AUTOINCREMENT, line1 string, line2 string)
                    """)
        self.cursor.execute("""INSERT INTO TEST(line1, line2) VALUES (?,?)""", ('123678', 'Data_db1'))

        self.conn.commit()

        self.cursor.execute("""INSERT INTO TEST(line1, line2) VALUES (?,?)""", ('123', 'GlobalDJ'))

        self.conn.commit()
        self.conn.close()

    def database2(self):
        try:
            os.remove("database2.db")
        except:
            pass

        self.conn = sqlite3.connect('database2.db')

        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS TEST (                   
                    id INTEGER PRIMARY KEY AUTOINCREMENT, line1 string, line2 string)
                    """)
        self.cursor.execute("""INSERT INTO TEST(line1, line2) VALUES (?,?)""", ('45s', 'DataDB_2'))

        self.conn.commit()

        self.cursor.execute("""INSERT INTO TEST(line1, line2) VALUES (?,?)""", ('456', 'Globalsyski'))

        self.conn.commit()
        self.conn.close()

    def comb(self, ind):

        if ind == 0:
            self.radiobutton()
            self.stat_indicator = 0
            try:
                self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                self.AllList = list(self.cursor.fetchall())
            except:
                self.AllList = []
            print(' self.numbersList:', self.AllList)
            self.k2 = ''
            for self.i in self.AllList:
                self.k2 += str(self.i) + ' '
            self.k2 = re.sub('[\[\]\,\'()]', '', str(self.k2))
            self.AllList = list(self.k2.split())
            print('self.numbersList: ', self.AllList)
            self.line1_row = []
            for self.i in self.AllList:
                self.line1_row.append(self.i)
        elif ind == 1:
            self.radiobutton()
            self.stat_indicator = 1
            try:
                self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                self.numbersList = list(self.cursor.fetchall())
            except:
                self.numbersList = []
            print(' self.numbersList:', self.numbersList)
            self.k2 = ''
            for self.i in self.numbersList:
                self.k2 += str(self.i) + ' '
            self.k2 = re.sub('[\[\]\,\'()]', '', str(self.k2))
            self.numbersList = list(self.k2.split())
            print('self.numbersList: ', self.numbersList)
            self.line1_row = []
            for self.i in self.numbersList:
                try:
                    int(self.i)
                    self.line1_row.append(int(self.i))
                except:
                    pass
        elif ind == 2:
            self.radiobutton()
            self.stat_indicator = 2
            try:
                self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                self.stringList = list(self.cursor.fetchall())
                print('self.stringList(1st after select from db): ', self.stringList)
            except:
                self.stringList = []
            self.k2 = ''
            for self.i in self.stringList:
                print('self.i', self.i)
                self.k2 += str(self.i) + ' '
            print('self.k2', self.k2)
            self.k2 = re.sub('[\[\],\'()]', '', str(self.k2))
            self.stringList = list(self.k2.split())
            print('self.stringList: ', self.stringList)
            self.line1_row = []
            for self.i in self.stringList:
                try:
                    int(self.i)
                except:
                    self.line1_row.append(self.i)
                    pass
        elif ind == 3:
            self.radiobutton()
            self.stat_indicator = 3
            try:
                self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                self.numbersList = list(self.cursor.fetchall())
            except:
                self.numbersList = []
            self.k2 = ''
            for self.i in self.numbersList:
                self.k2 += str(self.i) + ', '
            self.k2 = re.sub('[\[\],\'()]', '', str(self.k2))
            self.numbersList = list(self.k2.split())
            print('self.numbersList: ', self.numbersList)
            self.line1_row = []
            self.numbers = 0
            self.texts = 0
            for self.i in self.numbersList:
                try:
                    if int(self.i) / int(self.i) == 1:
                        self.numbers += 1
                except:
                    self.texts += 1
                    pass
            self.line1_row = 'Numbers in DB: ' + str(self.numbers) + "\n" + 'String values in DB: ' + str(self.texts)
            self.line1_row = list(self.line1_row)

    def comb2(self, ind):
        if ind == 0:
            self.style = " background-color : red; border:2px solid green; color: blue"
            self.label1.setStyleSheet(self.style)

##sort
        elif ind == 1:
# all data
            self.radiobutton()
            if self.stat_indicator == 0:
                try:
                    self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                    self.AllList = list(self.cursor.fetchall())
                except:
                    self.AllList = []
                print(' self.numbersList:', self.AllList)
                self.k2 = ''
                for self.i in self.AllList:
                    self.k2 += str(self.i) + ' '
                self.k2 = re.sub('[\[\]\,\'()]', '', str(self.k2))
                self.AllList = list(self.k2.split())
                print('self.numbersList: ', self.AllList)
                self.line1_row = []
                for self.i in self.AllList:
                    self.line1_row.append(self.i)

                self.line1_row.sort()
## numbers
            elif self.stat_indicator == 1:
                self.radiobutton()
                try:
                    self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                    self.sortList = list(self.cursor.fetchall())
                except:
                    self.sortList = []
                print(' self.sortList:', self.sortList)
                self.k2 = ''
                for self.i in self.sortList:
                    self.k2 += str(self.i) + ' '
                self.k2 = re.sub('[\[\]\,\'()]', '', str(self.k2))
                print('self.k2 ', self.k2)
                self.sortList = list(self.k2.split())
                print('self.sortList: ', self.sortList)
                self.line1_row = []
                for self.i in self.sortList:
                    try:
                        int(self.i)
                        self.line1_row.append(int(self.i))
                    except:
                        pass

                self.line1_row.sort()
## text
            elif  self.stat_indicator == 2:
                self.radiobutton()
                self.stat_indicator = 2
                try:
                    self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                    self.stringList = list(self.cursor.fetchall())
                    print('self.stringList(1st after select from db): ', self.stringList)
                except:
                    self.stringList = []
                self.k2 = ''
                for self.i in self.stringList:
                    print('self.i', self.i)
                    self.k2 += str(self.i) + ' '
                print('self.k2', self.k2)
                self.k2 = re.sub('[\[\],\'()]', '', str(self.k2))
                self.stringList = list(self.k2.split())
                print('self.stringList: ', self.stringList)
                self.line1_row = []
                for self.i in self.stringList:
                    try:
                        int(self.i)
                    except:
                        self.line1_row.append(self.i)
                        pass
                self.line1_row.sort()


    def bigLetters(self):
        if self.stat_indicator == 0:
            self.radiobutton()
            try:
                self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                self.bigLettersList = list(self.cursor.fetchall())
            except:
                self.bigLettersList = []
            print(' self.bigLettersList:', self.bigLettersList)
            self.k2 = ''
            for self.i in self.bigLettersList:
                self.k2 += str(self.i) + ' '
            self.k2 = re.sub('[\[\]\,\'()]', '', str(self.k2))
            self.bigLettersList = list(self.k2.split())
            print('self.numbersList: ', self.bigLettersList)
            self.line1_row = []
            for word in self.bigLettersList:
                if word[0].isupper():
                    self.line1_row.append(word)

    def moreThenAverageNumber(self):
        if self.stat_indicator == 0:
            self.radiobutton()
            try:
                self.cursor.execute("""SELECT line1,line2 FROM TEST""")
                self.moreAvgNumbersList = list(self.cursor.fetchall())
            except:
                self.moreAvgNumbersList = []
            print(' self.moreAvgNumbersList:', self.moreAvgNumbersList)
            self.k2 = ''
            for self.i in self.moreAvgNumbersList:
                self.k2 += str(self.i) + ' '
                print('self.k2',self.k2)
            self.k2 = re.sub('[\[\]\,\'()]', '', str(self.k2))
            print('self.k2', self.k2)
            self.moreAvgNumbersList = list(self.k2.split())
            print('self.moreAvgNumbersList: ', self.moreAvgNumbersList)
            self.line1_row = []
            self.only_numbers_list = []
            sumOfnumbers = 0
            numbersQuantity =0
            for self.i in self.moreAvgNumbersList:
                print('self.i in moreAvgNumbersList', self.i)
                try:
                    int(self.i)
                    sumOfnumbers+=int(self.i)
                    numbersQuantity+=1
                    self.only_numbers_list.append(self.i)
                except:
                    pass
            print('sumOfnumbers',sumOfnumbers)
            sumOfnumbers=sumOfnumbers/numbersQuantity#find average
            print('self.only_numbers_list',self.only_numbers_list)
            for number in self.only_numbers_list:
                if int(number) > int(sumOfnumbers) or numbersQuantity==1:
                    self.line1_row.append(number)
            print('self.line1_row in avg numbers:',self.line1_row)
            self.stat_indicator == 3#to prvent new row for numbers - switch to 3 for putItem


    def radiobutton(self):
        if self.radiobutton1.isChecked():
            self.conn = sqlite3.connect('database.db')
            self.cursor = self.conn.cursor()
        elif self.radiobutton2.isChecked():
            self.conn = sqlite3.connect('database2.db')
            self.cursor = self.conn.cursor()
        else:
            self.buttonReply()

    def putItem(self):

        self.k = ''
        for self.i in self.line1_row:
            if self.stat_indicator == 3:#works for stistics and > average number button
                self.k += str(self.i)
            else:
                self.k += str(self.i) + '\n'
        self.k = re.sub('[\[\],\'()]', '', str(self.k))
        self.label1.setText(str(self.k))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
