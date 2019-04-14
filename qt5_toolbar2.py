import sqlite3, os, sys, re

from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QWidget, QAction, QRadioButton, QMessageBox, \
    QPushButton, QLineEdit, QLabel, QFileDialog, QTextEdit
from PyQt5.QtGui import QIcon, QPalette, QBrush, QImage, QPixmap, QColor
from PyQt5.QtCore import QSize


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setFixedSize(900, 970)
        self.style = "border:2px solid green; color: blue"
        self.label1 = QLabel(self)
        self.label1.setFixedSize(500, 650)
        self.label1.move(100, 300)
        self.label1.setStyleSheet(self.style)

        self.button_1 = QPushButton("SHOW DATA", self)
        self.button_1.setGeometry(620, 300, 150, 40)
        self.button_1.clicked.connect(self.databaseOutput)

        self.button_4 = QPushButton("RUN", self)
        self.button_4.setGeometry(620, 10, 150, 270)
        self.button_4.clicked.connect(self.run)

        self.lbl1 = QLabel(self)
        self.lbl1.setText("Address:")
        self.lbl1.adjustSize()
        self.lbl1.move(50, 50)
        self.lbl1.setGeometry(70, 10, 120, 30)

        self.lbl2 = QLabel(self)
        self.lbl2.setText("Threads:")
        self.lbl2.adjustSize()
        self.lbl2.move(50, 50)
        self.lbl2.setGeometry(70, 40, 120, 30)

        self.lbl3 = QLabel(self)
        self.lbl3.setText("№ of requests:")
        self.lbl3.adjustSize()
        self.lbl3.move(50, 50)
        self.lbl3.setGeometry(70, 70, 120, 30)

        self.lbl4 = QLabel(self)
        self.lbl4.setText("Time limit:")
        self.lbl4.adjustSize()
        self.lbl4.move(50, 50)
        self.lbl4.setGeometry(70, 100, 120, 30)

        self.lbl5 = QLabel(self)
        self.lbl5.setText("Timeout:")
        self.lbl5.adjustSize()
        self.lbl5.move(50, 50)
        self.lbl5.setGeometry(70, 130, 120, 30)

        self.lbl6 = QLabel(self)
        self.lbl6.setText("Cookie:")
        self.lbl6.adjustSize()
        self.lbl6.move(50, 50)
        self.lbl6.setGeometry(70, 160, 120, 30)

        self.lbl7 = QLabel(self)
        self.lbl7.setText("Basic auth:")
        self.lbl7.adjustSize()
        self.lbl7.move(50, 50)
        self.lbl7.setGeometry(70, 190, 120, 30)

        self.lbl8 = QLabel(self)
        self.lbl8.setText("Content-type:")
        self.lbl8.adjustSize()
        self.lbl8.move(50, 50)
        self.lbl8.setGeometry(70, 220, 120, 30)

        self.lbl9 = QLabel(self)
        self.lbl9.setText("Arbitary header:")
        self.lbl9.adjustSize()
        self.lbl9.move(50, 50)
        self.lbl9.setGeometry(70, 250, 120, 30)

        self.lineedit_1 = QLineEdit(self)
        self.lineedit_1.move(100, 70)
        self.lineedit_1.setGeometry(200, 10, 400, 30)

        self.lineedit_2 = QLineEdit(self)
        self.lineedit_2.move(100, 70)
        self.lineedit_2.setGeometry(200, 40, 400, 30)

        self.lineedit_3 = QLineEdit(self)
        self.lineedit_3.move(100, 70)
        self.lineedit_3.setGeometry(200, 70, 400, 30)

        self.lineedit_4 = QLineEdit(self)
        self.lineedit_4.move(100, 70)
        self.lineedit_4.setGeometry(200, 100, 400, 30)

        self.lineedit_5 = QLineEdit(self)
        self.lineedit_5.move(100, 70)
        self.lineedit_5.setGeometry(200, 130, 400, 30)

        self.lineedit_6 = QLineEdit(self)
        self.lineedit_6.move(100, 70)
        self.lineedit_6.setGeometry(200, 160, 400, 30)

        self.lineedit_7 = QLineEdit(self)
        self.lineedit_7.move(100, 70)
        self.lineedit_7.setGeometry(200, 190, 400, 30)

        self.lineedit_8 = QLineEdit(self)
        self.lineedit_8.move(100, 70)
        self.lineedit_8.setGeometry(200, 220, 400, 30)

        self.lineedit_9 = QLineEdit(self)
        self.lineedit_9.move(100, 70)
        self.lineedit_9.setGeometry(200, 250, 400, 30)

    def run(self):
        self.database()

        self.address = str(self.lineedit_1.text())
        if self.address != "":
            self.address = " " + self.address

        self.concurent_connections = str(self.lineedit_2.text())
        if self.concurent_connections != "":
            self.concurent_connections = " -c " + self.concurent_connections

        self.number_of_requests = str(self.lineedit_3.text())
        if self.number_of_requests != "":
            self.number_of_requests = " -n " + self.number_of_requests

        self.timelimit = str(self.lineedit_4.text())
        if self.timelimit != "":
            self.timelimit = " -t " + self.timelimit

        self.timeout = str(self.lineedit_5.text())
        if self.timeout != "":
            self.timeout = " -s " + self.timeout

        self.cookie = str(self.lineedit_6.text())
        if self.cookie != "":
            self.cookie = " -C " + self.cookie

        self.basic_auth = str(self.lineedit_7.text())
        if self.basic_auth != "":
            self.basic_auth = " -A " + self.basic_auth

        self.arbitary_header = str(self.lineedit_8.text())
        if self.arbitary_header != "":
            self.arbitary_header = " -T " + self.arbitary_header

        self.content_type = str(self.lineedit_9.text())
        if self.content_type != "":
            self.content_type = " -H \"" + self.content_type + "\""
        else:
            self.content_type = self.content_type.split(',')
            for self.i in self.content_type:
                self.content_type += " -H \"" + self.i + "\""
            print(self.content_type)

        if str(sys.platform) == 'win32':  # checking os version, for windows we need to use abs instead of ab
            ab = "abs"
        else:
            ab = "ab"
        try:
            os.remove("output.txt")
        except:
            pass
        run_command = ab + self.number_of_requests + self.timelimit + self.basic_auth + self.arbitary_header + self.cookie + self.content_type + self.timeout + self.concurent_connections + self.address + " > output.txt && exit 0"
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
