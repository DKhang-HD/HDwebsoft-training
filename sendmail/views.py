from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def index(request):

    send_mail("Hello from Khang",
    "Hello, there. This is the automated message",
    "alvintk113@gmail.com",
    ["phamduykhang197@gmail.com"],
    fail_silently = False)
    
    return render(request,'sendmail/index.html')