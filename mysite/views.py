from django.shortcuts import render, redirect
# from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime

# Create your views here.
def homepage(request):
    # posts = Post.objects.all()
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append('No.{}：'.format(str(count)) + str(post) + '<br>')
    # return HttpResponse(post_lists)
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')