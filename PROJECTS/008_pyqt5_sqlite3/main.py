
# bulundugun dosyayı cmd ile ac sonra alltaki satırı yaz  ui -> py için.
# python -m PyQt5.uic.pyuic -x dene3.ui -o dene3.py

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets,QtCore
from dene3 import Ui_Form
from sqlite import *
from PyQt5.uic import loadUi


# login page admin
class Widget1(QWidget):
    
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.func1()
        
    def func1(self):
        layouth = QtWidgets.QHBoxLayout()
        layouth1 = QtWidgets.QHBoxLayout()
        layouth2 = QtWidgets.QHBoxLayout()
        layoutv = QtWidgets.QVBoxLayout()
        btn1 = QtWidgets.QPushButton("widget2 open")
        btn_register = QtWidgets.QPushButton("Admin Register")
        label_name=QtWidgets.QLabel("Name:")
        label_password=QtWidgets.QLabel("Password:")
        self.name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        
        self.name.setText("")
        self.password.setText("")
        btn1.setFixedSize(100,25)
        btn_register.setFixedSize(100,25)
        self.name.setFixedSize(100,25)
        self.password.setFixedSize(100,25)
        
        layouth.addWidget(label_name)
        layouth.addWidget(self.name)
        layouth.addStretch()
        layoutv.addLayout(layouth)
        
        layouth1.addWidget(label_password)
        layouth1.addWidget(self.password)
        layouth1.addStretch()
        layoutv.addLayout(layouth1)
        
        layouth2.addWidget(btn1)
        layouth2.addWidget(btn_register)
        layoutv.addLayout(layouth2)
        
        self.setLayout(layoutv)
        
        btn1.clicked.connect(self.switch)
        btn_register.clicked.connect(self.register_admin)
    
    def register_admin(self):
        self.swin=QWidget()
        self.swin.setWindowTitle("register page")
        self.swin.setGeometry(500,100,500,400)
        
        btn_register1 = QtWidgets.QPushButton("enroll")
        label_name1=QtWidgets.QLabel("Name:")
        label_password1=QtWidgets.QLabel("Password:")
        self.name1 = QtWidgets.QLineEdit()
        self.password1 = QtWidgets.QLineEdit()
        
        layouth = QtWidgets.QHBoxLayout()
        layouth1 = QtWidgets.QHBoxLayout()
        layoutv1 = QtWidgets.QVBoxLayout()
        
        layouth.addWidget(label_name1)
        layouth.addWidget(self.name1)
        layouth.addStretch()
        layoutv1.addLayout(layouth)
        
        layouth1.addWidget(label_password1)
        layouth1.addWidget(self.password1)
        layouth1.addStretch()
        layoutv1.addLayout(layouth1)
        
        btn_register1.setFixedSize(100,25)
        layoutv1.addWidget(btn_register1)
        self.swin.setLayout(layoutv1)
        
        btn_register1.clicked.connect(self.register_admin1)
        self.swin.show()
        
        
    def register_admin1(self):
        data=datas()
        data.Admin_user_enrol(self.name1.text(),self.password1.text())
        data.con.close()
        self.swin.close()
        
        
    
    def switch(self):
        bol=False
        data=datas()
        cheko=data.Admin_check()
        data.con.close()
        print("cheko : ",cheko)
        for i in cheko:
            if self.name.text() == i[0]:
                if  self.password.text() == i[1]:
                    bol = True
                    break
                else:
                    bol = False
        
        if bol:
            self.switch_window.emit()
 
            
class Widget2(QWidget):
    
    switch_window = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.open_func2()
        
    def open_func2(self):
        
        
        self.win1=QWidget()
        self.ui1=Ui_Form()
        self.ui1.setupUi(self.win1)
        
        layout2=QtWidgets.QVBoxLayout()
        self.btn2 = QtWidgets.QPushButton("widget3 open")
        

        self.btn2.setFixedSize(100,25)
        layout2.addWidget(self.win1)
        layout2.addWidget(self.btn2)
        self.setLayout(layout2)
        self.btn2.clicked.connect(self.func2)
        
    def func2(self):
        self.switch_window.emit()

class Widget3(QWidget):
    
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('widget3')
        self.func3()
        
    def func3(self):
        layout3 = QtWidgets.QGridLayout()
        self.btn3 = QtWidgets.QPushButton("widget2 open")
        self.btn3.setFixedSize(100,25)
        layout3.addWidget(QtWidgets.QLabel("hellow ebru"),1,1)
        layout3.addWidget(QtWidgets.QLabel("hellow ceylan"),1,2)
        layout3.addWidget(QtWidgets.QLabel("hellow mahi devran"),1,3)
        layout3.addWidget(QtWidgets.QLabel("hellow omur"),2,1)
        layout3.addWidget(QtWidgets.QLabel("hellow hatice"),2,2)
        layout3.addWidget(self.btn3,2,3)
        self.btn3.clicked.connect(self.switch)
        self.setLayout(layout3)
    
    def switch(self):
        self.switch_window.emit()


class Controller_pages:
    def __init__(self):

        self.widget1=Widget1()
        self.widget2=Widget2()
        self.widget3=Widget3()
        
    # login page
    def show_Widget1(self):
        self.widget1.setWindowTitle("widget1 page")
        self.widget1.setGeometry(200,200,400,400)
        #self.setFixedSize(600,600)
        self.widget1.switch_window.connect(self.show_Widget2)
        self.widget1.show()
        
    def show_Widget2(self):
        self.widget2.setWindowTitle("widget2 page")
        self.widget2.setGeometry(300,200,400,400)
        self.widget2.switch_window.connect(self.show_Widget3)
        self.widget1.close()
        self.widget3.close()
        self.widget2.show()
    
    def show_Widget3(self):
        self.widget3.setWindowTitle("widget3 page")
        self.widget3.setGeometry(400,200,400,400)
        self.widget3.switch_window.connect(self.show_Widget2)
        self.widget1.close()
        self.widget2.close()
        self.widget3.show()
        
       
if __name__ == "__main__":
    
    app=QtWidgets.QApplication(sys.argv)
    main = Controller_pages()
    main.show_Widget1()
    sys.exit(app.exec_())