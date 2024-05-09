
from django.http import HttpResponse
from django.template import loader
from .models import Client
from django.shortcuts import render, get_object_or_404

# Create your views here.
def show_clients(request):
    users = Client.objects.all().values()
    context = {'users':users}
    template = loader.get_template('user_clients.html')
    return HttpResponse(template.render(context, request))

def details(request, id):
    usr = get_object_or_404(Client, id=id)
    context = {'usr': usr}
    return render(request, 'details.html', context)

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    