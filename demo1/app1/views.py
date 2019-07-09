from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import loader
from .models import Chiose,Questions
# Create your views here.

def checklogin(fun):
    def check (request,*args):
        username=request.COOKIES.get("username")
        if username:
            # *args为可变函数
            return fun(request,*args)
        else:
            return redirect(reverse('app1:login'))
    return check


# 装饰器
@checklogin
def index(request):
    # temp=loader.get_template('app1/index.html')
    # context={'sfsd':'sdf'}
    # result=temp.render(context=context)
    # return  HttpResponse(result)
    # COOKIES.[]取不到会报错
    questions = Questions.objects.all()
    username = request.COOKIES.get("username")
    return render(request,'app1/index.html',locals())

    # username=requset.COOKIES.get("username")
    # if username:
    #     questions=Questions.objects.all()
    #     return render(requset,'app1/index.html',locals())
    # else:
    #     return redirect(reverse('app1:login'))

@checklogin
def detail(request,id):
    question=Questions.objects.get(pk = id)
    if request.method=='GET':
        return  render(request,'app1/detail.html',locals())

    elif request.method=='POST':
        choiceid = request.POST.get("chiose")
        choice = Chiose.objects.get(pk=choiceid)
        choice.number +=1
        choice.save()
        return redirect(reverse("app1:result" ,args=(id,)))
@checklogin
def result(request,id):
    quese=Questions.objects.get(pk=id)
    return  render(request,'app1/result.html',locals())



def login(request):
    if request.method=="GET":
        return render(request,'app1/login.html')
    elif request.method=="POST":

        response=redirect(reverse('app1:index'))
        response.set_cookie("username",request.POST.get("username"))
        return response

def logout(request):
    ret=redirect(reverse('app1:login'))
    ret.delete_cookie("username")
    return ret




