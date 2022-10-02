import sqlite3

class Admin_User():
    def __init__(self,Name,Password):
        self.Name=Name
        self.Password=Password
    
    def __str__(self):
        return "Admin Name: {}\n Password: {}\n".format(self.Name,self.Password)
    
class Table_User():
    def __init__(self,Name,Age,Gender):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
    
    def __str__(self):
        return "Table user Name: {}\n Age: {}\n Gender: {}\n".format(self.Name,self.Age,self.Gender)


class datas():
    
    def __init__(self):
        self.baglanti()

    def baglanti(self):
        self.con=sqlite3.connect("database.db")
        self.cursor=self.con.cursor()
        self.User_Table_compose()
        self.Table_Table_compose()
          
    def User_Table_compose(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS User(Name TEXT,Password TEXT)")
        self.con.commit()
        
    def Table_Table_compose(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Tables(Name TEXT,Age INT,Gender TEXT)")
        self.con.commit()

    def Admin_user_enrol(self,Name,Password):
        self.cursor.execute("insert into User VALUES(?,?)",(Name,Password))
        self.con.commit()
    
    def Table_user_enrol(self,name,password,gender):
        self.cursor.execute("insert into Tables VALUES(?,?,?)",(name,password,gender))
        self.con.commit()

        
    def Admin_check(self):
        self.cursor.execute("Select * From User")
        self.data=self.cursor.fetchall()
        return self.data
    
    def veri_al(self):
        self.cursor.execute("Select * From Tables") #  ne varsa alıyor bununla Select standart  ,yıldız tüm demek  From da hangi yerden belirtir
        self.data=self.cursor.fetchall()# bu bilgileri dataya atıyor list içinde tuple olarak,bununla alırız
        
        #for i in self.data:
        #    pass
    
    def veri_sil(self,name):
        self.cursor.execute("Delete From Tables where Name = ?",(name,))
        self.con.commit()
        
    def verigüncelle(self,name,age,gender,nname,nage,ngender):
        self.cursor.execute("UPDATE Tables SET Name =? Age =? Gender =? WHERE Name =? Age =? Gender =?",(name,age,gender,nname,nage,ngender))
        self.con.commit()