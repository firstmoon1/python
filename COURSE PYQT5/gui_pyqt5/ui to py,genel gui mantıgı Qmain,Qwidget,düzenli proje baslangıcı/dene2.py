
# bulundugun dosyayı cmd ile ac sonra alltaki satırı yaz  ui -> py için.
# python -m PyQt5.uic.pyuic -x dene2.ui -o dene2.py



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.btn_yaz = QtWidgets.QPushButton(Form)
        self.btn_yaz.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.btn_yaz.setObjectName("btn_yaz")
        self.btn_clear = QtWidgets.QPushButton(Form)
        self.btn_clear.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.btn_clear.setObjectName("btn_clear")
        self.message = QtWidgets.QLabel(Form)
        self.message.setGeometry(QtCore.QRect(70, 90, 241, 51))
        self.message.setText("")
        self.message.setObjectName("message")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btn_yaz.clicked.connect(self.yaz)
        self.btn_clear.clicked.connect(self.temiz)

    def yaz(self):
        self.message.setText("sen olmak kral reis")
        
    def temiz(self):
        self.message.clear()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dene2"))
        self.btn_yaz.setText(_translate("Form", "yaz"))
        self.btn_clear.setText(_translate("Form", "clear"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
