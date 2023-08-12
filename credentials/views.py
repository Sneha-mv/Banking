from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('credentials:login')

        else:
            messages.info(request, "Password not matching")
            return redirect('credentials:register')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('bankingapp:new')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('credentials:login')


    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('bankingapp:index')



