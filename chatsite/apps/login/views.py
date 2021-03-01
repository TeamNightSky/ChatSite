from django.shortcuts import render
from utils.storage import CONFIG


def login_page(request):
    return render(request, 'login.html', {'config': CONFIG})


def register_page(request):
    return render(request, 'register.html', {'config': CONFIG})
