from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from .models import Employee

from django.contrib import messages

from django.core.mail import send_mail  #step no 1

# Create your views here.

def base(request):
    return render(request,"index.html")

def register(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,"Account Successfully Created")
            return redirect('login')
        
    context={'form': form}
    return render(request,'register.html',context=context)




def login(request):
    form=LoginForm()

    if request.method=="POST":
        form=LoginForm(request,data=request.POST)

        if form.is_valid():
            username= request.POST.get('username')
            password= request.POST.get('password')
            
            user= authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashbord')
            
    complex={'form':form}
    return render(request,'login.html',complex)
            


def logout(request):
    auth.logout(request)

    messages.success(request, "Logout Successfully")
    return redirect('login')



def dashbord(request):

    send_mail('Welcome to CRM', 'Thank you for visiting to site', 'vinitvarvadkar0210@gmail.com',
              ['vinitvarvadkar0310@gmail.com','gmarathe050@gmail.com','vinitvarvadkar0210@gmail.com'], fail_silently=False)
    
    
    emp= Employee.objects.all()
    context={'emp':emp}
    return render(request,'dashbord.html',context)



def createrecord(request):
    form=CreateRecordForm()
    if request.method=="POST":
        form=CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,"Your Record Added Successufully")
            return redirect('dashbord')
    context={'form':form}
    return render(request,'createrecord.html',context)





def updaterecord(request,pk):
    
    emp=Employee.objects.get(id=pk)
    form=UpdateRecordForm(instance=emp)

    if request.method=="POST":
        form=UpdateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,"Your Record Update Successfully")
            return redirect('dashbord')
    context={'form':form}
    return render(request,'updaterecord.html',context)



def delete(request,pk):
    emp=Employee.objects.get(id=pk)
    emp.delete()

    messages.success(request,"Your Record Deleted Successfully")
    return redirect('dashbord')


    

def viewrecord(request,pk):
    emp=Employee.objects.get(id=pk)
    context={'emp':emp}
    return render(request,'viewrecord.html',context)




def email_invoice(request):
   
   send_mail('Welcome to CRM', 'Thank you for visiting to site', 'vinitvarvadkar0210@gmail.com',
              ['vinitvarvadkar0310@gmail.com','gmarathe050@gmail.com','vinitvarvadkar0210@gmail.com'], fail_silently=False)
   emp=Employee.objects.all()
   context={'emp':emp}
   return render(request,'dashbord.html','email-invoice.html',context)







