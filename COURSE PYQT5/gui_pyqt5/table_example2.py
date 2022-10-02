import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("dene3.ui",self)
        self.table.setColumnWidth(0,250)
        self.table.setColumnWidth(1,100)
        self.table.setColumnWidth(2,350)
        self.loaddata()

    def loaddata(self):
        people=[{"name":"John","age":45,"address":"New York"}, {"name":"Mark", "age":40,"address":"LA"},
                {"name":"George","age":30,"address":"London"}]
        row=0
        self.table.setRowCount(len(people))
        for person in people:
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(person["name"]))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["age"])))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(person["address"]))
            row=row+1



# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")