from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Thread

# Create your views here.


def index(request):
    threads = Thread.objects.all()
    context = {
        'threads': threads,
    }
    return render(request, 'index.html', context)


def thread(request, thread_id):
    thread_obj = Thread.objects.get(id=thread_id)
    context = {
        'thread_name': thread_obj.name,
        'posts': thread_obj.post_set.all(),
    }
    return render(request, 'thread.html', context)
