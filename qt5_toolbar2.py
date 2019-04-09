import sqlite3, os, sys, re

from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QWidget, QAction, QRadioButton, QMessageBox, \
    QPushButton, QLineEdit, QLabel, QFileDialog, QTextEdit
from PyQt5.QtGui import QIcon, QPalette, QBrush, QImage, QPixmap, QColor
from PyQt5.QtCore import QSize


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.database()

    def initUI(self):

        self.setFixedSize(900, 900)
        self.style = "border:2px solid green; color: blue"
        self.label1 = QLabel(self)
        self.label1.setFixedSize(450, 600)
        self.label1.move(100, 250)
        self.label1.setStyleSheet(self.style)

        self.button_1 = QPushButton("SHOW DATA", self)
        self.button_1.setGeometry(550, 280, 150, 40)
        self.button_1.clicked.connect(self.putItem)

        self.button_2 = QPushButton("LARGE LETTERS", self)
        self.button_2.setGeometry(550, 320, 150, 40)
        self.button_2.clicked.connect(self.bigLetters)

        self.button_3 = QPushButton("> AVER. NUMBERS", self)
        self.button_3.setGeometry(550, 360, 150, 40)
        self.button_3.clicked.connect(self.moreThenAverageNumber)

        self.button_4 = QPushButton("RUN", self)
        self.button_4.setGeometry(200, 200, 150, 40)
        self.button_4.clicked.connect(self.run)

        self.textedit_1=QTextEdit('Address:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 70, 120, 30)

        self.textedit_1=QTextEdit('# connects:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 100, 120, 30)

        self.textedit_1=QTextEdit('# tries:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 130, 120, 30)

        self.textedit_1=QTextEdit('-w:',self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 160, 120, 30)

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
        # self.timelimit = str(self.lineedit_4.text())
        # self.timeout = str(self.lineedit_5.text())
        # self.cookie = str(self.lineedit_6.text())
        # self.basic_auth = str(self.lineedit_7.text())
        # self.arbitary_header = str(self.lineedit_8.text())
        # self.content_type = str(self.lineedit_9.text())

        if str(sys.platform) == 'win32':  # checking os version, for windows we need to use abs instead of ab
            ab = "abs -n "
        else:
            ab = "ab -n "
        run_command = ab + self.number_of_requests + " -c " + self.concurent_connections + " " + self.address + " > output.txt && exit 0"
        print('run_command', run_command)
        os.system(run_command)
        count =0

        with open('output.txt') as self.file:
            for line in self.file:
                print('line: ', line)
                print('lenght line: ', len(line))
                count += 1
                if count > 7 and count < 28 and len(line) > 1:  # exclude empty and not nessasary lines
                    self.data_list = list(line.split(':'))
                    self.data_list[-1] = self.data_list[-1].strip()  # removing /n
                    self.data_list = list(self.data_list)
                    print('self.data_list:', self.data_list)
                    print('datalist0:', self.data_list[0])
                    print('datalist1:', self.data_list[1])
                    self.datalist0 = str(self.data_list[0])
                    self.datalist1 = str(self.data_list[1])
                    self.databaseFilling()
        self.databaseOutput()
        self.file.close

        file = open('output.txt', 'r')
        data = file.read()
        self.label1.setText(str(data))

        file = open('output.txt', 'r')
        data = file.read()
        self.label1.setText(str(data))

        self.file.close

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
                    id INTEGER PRIMARY KEY AUTOINCREMENT, definition string, data string)
                    """)


        self.conn.commit()
        self.conn.close()

    def databaseFilling(self):

        self.conn = sqlite3.connect('database.db')

        self.cursor = self.conn.cursor()
        # insert data to table

        self.cursor.execute("""INSERT INTO TEST(definition,data) VALUES (?,?)""", (self.datalist0, self.datalist1,))

        self.conn.commit()

        self.conn.close()

    def databaseOutput(self):

        self.conn = sqlite3.connect('database.db')

        self.cursor = self.conn.cursor()

        self.cursor.execute("""SELECT definition,data FROM TEST""")
        self.DBoutput = list(self.cursor.fetchall())
        print(self.DBoutput)

        self.conn.close()

    def comb(self, ind):
        pass

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
