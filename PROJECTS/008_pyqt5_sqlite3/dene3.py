

from PyQt5 import QtCore, QtGui, QtWidgets
from sqlite import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(10, 10, 361, 201))
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.btn_add.setObjectName("btn_add")
        self.btn_update = QtWidgets.QPushButton(Form)
        self.btn_update.setGeometry(QtCore.QRect(100, 260, 91, 23))
        self.btn_update.setObjectName("btn_update")
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setGeometry(QtCore.QRect(210, 260, 91, 23))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_add_row = QtWidgets.QPushButton(Form)
        self.btn_add_row.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.btn_add_row.setObjectName("btn_add_row")
        self.btn_del_row = QtWidgets.QPushButton(Form)
        self.btn_del_row.setGeometry(QtCore.QRect(210, 230, 91, 23))
        self.btn_del_row.setObjectName("btn_del_row")
        self.btn_refresh = QtWidgets.QPushButton(Form)
        self.btn_refresh.setGeometry(QtCore.QRect(100, 230, 91, 23))
        self.btn_refresh.setObjectName("btn_refresh")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        
        self.loaddatas()
        self.btn_add_row.clicked.connect(self.func_add_row)
        self.btn_del_row.clicked.connect(self.func_del_row)
        self.btn_add.clicked.connect(self.func_add)
        self.btn_delete.clicked.connect(self.func_del)
        self.btn_update.clicked.connect(self.func_update)
        self.btn_refresh.clicked.connect(self.loaddatas)
    
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Age"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Gender"))
        self.btn_add.setText(_translate("Form", "content add"))
        self.btn_update.setText(_translate("Form", "content update"))
        self.btn_delete.setText(_translate("Form", "content delete"))
        self.btn_add_row.setText(_translate("Form", "add_row"))
        self.btn_del_row.setText(_translate("Form", "delete_row"))
        self.btn_refresh.setText(_translate("Form", "Refresh"))
        
    def func_add_row(self):
        rowCount = self.table.rowCount()
        self.table.insertRow(rowCount)    
    
    def func_del_row(self):
        if self.table.currentItem() is None:
            #self.table.removeRow(self.table.rowCount()-1) # en sondan siliyor 
            self.table.removeRow(self.table.currentRow())
        
        
    # önceden var olan dataları tabloya yükler Pyqt deki. from sqlite3 den.
    def loaddatas(self):
        con=sqlite3.connect("database.db")
        cursor=con.cursor()
        cursor.execute("SELECT * FROM Tables")
        datas=cursor.fetchall()
        tablerow=0
        #print("datas : ",datas)
        self.table.setRowCount(len(datas))
        for row in datas:
            #print(row)
            self.table.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
        con.close()
        
        
    def func_add(self):
        
        if self.table.currentItem() is not None:
            con=sqlite3.connect("database.db")
            cursor=con.cursor()
            item=[]
            item_row=self.table.currentItem().row()
            item_column=self.table.currentItem().column()
            #item = [ self.table.item(item_row, i ).text() for i in (range(3)) ]
            
            for i in range(3):
                if self.table.item(item_row,i ) is None:
                    item.append("")
                else:
                    item.append(  self.table.item(item_row,i ).text() )
               
            
            #print(item_row)
            #print(item_column)
            #print(item)
    
            sorgu="insert into Tables VALUES(?,?,?)"
            cursor.execute(sorgu,(item[0],item[1],item[2]))    
            con.commit()
            con.close()
            self.loaddatas()
            
    
        
    def func_del(self):
        cnt=self.table.rowCount()
        #print("cnt : ",cnt)
        if cnt > 0:
            if self.table.currentItem() is None :
                self.table.removeRow(cnt-1)
            else :
                con=sqlite3.connect("database.db")
                cursor=con.cursor()
                item=[]
                item_row=self.table.currentItem().row()
                item_column=self.table.currentItem().column()
                #item = [ self.table.item(item_row, i ).text() for i in (range(3)) ]
                for i in range(3):
                    if self.table.item(item_row,i ) is None:
                        item.append("")
                    else:
                        item.append(  self.table.item(item_row,i ).text() )
                sorgu="Select rowid,* From Tables"  # tüm rowları ve index numberları ile aldık
                cursor.execute(sorgu)
                datas=cursor.fetchall()
                #print(datas)
                            
                #self.table.removeRow(self.table.rowCount()-1) # en sondan siliyor 
                #selected_row = self.table.currentRow()
                item_row=self.table.currentItem().row()
                #print("item row :",item_row)
                #item_column=self.table.currentItem().column() # bize direk secili cell içerigini verir
                #item =[ self.table.item(item_row, i ).text() for i in (range(3))]  # get cell at row, col
                #print("selected : ",selected_row )
                sorgu = "Delete From Tables where rowid =?"
                cursor.execute(sorgu, ( str(item_row+datas[0][0]  ) ))
                con.commit()
                con.close()
                self.table.removeRow(item_row) 
                self.loaddatas()
                """
                if item_row != None:
                    for i in datas:
                        #print(i[0],i[1],i[2])
                        if i[0] == item[0]:
                            if ( i[1] == item[1] )  :
                                if i[2] == item[2]:
                                    #print(" i : ",i[0],i[1],i[2])
                                    sorgu = "Delete From Tables where Name =? and Age =? and Gender =?"
                                    cursor.execute(sorgu, (i[0],i[1],i[2] ))
                                    con.commit()
                                    con.close()
                                    #self.table.removeRow(item_row) 
                                    self.loaddatas()
                                    break
                """
                    #print("selected item :",item)
                    #print("selected row :",item_row)
                    #print("selected column :",item_column)  
            #sorgu = "Delete From Tables where  = ?"
            #cursor.execute(sorgu, (selected_row,))
            #con.commit()
            #self.table.removeRow(selected) 

    def func_update(self):
        if self.table.currentItem() is not None:
            con=sqlite3.connect("database.db")
            cursor=con.cursor()
            # from table
            item_row=self.table.currentItem().row()
            item_column=self.table.currentItem().column()
            item = [ self.table.item(item_row, i ).text() for i in (range(3)) ]
            
            # from sqlite3
            sorgu="Select * From Tables"  # tüm rowları ve index numberları ile aldık
            cursor.execute(sorgu)
            datas=cursor.fetchall()
            if item_row != None:
                
                for i in range(len(datas)+1):
                    if i == item_row:   
                        print(i," - ",item_row)
                        print("types datas : ",type(datas[i][0]),type(datas[i][1]),type(datas[i][2]))
                        print("types ite : ",type(item[0]),type(item[1]),type(item[2]))
                        print("datas[",i,"] : ",datas[i][0],datas[i][1],datas[i][2])
                        print("item : ",item[0],item[1],item[2])

                        sorgu="Update Tables set Name = ? Where Name = ?"
                        cursor.execute(sorgu,(item[0],datas[i][0]))    
                        con.commit()
                        sorgu="Update Tables set Age = ? Where Age = ? "
                        cursor.execute(sorgu,(item[1],datas[i][1]))    
                        con.commit()
                        sorgu="Update Tables set Gender = ? Where  Gender = ?"
                        cursor.execute(sorgu,(item[2],datas[i][2]))    
                        con.commit()
                        con.close()
                        break
            
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
