from re import A
from PyQt5.QtWidgets import QApplication,QMainWindow,QMenuBar,QMenu,QAction,QFileDialog
from PyQt5.QtGui import QIcon,QImage,QPainter,QPen
from PyQt5.QtCore import Qt,QPoint
import sys



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        dummy_menu_names=list
        dummy_menu_names=self.main_function_titles_variables()
        self.file_save_actions(dummy_menu_names)
        self.brush_pixels(dummy_menu_names)
        self.brush_colors(dummy_menu_names)
        

    def main_function_titles_variables(self):
        
        up_down,left_right,width,height = 100,200,700,500
             
        self.setWindowTitle("Paint Application")
        self.setGeometry(left_right,up_down,width,height)
        self.setWindowIcon(QIcon("images/paint.jpg"))
        
        self.image=QImage(self.size(),QImage.Format_RGB32)
        self.image.fill(Qt.white) # by default we are gonna make this white
        
        self.drawing=False # initially drawing is false
        self.brushSize=2
        self.brushColor=Qt.black
        
        self.lastPoint=QPoint()
        
        mainMenu = self.menuBar()
        fileMenu=mainMenu.addMenu("File")
        brushMenu=mainMenu.addMenu("Brush Size")
        brushColor=mainMenu.addMenu("Brush Color")
        
        menu_names=[fileMenu,brushMenu,brushColor]
        return menu_names
        
    def file_save_actions(self,menu):
        
        # file menu attributes
        saveAction = QAction( QIcon("images/save.jpg") , "Save" , self )
        saveAction.setShortcut("Ctrl+S")
        menu[0].addAction(saveAction)
        saveAction.triggered.connect(self.save)
        
        clearAction = QAction(QIcon("images/clear.jpg"),"Clear",self)
        clearAction.setShortcut("Ctrl+C")
        menu[0].addAction(clearAction)        
        clearAction.triggered.connect(self.clear)

    def brush_pixels(self,menu):
        
        # brush menu  attributes
        threepxAction = QAction(QIcon("images/brush_size.jpg"),"3px",self)
        threepxAction.setShortcut("Ctrl+T")
        menu[1].addAction(threepxAction)       
        threepxAction.triggered.connect(self.threePx)
        
        fivepxAction = QAction(QIcon("images/brush_size.jpg"),"5px",self)
        fivepxAction.setShortcut("Ctrl+F")
        menu[1].addAction(fivepxAction) 
        fivepxAction.triggered.connect(self.fivePx)
        
        sevenpxAction = QAction(QIcon("images/brush_size.jpg"),"7px",self)
        sevenpxAction.setShortcut("Ctrl+S")
        menu[1].addAction(sevenpxAction) 
        sevenpxAction.triggered.connect(self.sevenPx)
        
        ninepxAction = QAction(QIcon("images/brush_size.jpg"),"9px",self)
        ninepxAction.setShortcut("Ctrl+N")
        menu[1].addAction(ninepxAction) 
        ninepxAction.triggered.connect(self.ninePx)
        
    def brush_colors(self,menu):
        
        # brush color  attributes
        blackAction=QAction(QIcon("images/black.png"),"black",self)
        blackAction.setShortcut("Ctrl+B")
        menu[2].addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)
        
        whiteAction=QAction(QIcon("images/white.png"),"white",self)
        whiteAction.setShortcut("Ctrl+W")
        menu[2].addAction(whiteAction)
        whiteAction.triggered.connect(self.whiteColor)
        
        grayAction=QAction(QIcon("images/gray.png"),"gray",self)
        grayAction.setShortcut("Ctrl+G")
        menu[2].addAction(grayAction)
        grayAction.triggered.connect(self.grayColor)
        
        greenAction=QAction(QIcon("images/green.png"),"green",self)
        greenAction.setShortcut("Ctrl+G")
        menu[2].addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)
        
        
        redAction=QAction(QIcon("images/red.png"),"red",self)
        redAction.setShortcut("Ctrl+R")
        menu[2].addAction(redAction)
        #redAction.triggered.connect(self.redColor) # ya direk functionlara gönder ayrı ayrı yaptım aşagıda yada tek functionda gönder parametre ile
        redAction.triggered.connect(lambda : self.color_choose_function("red"))
        
        yellowAction=QAction(QIcon("images/yellow.png"),"yellow",self)
        yellowAction.setShortcut("Ctrl+G")
        menu[2].addAction(yellowAction)
        #yellowAction.triggered.connect(self.yellowColor)
        self.yellow="yellow"
        yellowAction.triggered.connect(lambda : self.color_choose_function(self.yellow)) 
        # self.color_choose_function(self.yellow) diyemedik cünkü function içinde eleman gönderemedik,lambda kullanarak function içinde function göndermiş olduk yada parametre göndermiş olduk bu yontem ile
        
        
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
    
    # paint function 
    def paintEvent(self, event):
        canvasPainter=QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image,self.image.rect()  )
        #self.rect() : means rectangle 
    
    # file save function
    def save(self):
        filePath , _ = QFileDialog.getSaveFileName( self, "save Image","","PNG(*.png);; JPEG(*jpg *.jpeg);; ALL Files(*.*) " ) 
        if filePath =="":
            return
        self.image.save(filePath)
    
    # window clear function
    def clear(self):
        self.image.fill(Qt.white)
        self.update() # bunu update etmezsen etki etmez paint tablosuna
        
    # brush size functions
    def threePx(self):
        self.brushSize = 3
    
    def fivePx(self):
        self.brushSize = 5
        
    def sevenPx(self):
        self.brushSize = 7
        
    def ninePx(self):
        self.brushSize = 9
        
    # brush color functions
    def blackColor(self):
        self.brushColor = Qt.black
        
    def whiteColor(self):
        self.brushColor = Qt.white
        
    def grayColor(self):
        self.brushColor = Qt.gray
    
    def greenColor(self):
        self.brushColor = Qt.green
          
    """   # ayrı ayrı function yerine tek functionda parametre ile de ayrım yapılabilir
    def redColor(self):
        self.brushColor = Qt.red
    
    def yellowColor(self):
        self.brushColor = Qt.yellow
    """    

    def color_choose_function(self,color):
        if color=="red":
            self.brushColor =Qt.red
        elif color =="yellow":
            self.brushColor=Qt.yellow
    
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
        
        
        
        
        
        