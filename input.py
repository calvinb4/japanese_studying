# Calvin Bertoncini

# This program creates a GUI for quizzing.
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel, QShortcut
import sys
#import webbrowser
import random

#a = {"dictionary":"jisho","you":"anata","to hear":"kiku","stairs":"kaidan","white":"shiro"}

file_read = 'genki_2.txt'

with open(file_read,'r') as f:
    f = f.read()
    lines = f.splitlines()
    keys = []
    vals = []
    for line in lines:
        line = line.split(":")
        keys.append(line[0])
        vals.append(line[1])
    dictionary = dict(zip(keys, vals))

missed = {}

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.already_missed = False
        
        font = QtGui.QFont("Times", 16, QtGui.QFont.Normal)
        self.setFont(font)
        
        self.count = 0

        self.setup_dictionary()
        
        self.lbl2 = QLabel(self)

        self.lbl3 = QLabel(self)
        
        self.btn = QPushButton("Ok!", self)
        self.btn.move(100, 50)
        self.btn.clicked.connect(self.clicked)

        self.btn2 = QPushButton("Show answer", self)
        self.btn2.move(100, 85)
        self.btn2.clicked.connect(self.show_answer)

        self.le = QLineEdit(self)
        self.le.move(100, 20)
        
        self.lbl1 = QLabel(self.keys[self.count], self)
        self.lbl1.move(100, 200)
        self.lbl1.adjustSize()

        self.btn3 = QPushButton("Skip question", self)
        self.btn3.move(250, 85)
        self.btn3.clicked.connect(self.skip_question)

        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("Quizzer")
        self.show()

        enter_shortcut = QShortcut(self)
        #enter_shortcut.setContext(Qt.ApplicationShortcut)
        enter_shortcut.setKey(Qt.Key_Return)
        enter_shortcut.activated.connect(self.clicked)
        
        #shortcut = QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter), self)
        #shortcut.activated.connect(self.clicked)

    def clicked(self):
        self.key = self.keys[self.count]
        
        if (self.le.text() == dictionary[self.key]):
            self.already_missed = False
            self.lbl2.setText("Correct")
            self.lbl2.adjustSize()
            self.lbl2.move(100, 150)

            # Resets if at end of dictionary
            if (len(self.keys) == self.count + 1):
                self.print_missed()
            
            self.count += 1
            self.lbl1.setText(self.keys[self.count])
            #self.lbl1.move(300, 300)
            self.lbl1.adjustSize()

            self.lbl3.setText("") # Refreshes answer to null string
            self.le.setText("") # Refreshes input to null string
            
        else:
            self.lbl2.setText("Incorrect")
            self.lbl2.adjustSize()
            self.lbl2.move(100, 150)
            if (self.already_missed == False):
                missed[self.key + "    " + dictionary[self.key]] = self.le.text()
                self.already_missed = True # Otherwise duplicate values in missed

    def setup_dictionary(self):
        self.keys = list(dictionary.keys())
        random.shuffle(self.keys)

    def show_answer(self):
        key = self.keys[self.count]

        self.lbl3.move(100, 110)
        self.lbl3.setMargin(10)
        self.lbl3.setText(dictionary[key])
        self.lbl3.adjustSize()

    def print_missed(self):
        printed_file = open("missed.txt","w+")
        printed_file.write("Missed words:\nEnglish    Correct answer    Your answer\n")
        for i in missed:
            printed_file.write(i+"    "+missed[i]+"\n")

        #webbrowser.open("missed.txt") # Opens missed words

        self.close() # Closes window

    def skip_question(self):
        self.already_missed = False
        self.key = self.keys[self.count]
        if (len(self.keys) == self.count + 1):
                self.print_missed()
        else:
            self.count += 1
            self.lbl1.setText(self.keys[self.count])
            #self.lbl1.move(300, 300)
            self.lbl1.adjustSize()
        
            self.lbl3.setText("") # Refreshes answer to null string
            self.le.setText("") # Refreshes input to null string

            missed[self.key + "    " + dictionary[self.key]] = "Skipped"

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
