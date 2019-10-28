import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        button = QPushButton("Add", self)
        button.setToolTip("Adds a record to the password database")
        button.move(15, 10)
        button.clicked.connect(self.on_click)

        button2 = QPushButton("Settings", self)
        button2.setToolTip("Change your settings")
        button2.move(510, 10)
        button2.clicked.connect(self.on_click2)

        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Host Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Email"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Nickname"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Password"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Discord"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("kinga.milaszkiewicz@outlook.com"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("Kinga#6585"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("somePassword"))
        self.tableWidget.move(100, 50)

        self.tableWidget.doubleClicked.connect(self.on_click_table)

    @pyqtSlot()
    def on_click_table(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

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