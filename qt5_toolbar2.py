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

        self.setFixedSize(900, 930)
        self.style = "border:2px solid green; color: blue"
        self.label1 = QLabel(self)
        self.label1.setFixedSize(550, 645)
        self.label1.move(100, 280)
        self.label1.setStyleSheet(self.style)

        self.button_1 = QPushButton("SHOW DATA", self)
        self.button_1.setGeometry(650, 280, 150, 40)
        self.button_1.clicked.connect(self.databaseOutput)

        self.button_2 = QPushButton("LARGE LETTERS", self)
        self.button_2.setGeometry(650, 320, 150, 40)
        self.button_2.clicked.connect(self.run)

        self.button_3 = QPushButton("> AVER. NUMBERS", self)
        self.button_3.setGeometry(650, 360, 150, 40)
        self.button_3.clicked.connect(self.run)

        self.button_4 = QPushButton("RUN", self)
        self.button_4.setGeometry(650, 200, 150, 40)
        self.button_4.clicked.connect(self.run)

        self.textedit_1 = QTextEdit('Address:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 10, 120, 30)

        self.textedit_1 = QTextEdit('Threads:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 40, 120, 30)

        self.textedit_1 = QTextEdit('# of requests:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 70, 120, 30)

        self.textedit_1 = QTextEdit('Time limit:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 100, 120, 30)

        self.textedit_1 = QTextEdit('Timeout:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 130, 120, 30)

        self.textedit_1 = QTextEdit('Cookie:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 160, 120, 30)

        self.textedit_1 = QTextEdit('Basic auth:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 190, 120, 30)

        self.textedit_1 = QTextEdit('Content-type:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 220, 120, 30)

        self.textedit_1 = QTextEdit('Arbitary header:', self)
        self.textedit_1.move(50, 50)
        self.textedit_1.setGeometry(100, 250, 120, 30)

        self.lineedit_1 = QLineEdit(self)
        self.lineedit_1.move(100, 70)
        self.lineedit_1.setGeometry(200, 10, 220, 30)

        self.lineedit_2 = QLineEdit(self)
        self.lineedit_2.move(100, 70)
        self.lineedit_2.setGeometry(200, 40, 220, 30)

        self.lineedit_3 = QLineEdit(self)
        self.lineedit_3.move(100, 70)
        self.lineedit_3.setGeometry(200, 70, 220, 30)

        self.lineedit_4 = QLineEdit(self)
        self.lineedit_4.move(100, 70)
        self.lineedit_4.setGeometry(200, 100, 220, 30)

        self.lineedit_5 = QLineEdit(self)
        self.lineedit_5.move(100, 70)
        self.lineedit_5.setGeometry(200, 130, 220, 30)

        self.lineedit_6 = QLineEdit(self)
        self.lineedit_6.move(100, 70)
        self.lineedit_6.setGeometry(200, 160, 220, 30)

        self.lineedit_7 = QLineEdit(self)
        self.lineedit_7.move(100, 70)
        self.lineedit_7.setGeometry(200, 190, 220, 30)

        self.lineedit_8 = QLineEdit(self)
        self.lineedit_8.move(100, 70)
        self.lineedit_8.setGeometry(200, 220, 220, 30)

        self.lineedit_9 = QLineEdit(self)
        self.lineedit_9.move(100, 70)
        self.lineedit_9.setGeometry(200, 250, 220, 30)

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

        if str(sys.platform) == 'win32':  # checking os version, for windows we need to use abs instead of ab
            ab = "abs -n "
        else:
            ab = "ab -n "
        run_command = ab + self.number_of_requests + " -c " + self.concurent_connections + " " + self.address + " > output.txt && exit 0"
        print('run_command', run_command)
        os.system(run_command)
        count = 0

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

        self.file.close

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

        self.putItem()

    def putItem(self):

        self.k = ''
        for self.i in self.DBoutput:
            self.k += str(self.i) + '\n'
        self.k = re.sub('[\[\]\'()]', '', str(self.k))
        self.k = re.sub('[,]', ':          ', str(self.k))  # adding :
        self.label1.setText(str(self.k))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
