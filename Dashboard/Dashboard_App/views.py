from django.shortcuts import render

def dashboard(request):
    return render(request,'login.html')

def dashboard2(request):
    return render(request,'dashboard.html')


def users(request):
    return render(request,'users-profile.html')

def form(request):
    return render(request,'form.html')

def editform(request):
    return render(request,'editform.html')

def mydata(request):
    return render(request,'mydata.html')

