from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def cat(request):
    return render(request, 'cat.html')

def checkout1(request):
    return render(request, 'checkout1.html')

def consult(request):
    return render(request, 'consult.html')

def consult1(request):
    return render(request, 'consult1.html')

def dog(request):
    return render(request, 'dog.html')

def login(request):
    return render(request, 'login.html')

def petservice(request):
    return render(request, 'petservice.html')

def smallpet(request):
    return render(request, 'smallpet.html')

def thank(request):
    return render(request, 'thank.html')
