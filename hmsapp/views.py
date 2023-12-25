from django.shortcuts import render,redirect
from django.http import HttpResponse
from hmsapp.models import Bookorder,Menu
from hmsapp.forms import EmpFormClass,UserRegister
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate ,login


# Create your views here.
def home(request):
    return render(request,'home.html')

def bookorder(request):
    user_id=request.user.id 
    if request.method=='POST':
        fn=request.POST['fname']
        qt=request.POST['qty']
        ca=request.POST['cat']
        name=request.POST['n']
        add=request.POST['a']
        con=request.POST['c']
        
        x = Bookorder.objects.create(foodname=fn,qty=qt,cat=ca,name=name,address=add,contact=con,uid=user_id)
        x.save()
        return render(request,'orderdone.html')
    else:    
        return render(request,'bookorder.html')
    

def menucard(request):
    qset=Menu.objects.all()
    content={}
    content['data']=qset
    return render(request,'menucard.html',content)

def orderdone(request):
    return render(request,"orderdone.html")

def dash(request):
    qset=Bookorder.objects.all()
    content={}
    content['data']=qset
    return render(request,"dash.html",content)

def completed(request,rid):
    x = Bookorder.objects.filter(id=rid)
    x.delete()
    return redirect('/dash')

def edit(request,rid):
    
    return redirect('/dash')

def addmenu(request):
    if request.method=='POST':
        a=request.POST['fn']
        b=request.POST['qt']
        c=request.POST['ca']
        d=request.POST['pri']
        e=request.POST['sd']
        y = Menu.objects.create(foodname=a,qty=b,cat=c,price=d,stat=e)
        y.save()
        return HttpResponse("New Menu added succesfully!!")
    else:
        return render(request,"addmenu.html")

def menu(request):
    qset=Menu.objects.all()
    content={}
    content['data']=qset
    return render(request,"menu.html",content)

def updatemenu(request,rid):
    if request.method == 'POST':
        a=request.POST['fn']
        b=request.POST['qt']
        c=request.POST['ca']
        d=request.POST['pri']
        e=request.POST['sd']
        p=Menu.objects.filter(id=rid)
        p.update(foodname=a,qty=b,cat=c,price=d,stat=e)
        return redirect ('/menu')
    else:
        z=Menu.objects.filter(id=rid)
        content={}
        content['data']=z
        return render(request,'updatemenu.html',content)

def deletemenu(request,rid):
    q = Menu.objects.filter(id=rid)
    q.delete()
    return redirect('/menu')

def catfilter(request,cv):
     m = Bookorder.objects.filter(cat=cv)
     print(m)
     content={}
     content['data']=m
     return render(request,"dash.html",content)

def sortfilter(request,x):
    if x == '0':
        n=Menu.objects.order_by('price')
    else:
        n=Menu.objects.order_by('-price')

    content={}
    content['data']=n
    return render(request,"menucard.html",content)
    
def filprice(request,x):
    if x == '1':
        n=Menu.objects.order_by('-price').filter(price__gt=400)
    else:
        n=Menu.objects.filter(price__lte=400)

    content={}
    content['data']=n
    return render(request,"menucard.html",content)
        
def django_form(request): 

    if request.method=="POST":
        name=request.POST['empname']
        mob=request.POST['mobile']
        date=request.POST['joiningdate']
        
    else:
        dfobj=EmpFormClass()
        # print(dfobj)
        content={}
        content['form']=dfobj
        return render(request,'empform.html',content)

def user_register(request):
    content={}
    if request.method=="POST":
        regfm=UserRegister(request.POST)
        # print(regfm)
        if regfm.is_valid():
            regfm.save()
            content['msg']="User registred Successfully"
            return render(request,'registersuccess.html',content)
        
    else:
        regfm=UserRegister()
        # print(regfm)
        content={}
        content['regfm']=regfm
        return render(request,'register.html',content)

def user_login(request):
    if request.method=="POST":
        logfm=AuthenticationForm(request=request,data=request.POST)
        if logfm.is_valid():
            uname=logfm.cleaned_data['username']
            upass=logfm.cleaned_data['password']
            res=authenticate(username=uname,password=upass)
            if res:
                login(request,res)
                return redirect('/bookorder')       
    else:
        logfm=AuthenticationForm()
        # print(logfm)
        content={}
        content['form']=logfm
        return render(request,'login.html',content)
    
def staticfile(request):
    return render(request,'learnstatic.html')


