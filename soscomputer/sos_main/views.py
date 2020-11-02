from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def index(request):
    if request.method == 'POST':
        # form = NameForm(request.POST);
        # if form.is_valid():
        clientName = request.POST.get('clientName',False)
        clientPhone = request.POST.get('clientPhone',False)
        clientMessage = request.POST.get('clientMessage',False)
        if clientName and clientPhone and clientMessage:
            mailText = f"""
            Имя: {clientName}
            Телефон: {clientPhone}
            Сообщение: {clientMessage}
            """
            send_mail('Новая заявка c сайта',mailText,'soscomputeracademy@gmail.com',['soscomputeracademy@gmail.com'],fail_silently=False)
            return HttpResponse(clientName+clientPhone+clientMessage)
        else:
            return HttpResponse("false")

    else:
        return render(request, 'sos_main/index.html',context={})
def course(request):
    return render(request, 'sos_main/course.html',context={})