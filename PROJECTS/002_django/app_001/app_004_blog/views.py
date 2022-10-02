from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def dashboard(request):
    articles=Article.objects.all()
    return render(request,"dashboard.html",{"article":articles})

def articles(request):
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})


def detail(request,id):
    article=get_object_or_404(Article,id=id)
    return render(request,"detail.html",{"artic":article})
    
    
def article_add(request):
    
    if request.method == "POST":
        author=request.POST["author2"]
        title=request.POST["title2"]
        content=request.POST["content2"]
        if request.FILES :
            file=request.FILES["file2"]
        else:
            file=None
        Article.objects.create(author=author, title=title,content=content,files=file)
        messages.success(request,"makale eklendi")
        return redirect("app4:name_dashboard")    
    return render(request,"add_article.html")

def article_delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"makale is deleted.")
    return redirect("app4:name_dashboard")

def article_update(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method == "POST":
        article.author=request.POST["author3"]
        article.title=request.POST["title3"]
        article.content=request.POST["content3"]
        if request.FILES :
            article.files=request.FILES["file3"]
        else :
            article.files=None
        article.save()
        messages.success(request,"makale guncellendi")
        return redirect("app4:name_dashboard")
    return render(request,"update_article.html")