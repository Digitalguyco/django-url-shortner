
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
import uuid
from django.contrib.auth.models import User
from .models import Url
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# creat hashed password with make_password
from django.contrib.auth.hashers import make_password

# Create your views here.

# ALL FUNCTION BASED VIEWS


#   Index view
def index(request):
    return render(request, 'index.html') 

# Signup view
def signup(request):
    if request.user.is_authenticated: # check if user is authenticated
        return redirect('/app/') 
    
     
    if request.method == 'POST':
        # Get Posted Informations
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        new_user = User.objects.create(
            email = email,
            password = make_password(password),
            username= username
        ) # Create a new User
        new_user.save() # Save to Database
        # Once Compelted Login The User
        login(request, new_user)
        
        

    
    return render(request, 'signup.html')
        
    
 
# Signin view
def signin(request):
    if request.user.is_authenticated:
        # print(request.user) checking the user
        return redirect('/app/')
        
    if request.method == 'POST':
        # Get Posted Informations
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
        # print(user) Checking if user existing in Database

        if user is not None: # If User Exists
           login(request,user)
          
        else: # Throw an error message
            return HttpResponse("Error: This User isn't Found in our Database, Please Create an account")
           
    return render(request, 'signin.html')

# Signout view
def signout(request):
    logout(request) # sign user out 
    return redirect('/') # redirect user to home

# SHORTEND link view

def short(request, pk): # takes primary key(pk) as second args
    # If any errors, Redirect to homepage
    try:
        url = Url.objects.get(uuid=pk) # get spefic url
        return redirect('https://'+url.link) # redirect to link
    except:
        return redirect('/') # if any errors Redirect home





# VIEWS ONLY ACCESSABLED TO AUTHETICATED USERS

# App view
@login_required
def app(request):
    return render(request, 'dashboard.html')

# Links view
@login_required
def links(request):
    links = Url.objects.filter(user=request.user) # gets specific users links
    return render(request, 'links.html', {'links': links}) # Passing Links as context

# Create Short Link View
@login_required
def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:3] # gets a 3 digit uuid
        # Saving Url Objects to database
        new_url = Url(link=link,uuid=uid,user=request.user) 
        new_url.save()
        # Returning uid as a response
        return HttpResponse(uid)




   
        