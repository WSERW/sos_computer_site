from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sos_main/index.html',context={})
def course(request):
    return render(request, 'sos_main/course.html',context={})