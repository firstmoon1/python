
"""
cap_dshow için linkler  üstte
https://www.codegrepper.com/code-examples/python/cap+%3D+cv2.VideoCapture%280%29+open+web+cam
https://www.reddit.com/r/learnpython/comments/oxo3gd/why_do_i_have_to_use_cv2cap_dshow/
There was a change in cv2 library and now you have to specify the video source (for example cv2.CAP_DSHOW on Windows).
Whereas in former times there was just the only one source available or systems default was used. I guess this was the DirectShow device in Windows anyways.
When you see "old" code example, just remember to add the source device parameter.

python self.change_pixmap_signal.emit   için bakmıstım bunu verdi google genel olarak gui ile cv2 beraber sıkıntılı calışıyormus bu yöntem ile calışırmıs etc. tam net bilmiyorum
https://gist.github.com/docPhil99/ca4da12c9d6f29b9cea137b617c7b8b1
"""
# importing libraries
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys,os
import cv2
import numpy as np
import io
import folium


class VideoThread(QThread): #bu thread  gui donmasın diye yazılmıs,bir tuşa bastın o tus görevini bitirene kadar gui donar bunun olmaması için yazılır
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret: self.change_pixmap_signal.emit(cv_img)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
        # setting geometry
        self.setGeometry(100, 100, 640, 480)
        # calling methods
        self.UiComponents()

    # method for widgets

    def UiComponents(self):


        # --------------------------------------------------------#
        #label2 = QLabel(self)
        #pixmap2 = QPixmap('image2.png')
        #label2.setPixmap(pixmap2)
        #label2.setGeometry(0, 0, pixmap2.width(), pixmap2.height())
        # --------------------------------------------------------#
        #label = QLabel(self)
        #pixmap = QPixmap('image.png')
        #label.setPixmap(pixmap)
        #label.setGeometry(0 + 10, 0, pixmap.width(), pixmap.height())
        # --------------------------------------------------------#

        # -------Map Elements--------#


        webView = QWebEngineView(self)
        webView.setGeometry(300, 10, 300, 300) # map in konumu x,y, width,height
        # coordinate = (37.8199286, -122.4782551) # usa da bir yer
        coordinate = (41.005858, 29.009490)
        m = folium.Map(tiles='Stamen Terrain', zoom_start=13, location=coordinate)

        """
        folium.Marker(
            location=coordinate, # coordinates for the marker (Earth Lab at CU Boulder)
            popup='aradıgın yer gülüm.', # pop-up label for the marker
            #icon=folium.Icon()   # icon degiştirme
            icon=folium.Icon(color='lightgray', icon='plane', prefix='fa')
            ).add_to(m)"""
        
        folium.Circle(
            radius=100,
            location=coordinate,
            popup="The Waterfront",
            color="crimson",
            fill=False,
        ).add_to(m)

        folium.CircleMarker(
            location=coordinate,
            radius=50,
            popup="Laurelhurst Park",
            color="#3186cc",
            fill=True,
            fill_color="#3186cc",
        ).add_to(m)

        
        # save map
        data = io.BytesIO()
        m.save(data, close_file=False)
        webView.setHtml(data.getvalue().decode())

        # -------Map Elements--------#

        #-------Video Elements--------#
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0,300, 300)
        self.image_label.setContentsMargins(10, 0, 10, 10) # edgelerden bırakılan boşluklar

        #gui üzerindeki boyut ve konum belirler
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
        # -------Video Elements--------#




        # creating a push button
        button = QPushButton("CLICK", self)
        button.setGeometry(50, 300 + 25, 100, 40)

        button2 = QPushButton("CLICK2", self)
        button2.setGeometry(200, 300 + 25, 100, 40)

        # adding action to a button
        button.clicked.connect(self.clickme)
        button2.clicked.connect(self.clickme)

    def clickme(self):
        # printing pressed
        print("pressed")

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        #burdaki değişkenler videonun çözünürlüğünü belirler
        #video elementin içindekiler ise videnun ne kadarının
        #gösterileceğini söyler(guide kapladığı yer)
        p = convert_to_Qt_format.scaled(350, 300, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
if __name__=="__main__":
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
