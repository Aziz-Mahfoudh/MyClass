from django.shortcuts import render, redirect
from firebase_admin import auth
import pyrebase

config = {
    'apiKey': "AIzaSyB1dsl_Gy7xS6J-1MHYMDIzdwvdQ2fDyrU",
    'authDomain': "myclass-beta.firebaseapp.com",
    'databaseURL': "https://myclass-beta-default-rtdb.firebaseio.com",
    'projectId': "myclass-beta",
    'storageBucket': "myclass-beta.appspot.com",
    'messagingSenderId': "643574428350",
    'appId': "1:643574428350:web:bfc6c3c6177c863e7364ef",
    'measurementId': "G-DGSL2WZ6JQ"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def toLogin(request):
    
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    
    try: 
        token = auth.sign_in_with_email_and_password(email, pwd)
    except:
        message = "Identifiant ou mot de passe incorrect. Veuillez vous reconnecter."
        return render(request, 'login.html', {"message":message})
    
    sessionId = token['idToken']
    request.session['uid']= sessionId
    
    return render(request, 'home.html', {"email":email})

def logout(request):
    # try:
    #     del request.session['uid']
    # except:
    #     pass
    return render(request, 'login.html')


