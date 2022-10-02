
from PyQt5 import QtWidgets,uic,QtGui
import sys,cv2,io
from PyQt5.QtWidgets import  QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from dene2 import Ui_Form
from opencv_gui import camera,VideoThread

""" # opencv kamerayı hem burdan tek python file inde denedim calıştı hemde opencv_gui.py den calıştırdım burda inheritledim
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()
    
    def stop(self):
        #Sets run flag to False and waits for thread to finish
        self._run_flag = False
        self.wait()


class camera(QWidget):
    
    def __init__(self):
        super().__init__()
        self.display_width=300
        self.display_height=300
        self.image_label=QLabel(self)
        self.image_label.resize(self.display_width,self.display_height)
              
        
        hbox=QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.image_label)
        self.setLayout(hbox)
        
        
        self.thread=VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
    
    def closeEvent(self, event):
        self.thread.stop()
        event.accept()
    
    @pyqtSlot(np.ndarray)      
    def update_image(self, cv_img):
        #Updates the image_label with a new opencv image 
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        #Convert from an opencv image to QPixmap
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
"""


class widget1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #uic.loadUi("dene2.ui",self)
        #self.opendene3()
        self.buttons()
        self.cam()
        
    def cam(self):
        pass
 
    def buttons(self):
        
        self.horizontal_layout=QtWidgets.QHBoxLayout()
        self.vertical_layout=QtWidgets.QVBoxLayout()
        
        self.btn_file=QtWidgets.QPushButton("dene2.py'yi ac")
        self.btn_file.setFixedSize(100,25)
        #self.btn_file.move(100,100)
        #self.btn_file.setText("dene2.py'yi ac")
        
        self.vertical_layout.addStretch()
        self.vertical_layout.addWidget(self.btn_file)
        self.setLayout(self.vertical_layout)

        self.btn_file.clicked.connect(self.open_dene2)

    def open_dene2(self):
        print("monkey1")
        self.window=QtWidgets.QWidget()
        self.elma=Ui_Form()
        self.elma.setupUi(self.window)
        self.window.show()


class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # https://www.pythonguis.com/tutorials/pyqt-layouts/   #önemli
        layout=QVBoxLayout()
        layout.addWidget(camera(self))
        layout.addWidget(widget1())
        
        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        """ # ui dosyasını gui de kullanmayı denedim oldu
        self.widg=camera() # camerayı tek koymayı denedim ,yukarda ise multi widget eklemeyi gördük
        self.setCentralWidget(self.widg)
        #uic.loadUi("dene1.ui",self)
        """
        self.m_function1()
        
    def m_function1(self):
        
        print("monkey0")
        self.setWindowTitle("Main page")
        self.setGeometry(100,100,600,600)
        self.setFixedSize(800,600)
        self.setStyleSheet("QMainWindow {background: 'pink';}")
       

    
    


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main1=mainwindow()
    main1.show()
    sys.exit(app.exec_())


