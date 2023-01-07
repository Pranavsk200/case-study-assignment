from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as dj_login,logout
from django.contrib.auth.models import User
from .models import Incident
from django.contrib import messages
import datetime

# Create your views here.
def incidentForm(request):
    if request.method == "POST":
        location = request.POST['loc']
        incDept = request.POST['incDep']
        date = request.POST['date']
        time = request.POST['time']
        incLOcation = request.POST['incLoc']
        initSeverity= request.POST['initialSeverity']
        case = request.POST['case']
        action = request.POST['action']
        env = request.POST.get('env',False)
        injury = request.POST.get('injury', False)
        prop =  request.POST.get('property', False)
        vechical = request.POST.get('vechical',False)

        if prop == 'on':
            prop = True
        else:
            prop=False
        if vechical == 'on':
            vechical=True
        else:
            vechical = False
        if injury == 'on':
            injury=True
        else:
            injury=False
        if env == 'on':
            env = True 
        else:
            env = False                           
        
        inci = Incident(
            location=location,
            incidentDept = incDept,
            time = time,
            incidentLoc = incLOcation,
            initialSeverity = initSeverity,
            cause = case,
            actionTaken = action,
            envInc = env,
            injury = injury,
            properties = prop,
            Vehical = vechical,
            user = request.user,
        )
        inci.save()
        messages.info(request,'incident is saved succesfully')
    return render(request, 'reportIncident.html')

def login(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['pass']
        user=authenticate(request, username=name, password=password)
        if user is not None:
            dj_login(request, user)
            current_user=request.user
            return redirect("incidentForms")
        else:
            messages.success(request, "username or password is incorrect") 
            return redirect("login")   
    else:    
        return render(request,"login.html")    

def signin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['pass']
        repassword = request.POST['repass']
        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exists,please resistor with another username") 
                return redirect("signin")   
            else:    
                user =User.objects.create_user(username=username, password=password)
                user.save()
                print('user created')
                return redirect("login")
        else:
            messages.info(request, "conform passowerd and password are not matching")
    else:
        return render(request, "signin.html")        