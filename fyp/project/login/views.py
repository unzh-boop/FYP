from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("TRAFFIC ANOMALY IDENTOFOCATOON SUSTEM")

def signup(request):
    return render(request, 'signup.html')

def upload(request):
    return render(request, 'upload.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

