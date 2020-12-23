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
        if client_name and client_phone and client_message:
            order = Order(
                name=client_name,
                email=client_phone,
                description=client_message,
            )
            order.save()
            # send_mail('Новая заявка c сайта',mailText,'soscomputeracademy@gmail.com',['soscomputeracademy@gmail.com'],fail_silently=False)
            return HttpResponse("Спасибо с вами свяжутся!")
        else:
            return HttpResponse("false")

    else:
        return render(request, 'sos_main/index.html',context={})

def course(request):
    return render(request, 'sos_main/course.html',context={})

def services(request):
    return render(request,'sos_main/services.html',context={})