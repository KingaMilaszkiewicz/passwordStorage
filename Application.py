import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QDesktopWidget

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Storage")
        self.setGeometry(0, 0, 600, 600)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())