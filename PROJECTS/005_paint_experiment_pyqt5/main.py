
from PyQt5.QtWidgets import QApplication,QMainWindow,QMenuBar,QMenu,QAction,QFileDialog
from PyQt5.QtGui import QIcon,QImage,QPainter,QPen
from PyQt5.QtCore import Qt,QPoint
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        up_down=100
        left_right=200
        width=700
        height=500
        
        icon="images/paint.jpg"
        
        self.setWindowTitle("Paint Application")
        self.setGeometry(left_right,up_down,width,height)
        self.setWindowIcon(QIcon(icon))
        
        self.image=QImage(self.size(),QImage.Format_RGB32)
        self.image.fill(Qt.white) # by default we are gonna make this white
        
        self.drawing=False
        self.brushSize=2
        self.brushColor=Qt.black
        
        self.lastPoint=QPoint()
        
        mainMenu = self.menuBar()
        fileMenu=mainMenu.addMenu("File")
        brushMenu=mainMenu.addMenu("Brush Size")
        brushColor=mainMenu.addMenu("Brush Color")
        
        # file menu attributes
        saveAction = QAction(QIcon("images/save.jpg"),"Save",self )
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        
        clearAction = QAction(QIcon("images/clear.jpg"),"Clear",self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)        
        clearAction.triggered.connect(self.clear)
        
        
        # brush menu  attributes
        threepxAction = QAction(QIcon("images/brush_size.jpg"),"3px",self)
        threepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(threepxAction)       
        threepxAction.triggered.connect(self.threePx)
        
        fivepxAction = QAction(QIcon("images/brush_size.jpg"),"5px",self)
        fivepxAction.setShortcut("Ctrl+F")
        brushMenu.addAction(fivepxAction) 
        fivepxAction.triggered.connect(self.fivePx)
        
        sevenpxAction = QAction(QIcon("images/brush_size.jpg"),"7px",self)
        sevenpxAction.setShortcut("Ctrl+S")
        brushMenu.addAction(sevenpxAction) 
        sevenpxAction.triggered.connect(self.sevenPx)
        
        ninepxAction = QAction(QIcon("images/brush_size.jpg"),"9px",self)
        ninepxAction.setShortcut("Ctrl+N")
        brushMenu.addAction(ninepxAction) 
        ninepxAction.triggered.connect(self.ninePx)
        
        # brush color  attributes
        blackAction=QAction(QIcon("images/black.png"),"black",self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)
        
        whiteAction=QAction(QIcon("images/white.png"),"white",self)
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.whiteColor)
        
        redAction=QAction(QIcon("images/red.png"),"red",self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)
        
        grayAction=QAction(QIcon("images/gray.png"),"gray",self)
        grayAction.setShortcut("Ctrl+G")
        brushColor.addAction(grayAction)
        grayAction.triggered.connect(self.grayColor)
        
        greenAction=QAction(QIcon("images/green.png"),"green",self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)
        
        yellowAction=QAction(QIcon("images/yellow.png"),"yellow",self)
        yellowAction.setShortcut("Ctrl+G")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)
        
        
    # mouse events.
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: 
            self.drawing = True 
            self.lastPoint =event.pos() # we take position of mouse 

            #print(self.lastPoint) #mouse sag click yaptıgında (x,y) coordination'larını alıyoruz
            
    def mouseMoveEvent(self,event):
        if ( event.buttons() & Qt.LeftButton ) & self.drawing :
            painter=QPainter(self.image  )
            painter.setPen(QPen(self.brushColor,self.brushSize,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin ))
            painter.drawLine(self.lastPoint,event.pos() )
            self.lastPoint=event.pos()
            self.update()
    
    def mouseReleaseEvent(self,event ):
        if (event.buttons() & Qt.LeftButton ):
            self.drawing=False
            
    def paintEvent(self, event):
        canvasPainter=QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image,self.image.rect()  )
        #self.rect() : rectangle demek
    
    
    def save(self):
        filePath , _ = QFileDialog.getSaveFileName( self, "save Image","","PNG(*.png);; JPEG(*jpg *.jpeg);; ALL Files(*.*) " ) 
        if filePath =="":
            return
        self.image.save(filePath)
     
    
    def clear(self):
        self.image.fill(Qt.white)
        self.update() # bunu update etmezsen etki etmez paint tablosuna
        
        
    # brush size
    def threePx(self):
        self.brushSize = 3
    
    def fivePx(self):
        self.brushSize = 5
        
    def sevenPx(self):
        self.brushSize = 7
        
    def ninePx(self):
        self.brushSize = 9
        
        
    # brush color
    
    def blackColor(self):
        self.brushColor = Qt.black
        
    def whiteColor(self):
        self.brushColor = Qt.white
        
    def redColor(self):
        self.brushColor = Qt.red
        
    def yellowColor(self):
        self.brushColor = Qt.yellow
        
    def grayColor(self):
        self.brushColor = Qt.gray
    
    def greenColor(self):
        self.brushColor = Qt.green
    
    
    
       
if __name__ =="__main__":
    app=QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        