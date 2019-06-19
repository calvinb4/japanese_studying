# Calvin Bertoncini

# This program creates a GUI for quizzing.
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel, QShortcut, QVBoxLayout, QScrollArea, QHBoxLayout, QScrollBar, QComboBox, QToolButton, QMenu, QCheckBox, QWidgetAction
import sys
#import webbrowser
import random

#a = {"dictionary":"jisho","you":"anata","to hear":"kiku","stairs":"kaidan","white":"shiro"}

#file_read = 'genki_2.txt'
#file_read = "test.py"



class custom_menu(QMenu):
    def actionEvent(self, event):
        super().actionEvent(event)
        self.show()

class Missed_Display(QScrollArea):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        widget = QWidget()
        self.layout = QVBoxLayout(widget)
        #layout.addLayout(box)
        #self.layout.setAlignment(Qt.AlignTop)

        #self.scroll = QScrollBar()
        #self.scroll.setMaximum(900)
        #self.scroll.sliderMoved.connect(self.scroll_move)

        #hbox.addWidget(self.scroll)
        # self.lbl = QLabel(self)
        # self.lbl.move(100,100)
        # self.lbl.setText("hi!")

        font = QtGui.QFont("Times", 16, QtGui.QFont.Normal)
        self.setFont(font)

        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("Missed Words")

        #self.lbl2 = QLabel(self)
        #self.lbl.move(100,200)

        count = 0

        guide = QLabel(self)
        guide.setText("English    Correct answer    Your answer")
        self.layout.addWidget(guide)
        
        for i in window.missed: # window is instance of Window class
            self.setup_one_missed_label(i, count)
            count += 1

        self.setWidget(widget)
        self.setWidgetResizable(True)

    def setup_one_missed_label(self, i, count):
        new = QLabel(self)
        new.move(300,0+20*count)
        new.setText(i + "    " + window.missed[i])
        self.layout.addWidget(new)

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.files_added = []

        
        # Drop down menu

        # Note that this line finds subdirectories as well, so make sure vocab_files only contains files
        files = [f for f in os.listdir("./vocab_files")]
        
        self.setup_dictionary()
        
        
        self.toolbutton = QToolButton(self)
        self.toolbutton.setText("Select Files")
        
        self.toolmenu = custom_menu(self)
        for i in files:
            #self.checkbox = QCheckBox(i, self.toolmenu)
            #self.checkbox.filename = i
            #self.checkbox.stateChanged.connect(self.box_check)
            
            #action = self.toolmenu.addAction(str(i))
            #action.setCheckable(True)
            #action = QWidgetAction(self.toolmenu)
            #action.setDefaultWidget(self.checkbox)
            #action.text = i
            #self.toolmenu.addAction(action)
            action = self.toolmenu.addAction(str(i))
            action.setCheckable(True)

        self.toolmenu.triggered.connect(self.menu_trigger)
        self.toolbutton.setMenu(self.toolmenu)
        self.toolbutton.setPopupMode(QToolButton.InstantPopup)
        self.toolbutton.move(250,250)        
        

        #self.missed = {}
        #self.already_missed = False
        
        font = QtGui.QFont("Times", 16, QtGui.QFont.Normal)
        self.setFont(font)
        
        self.count = 0
        
        self.lbl2 = QLabel(self)
        self.lbl2.move(100, 150)

        self.lbl3 = QLabel(self)
        self.lbl3.move(100, 110)
        
        self.btn = QPushButton("Ok!", self)
        self.btn.move(100, 50)
        self.btn.clicked.connect(self.clicked)

        self.btn2 = QPushButton("Show answer", self)
        self.btn2.move(100, 85)
        self.btn2.clicked.connect(self.show_answer)

        self.le = QLineEdit(self)
        self.le.move(100, 20)
        
        if not self.keys:
            self.lbl1 = QLabel("", self)
        else:
            self.lbl1 = QLabel(self.keys[self.count], self)
            
        self.lbl1.move(100, 200)
        self.lbl1.adjustSize()

        self.btn3 = QPushButton("Skip question", self)
        self.btn3.move(250, 85)
        self.btn3.clicked.connect(self.skip_question)

        self.lbl_counter = QLabel(self)
        self.lbl_counter.move(250,150)


        self.start_test = QPushButton("Start!", self)
        self.start_test.move(400,250)
        self.start_test.clicked.connect(self.start_test_method)



        
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("Quizzer")
        self.show()

        enter_shortcut = QShortcut(self)
        #enter_shortcut.setContext(Qt.ApplicationShortcut)
        enter_shortcut.setKey(Qt.Key_Return)
        enter_shortcut.activated.connect(self.clicked)
        
        #shortcut = QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter), self)
        #shortcut.activated.connect(self.clicked)


    def start_test_method(self):
        self.lbl2.setText("")
        self.count = 0
        self.setup_dictionary()

    def menu_trigger(self, action):
        if (action.text() in self.files_added):
            self.files_added.remove(action.text())
        else:
            self.files_added.append(action.text())



    def clicked(self): # Ok button
        
        if not self.keys: # No file selected
            self.lbl2.setText("Select a file.")
            self.lbl2.adjustSize()
            return
        
        self.key = self.keys[self.count]
        
        if (self.le.text() == self.dictionary[self.key]):
            self.already_missed = False
            self.lbl2.setText("Correct")
            self.lbl2.adjustSize()
            self.lbl2.move(100, 150)

            # Resets if at end of dictionary
            if (len(self.keys) == self.count + 1):
                self.print_missed()

            else:
                self.count += 1
                self.lbl1.setText(self.keys[self.count])
                #self.lbl1.move(300, 300)
                self.lbl1.adjustSize()

                self.lbl3.setText("") # Refreshes answer to null string
                self.le.setText("") # Refreshes input to null string

                lbl_counter_text = str(self.count) + "/" + str(len(self.dictionary))
                self.lbl_counter.setText(lbl_counter_text)
                self.lbl_counter.adjustSize()
            
        else:
            self.lbl2.setText("Incorrect")
            self.lbl2.adjustSize()
            self.lbl2.move(100, 150)
            if (self.already_missed == False):
                self.missed[self.key + "    " + self.dictionary[self.key]] = self.le.text()
                self.already_missed = True # Otherwise duplicate values in missed

    def setup_dictionary(self):
        self.missed = {}
        self.already_missed = False
        keys = []
        vals = []
        file_path = "./vocab_files/"
        
        
        for file_read in self.files_added:
            path = file_path + file_read


            try:
                
                with open(path,'r') as f:
                    f = f.read()
                    lines = f.splitlines()
                    #keys = []
                    #vals = []
                    for line in lines:
                        line = line.split(":")
                        keys.append(line[0])
                        vals.append(line[1])

            except IsADirectoryError:
                self.lbl2.setText("Error, please select a valid file.")
                self.lbl2.adjustSize()
                
        self.dictionary = dict(zip(keys, vals))
        
        self.keys = list(self.dictionary.keys())
        random.shuffle(self.keys)

        if self.keys:
            self.lbl1.setText(self.keys[0])
            self.lbl1.adjustSize()

        
    def show_answer(self):

        if not self.keys:
            self.lbl2.setText("Select a file.")
            self.lbl2.adjustSize()
            return
        
        key = self.keys[self.count]

        self.lbl3.move(100, 110)
        self.lbl3.setMargin(10)
        self.lbl3.setText(self.dictionary[key])
        self.lbl3.adjustSize()

    def print_missed(self):
        #printed_file = open("missed.txt","w+")
        #printed_file.write("Missed words:\nEnglish    Correct answer    Your answer\n")
        #for i in missed:
        #    printed_file.write(i+"    "+missed[i]+"\n")

        #webbrowser.open("missed.txt") # Opens missed words

        #self.close() # Closes window

        
        self.new_window = Missed_Display()
        self.new_window.show()

    def skip_question(self):
        self.already_missed = False

        if not self.keys:
            self.lbl2.setText("Select a file.")
            self.lbl2.adjustSize()
            return
        
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

            self.missed[self.key + "    " + self.dictionary[self.key]] = "Skipped"

    def return_missed(self):
        return self.missed

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
