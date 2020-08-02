from django.shortcuts import render

from .models import client
# Create your views here.


def home(request):
# get all records from client table
    clients = client.objects.all()
    return render( request,'home.html', {'clients':clients,})

def client_detail(request, client_id):
    records = client.objects.get(id = client_id)
    return render(request, 'client.html', {'records':records})

def about(request):
    heading = 'Razban Professional Clothing Compay'
    return render(request, 'about.html', {'heading':heading })
