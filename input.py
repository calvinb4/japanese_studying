# Calvin Bertoncini

# This program creates a GUI for quizzing.

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel
import sys
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

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.count = 0

        self.setup_dictionary()
        
        self.lbl2 = QLabel(self)

        self.lbl3 = QLabel(self)
        
        self.btn = QPushButton("Ok!", self)
        self.btn.move(100, 50)
        self.btn.clicked.connect(self.clicked)

        self.btn2 = QPushButton("Show answer", self)
        self.btn2.move(100, 75)
        self.btn2.clicked.connect(self.show_answer)

        self.le = QLineEdit(self)
        self.le.move(100, 20)
        
        self.lbl1 = QLabel(self.keys[self.count], self)
        self.lbl1.move(100, 200)
        self.lbl1.adjustSize()

        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("Quizzer")
        self.show()

    def clicked(self):
        key = self.keys[self.count]
        
        if (self.le.text() == dictionary[key]):
            self.lbl2.setText("Correct")
            self.lbl2.adjustSize()
            self.lbl2.move(100, 150)

            # Resets if at end of dictionary
            if (len(self.keys) == self.count + 1):
                self.count = -1
            
            self.count += 1
            self.lbl1.setText(self.keys[self.count])
            #self.lbl1.move(300, 300)

            self.lbl3.setText("") # Refreshes answer to null string
            
        else:
            self.lbl2.setText("Incorrect")
            self.lbl2.adjustSize()
            self.lbl2.move(100, 150)

    def setup_dictionary(self):
        self.keys = list(dictionary.keys())
        random.shuffle(self.keys)

    def show_answer(self):
        key = self.keys[self.count]

        self.lbl3.move(100, 85)
        self.lbl3.setMargin(10)
        self.lbl3.setText(dictionary[key])
        self.lbl3.adjustSize()     

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
