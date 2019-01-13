from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel
import sys
import random

a = {"dictionary":"jisho","you":"anata","to hear":"kiku","stairs":"kaidan","white":"shiro"}

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.count = 0

        self.setup_dictionary()
        
        self.lbl2 = QLabel(self)
        
        self.btn = QPushButton("Ok!", self)
        self.btn.move(100, 50)
        self.btn.clicked.connect(self.clicked)

        self.le = QLineEdit(self)
        self.le.move(100, 20)
        
        self.lbl1 = QLabel(self.keys[self.count], self)
        self.lbl1.move(300, 300)

        self.setGeometry(100, 100, 1000, 500)
        self.setWindowTitle("Window")
        self.show()

    def clicked(self):
        key = self.keys[self.count]
        
        if (self.le.text() == a[key]):
            self.lbl2.setText("Correct")
            self.lbl2.adjustSize()
            self.lbl2.move(200, 200)
            self.count += 1
            self.lbl1 = QLabel(self.keys[self.count], self)
            self.lbl1.move(300, 300)
            
        else:
            self.lbl2.setText("Incorrect")
            self.lbl2.adjustSize()
            self.lbl2.move(200, 200)

    def setup_dictionary(self):
        self.keys = list(a.keys())
        random.shuffle(self.keys)
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
