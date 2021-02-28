from django.shortcuts import render
from utils.storage import CONFIG


def messages_page(request):
    return render(request, 'messages.html', {'config': CONFIG})

def post_page(request):
    return render(request, 'post.html', {'config': CONFIG})

def explore_page(request):
    return render(request, 'explore.html', {'config': CONFIG})

def help_page(request):
    return render(request, 'help.html', {'config': CONFIG})
