from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


# Create your views here.

def register_func(request):
    if request.method == "POST":
        username = request.POST["username2"]
        email = request.POST["email2"]
        password = request.POST["password2"]
        password1 = request.POST["password12"]
    
        if password == password1 :
            if  User.objects.filter(email=email).exists():
                messages.info(request,"email already used")
                return redirect("app3:name_register") 
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already Used") 
                return redirect("app3:name_register") 
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                #user.save()  # objects ile kullanıcı kayıt edersen save etmene gerek yok,auto save eder.
                messages.success(request,"basarı ile kayıt olundu")
                #login(request,user)
                return redirect("app3:name_login")    
        else:
            messages.info(request,"password not same")
            return redirect("app3:name_login")
    else:    
        return render(request,"register.html")


def login_func(request):
    
    if request.method=="POST":
        username=request.POST["username3"]
        password=request.POST["password3"]
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("name_index")
        else:
            messages.info(request,"username or password may be empty or wrong")
            return redirect("app3:name_login")
    return render(request,"login.html")


def logout_func(request):
    logout(request)
    messages.success(request,"basarı ile cıkıs yapıldı")
    return redirect("name_index")  # app_001 deki urls.py deki ana sayfa







"""   
---------------------------------------------------------------------------------------------------------------

Kullanıcı kaydetme yolu 1
- newUser = User(username="denemekullanıcı1",password="123")
newUser.save()
terminalde newUser yazarak kullanıcıyı görürsün,sqlite dan baktıgında şifre encryted edilmemiştir, bunun için alttaki gibi yap

Kullanıcı kaydetme yolu 2
- newUser2 =User(username="denemekullanıcı2")
newUser2.set_password("123") // encrypted edildi
newUser2.save() // veritabanına kaydetmek için kullandık

Kullanıcı kaydetme yolu 3
- newuser2=User()
newuser2.username="denemekullanıcı3"
newUser3.set_password("123") // encrypted edildi
newUser3.save() // veritabanına kaydetmek için kullandık

----------------------------------------------------------------------------------------------------------------

Article olusturma yöntemi 1
- article1=Article(title="Django Shell Deneme",content="icerik icerik",author=newuser1) // byrdaki newuser1 yukarda olusturduk var olan User olmalı
article1.save()


Article olusturma yöntemi 2
- article2.title="deneme 15" 
article2.content="icerik" 
article2.author=newuser2
article2.save()


Article olusturma yöntemi 3 ,bu yontemde article3.save() yapmana gerek kalmıyor kendi auto yapar :

- Article.objects.create(title="deneme 32",content="21",author=newuser3)

 veya bir objeye atayabilirsin :

- article3 = Article.objects.create(title="deneme 30",content="21",author=newuser3) 
article3.title yazarak terminalde sana 'deneme 30' yazar 

eger uptade yapmak istersen böyle yaparsın ama sonrasında .save() yapılmalı :

- article3.title="deneme 30 degisti" 
article3.save()

----------------------------------------------------------------------------------------------------------------

tablodaki tüm article ları almak için :

- Article.objects.all()
output : <QuerySet [<Article: Article object (7)>, <Article: Article object (8)>, <Article: Article object (9)>, <Article: Article 
object (10)>, <Article: Article object (11)>]> 

belirli objeyi almak için spesifik olarak :

- Article.objects.get(title="deneme 15")
output : <Article: Article object (9)>

veya bir objeye atayabilirsin :  

 article4=Article.objects.get(title="deneme 15") 
 article4.title
output :'deneme 15'


bir article'i silmek içinde .delete() yaparız mesela :

- article4.delete()
output : (1, {'article.Article': 1})


bir article'i id ye göre secme :

- article5=Article.objects.get(id=7)  // sqlite dan baktım article_article tablosundan deneme_1 diye bir article vardı

istersen bunuda silersin mesela :
- article5.delete()  // gibi


filter da yapılabilir mesela title da içinde den gecenleri al gibi :
djangoda orm sorguları için title__contains ="" yapılmalı ,title degişebilir mesela id__contains=5 gibi mesela,"" içine yazdıgın mesela "Den"

- Article.objects.filter(title__contains="She") // bir objeye atayamadım mesela article6=Article.objects.filter(...) gibi
output : <QuerySet [<Article: Article object (8)>]>

----------------------------------------------------------------------------------------------------------------




"""