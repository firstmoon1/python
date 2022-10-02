from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QPixmap
import sys,cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np

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
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

class camera(QWidget):
    
    def __init__(self,tt):
        super(camera,self).__init__()
        
        self.display_width=300
        self.display_height=300
        self.image_label=QLabel(tt)
        self.image_label.move(480,10)
        self.image_label.resize(self.display_width,self.display_height)
        
        self.image_label.setScaledContents(True)
        
        """ # eget tt yi silersen main.py den camera() bu şekilde gönderirsen hbox ile felanda ekrana yansıtabilirsin
        hbox=QHBoxLayout()
        #hbox.addStretch()
        #hbox.addSpacing(300)
        hbox.addWidget(self.image_label)
        self.setLayout(hbox)"""
        
        
        self.thread=VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
    
    def closeEvent(self, event):
        self.thread.stop()
        event.accept()
    
    @pyqtSlot(np.ndarray)      
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

if __name__== "__main__":
    app=QApplication(sys.argv)
    a=camera()
    a.show()
    sys.exit(app.exec_())