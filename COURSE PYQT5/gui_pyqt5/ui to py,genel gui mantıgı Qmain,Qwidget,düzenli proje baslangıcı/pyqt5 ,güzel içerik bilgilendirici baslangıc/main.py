
from PyQt5 import QtWidgets,uic
import sys
from dene2 import Ui_Form

class widget1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #uic.loadUi("dene2.ui",self)
        #self.opendene2()
        self.but()

    def but(self):
        self.btn_file=QtWidgets.QPushButton(self)
        self.btn_file.move(100,100)
        self.btn_file.setText("ac yavrum")

        self.etiket=QtWidgets.QLabel(self) # pencereden yer ayırdık yazı için
        self.etiket.setText("hello world")
        self.etiket.move(100,30) 

        self.btn_file.clicked.connect(self.open)

    def open(self):
        self.open_dene2()   

    def open_dene2(self):
        print("bitches")
        self.window=QtWidgets.QWidget()
        self.elma=Ui_Form()
        self.elma.setupUi(self.window)
        self.window.show()

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widg=widget1()
        self.setCentralWidget(self.widg)
        #uic.loadUi("dene1.ui",self)
        self.m_function1()
        
    def m_function1(self):
        self.setGeometry(100,100,400,300)
        self.show()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main1=mainwindow()
    sys.exit(app.exec_())


