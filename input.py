from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton("Ok!", self)
        self.btn.move(100, 50)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(100, 20)

        self.lbl1 = QLabel("Answer", self)
        self.lbl1.move(300, 300)

        self.setGeometry(100, 100, 1000, 500)
        self.setWindowTitle("Window")
        self.show()

    def showDialog(self):

        text, ok = QInputDialog.getText(self, "Answer", "Hi")

        if ok:
            self.le.setText(str(text))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
