


import sqlite3

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsım TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_sayısı INT)")
    con.commit()
def deger_ekle():
    cursor.execute("insert into kitaplık values('istanbul hatırası3','ahmet umit3','amip',263)")
    con.commit()

def deger_ekle2(isim,sanatcı,yayın_evi,sayfa_sayısı):
    cursor.execute("insert into kitaplık VALUES(?,?,?,?)",(isim,sanatcı,yayın_evi,sayfa_sayısı))
    con.commit()

def  veri_al():
    cursor.execute("Select * From kitaplık") #  ne varsa alıyor bununla Select standart  ,yıldız tüm demek  From da hangi yerden belirtir
    data=cursor.fetchall()# bu bilgileri dataya atıyor list içinde tuple olarak,bununla alırız
    print(data)
    print("kitaplık tablosunun bilgileri düzenli")
    for i in data:
        print(i)

def veri_al2():
    cursor.execute("select İsım,Yazar from Kitaplık")
    data=cursor.fetchall()
    print("kitaplık tablosundan bilgiler...")
    for i in data:
        print(i)

def veri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi=? ",(yayınevi,))# parantex ve yayınevi sonrasındaki virgul şart yoksa hata alırsın
    data=cursor.fetchall()
    print("bilgiler tablodan ....")
    for i in data:
        print(i)

def verigüncelle(yayınevi):
    cursor.execute("UPDATE kitaplık SET Yayınevi =? WHERE Yayınevi =?",(yayınevi,'everest'))
    con.commit()


# aynı yazara sahip all kitaplar silinir.
def veri_sil(ebru):
    cursor.execute("Delete From kitaplık where Yazar = ?",(ebru,))
    con.commit()


con=sqlite3.connect("kutuphane.db")
cursor=con.cursor()

tablo_oluştur()
deger_ekle()
#deger_ekle2()
#veri_al()
#veri_al2()
#veri_al3("everest")

veri_al()
#verigüncelle("alsunaidi")
#veri_al2()
veri_sil("ahmet umit3")


"""
veri_al() # veri sildik tablodan
veri_sil("ahmet umit2")
veri_al()
cursor.close()
"""








