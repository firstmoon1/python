
from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import Personal
from django.contrib import messages


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def personal(request):
    if request.method=="POST":
        name1=request.POST.get("name_form")
        age1=request.POST.get("age_form")
        gender1=request.POST.get("gender_form")
        person=Personal( name=name1 , age=age1 , gender=gender1 )
        person.save()
        return redirect("app2:name_personal")
        #return redirect("/") # redirect in parametresi url olur , name olur,mesela redirect("name_index") yada redirect("/")
    person=Personal.objects.all()
    context={
        "datas":person,
    }
    return render(request,"personals.html",context)

def update_function(request,id):
    if request.method=="POST":
        name=request.POST.get("name1_form")
        age=request.POST.get("age1_form")
        gender=request.POST.get("gender1_form")
        Personal.objects.filter(id=id).update(name=name,age=age,gender=gender)
        return redirect("app2:name_personal")
    return render(request,"update.html" )   

def delete_function(request,id):
    person=Personal.objects.filter(id__contains=id)
    person.delete()
    return redirect("app2:name_personal")