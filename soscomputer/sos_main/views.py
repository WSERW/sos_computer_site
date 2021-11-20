import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Order

# Create your views here.

def index(request):
    if request.method == 'POST':
        client_name = request.POST.get('clientName',False)
        client_phone = request.POST.get('clientPhone',False)
        client_message = request.POST.get('clientMessage',False)
        captcha = request.POST.get('g-recaptcha-response',False)
        print(request.POST)
        params = {'secret':'6LfW78IaAAAAAA0phM-k5DB95tq80x-yalicb8Y3','response':captcha}
        captcha_resolved = False
        try:
            captcha_resolved = requests.post('https://www.google.com/recaptcha/api/siteverify', params = params).json()['success']
        except Exception as e:
            print(e)
        if captcha_resolved:
            print(captcha_resolved)
            if client_name and client_phone and client_message:
                order = Order(
                    name=client_name,
                    email=client_phone,
                    description=client_message,
                )
                order.save()
                # send_mail('Новая заявка c сайта',mailText,'soscomputeracademy@gmail.com',['soscomputeracademy@gmail.com'],fail_silently=False)
                return HttpResponse("true")
            else:
                return HttpResponse("false")
        else:
            print(captcha_resolved)
            return HttpResponse("captcha")
    else:
        return render(request, 'sos_main/index.html',context={})

def course(request):
    return render(request, 'sos_main/course.html',context={})

def services(request):
    return render(request,'sos_main/services.html',context={})