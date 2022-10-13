from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    return render(request, 'appProg/post_list.html  ')
    
def cadastro(request):
    return render(request, 'appProg/cadastro.html  ')

def checkin(request):
    return render(request, 'appProg/checkin.html  ')