from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from borda.forms import PostForm
from .models import Post, Thread
from django.views.generic import View

# Create your views here.


def index(request):
    threads = Thread.objects.all()
    context = {
        'threads': threads,
    }
    return render(request, 'index.html', context)


class Threadpage(View):
    def get(self, request, **kwargs):
        thread_obj = Thread.objects.get(id=kwargs['thread_id'])
        form = PostForm()
        context = {
            'thread_name': thread_obj.name,
            'posts': thread_obj.post_set.all(),
            'form': form,
        }
        return render(request, 'thread.html', context)

    def post(self, request, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            p = Post(post_text=form.cleaned_data['post'], pub_date=timezone.now(), thread_id=kwargs['thread_id'])
            p.pic = request.FILES.get('picture', '')
            p.save()
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('')
