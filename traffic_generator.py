import sqlite3
import os
import sys
import re
import subprocess

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QMessageBox


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the main window size and style
        self.setFixedSize(900, 970)
        self.style = "border:2px solid green; color: blue"

        # Initialize the label to display data
        self.label1 = QLabel(self)
        self.label1.setFixedSize(500, 650)
        self.label1.move(100, 300)
        self.label1.setStyleSheet(self.style)

        # Initialize buttons and connect them to their respective functions
        self.button_1 = QPushButton("SHOW DATA", self)
        self.button_1.setGeometry(620, 300, 150, 40)
        self.button_1.clicked.connect(self.databaseOutput)

        self.button_4 = QPushButton("RUN", self)
        self.button_4.setGeometry(620, 10, 150, 270)
        self.button_4.clicked.connect(self.run)

        # Create labels and line edits for user inputs
        self.create_labels()
        self.create_lineedits()

    def create_labels(self):
        # Create and position labels for each input field
        labels_info = [
            ("Address:", 10),
            ("Threads:", 40),
            ("№ of requests:", 70),
            ("Time limit:", 100),
            ("Timeout:", 130),
            ("Cookie:", 160),
            ("Basic auth:", 190),
            ("Content-type:", 220),
            ("Arbitrary header:", 250)
        ]
        for text, y in labels_info:
            label = QLabel(self)
            label.setText(text)
            label.setGeometry(70, y, 120, 30)

    def create_lineedits(self):
        # Create and position line edits for each input field
        self.lineedits = []
        for i in range(9):
            lineedit = QLineEdit(self)
            lineedit.setGeometry(200, 10 + 30 * i, 400, 30)
            self.lineedits.append(lineedit)

    def run(self):
        # Prepare database and collect user inputs
        self.database()
        params = [
            ("", self.lineedits[0].text().strip()),  # Address
            ("-c", self.lineedits[1].text().strip()),  # Threads
            ("-n", self.lineedits[2].text().strip()),  # Number of requests
            ("-t", self.lineedits[3].text().strip()),  # Time limit
            ("-s", self.lineedits[4].text().strip()),  # Timeout
            ("-C", self.lineedits[5].text().strip()),  # Cookie
            ("-A", self.lineedits[6].text().strip()),  # Basic auth
            ("-H", self.lineedits[7].text().strip()),  # Content-type
            ("-T", self.lineedits[8].text().strip())   # Arbitrary header
        ]
        args = self.build_command(params)

        # Check platform to determine the command name
        ab = "abs" if str(sys.platform) == 'win32' else "ab"

        # Remove output file if it exists
        try:
            os.remove("output.txt")
        except FileNotFoundError:
            pass

        # Run the command and capture the output
        command = [ab] + args
        print('run_command', ' '.join(command))
        subprocess.run(command, stdout=open('output.txt', 'w'), check=True)

        # Process the output from the command
        self.process_output()

    def build_command(self, params):
        # Build the command from the given parameters
        command = []
        for flag, value in params:
            if value:
                if flag:
                    command.extend([flag, value])
                else:
                    command.append(value)
        return command

    def process_output(self):
        # Process the output file and store data in the database
        count = 0
        with open('output.txt') as self.file:
            for line in self.file:
                print('line: ', line)
                print('length line: ', len(line))
                count += 1
                if 7 < count < 28 and len(line) > 1:
                    self.data_list = list(map(str.strip, line.split(':')))
                    self.databaseFilling()

        # Display the output in the label
        with open('output.txt', 'r') as file:
            data = file.read()
            self.label1.setText(str(data))

        self.show()

    def buttonReply(self):
        # Display a message box for user interaction
        buttonReplyD = QMessageBox.question(self, 'PyQt5 message', "Please choose DB!", QMessageBox.Ok)
        if buttonReplyD == QMessageBox.Ok:
            print('Ok clicked.')
        self.show()

    def database(self):
        # Create a new SQLite database and table
        try:
            os.remove("database.db")
        except FileNotFoundError:
            pass
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS TEST (
                                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                definition STRING, 
                                data STRING)""")
        self.conn.commit()
        self.conn.close()

    def databaseFilling(self):
        # Insert data into the SQLite database
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""INSERT INTO TEST(definition, data) VALUES (?,?)""", (self.data_list[0], self.data_list[1]))
        self.conn.commit()
        self.conn.close()

    def databaseOutput(self):
        # Retrieve data from the SQLite database and display it
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""SELECT definition, data FROM TEST""")
        self.DBoutput = list(self.cursor.fetchall())
        print(self.DBoutput)
        self.conn.close()
        self.putItem()

    def putItem(self):
        # Format the database output and set it in the label
        self.k = ''
        for self.i in self.DBoutput:
            self.k += f"{self.i[0]}:          {self.i[1]}\n"
        self.label1.setText(self.k)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
