import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QDesktopWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Storage")
        self.setGeometry(0, 0, 600, 600)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.initUI()

    def initUI(self):
        button = QPushButton("Add", self)
        button.setToolTip("Adds a record to the password database")
        button.move(15, 10)
        button.clicked.connect(self.on_click)

        button2 = QPushButton("Settings", self)
        button2.setToolTip("Change your settings")
        button2.move(510, 10)
        button2.clicked.connect(self.on_click2)

        self.show()

    @pyqtSlot()
    def on_click2(self):
        print("Entered settings window!")

    @pyqtSlot()
    def on_click(self):
        print("Added a record!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())