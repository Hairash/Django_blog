from django.shortcuts import render, redirect
from django.http import Http404

from .models import Post
from .forms import PostForm


def index(request):
    top_post = ''
    top_post_start = ''
    if Post.objects.all().count() > 0:
        top_post = Post.objects.order_by('-date')[0]
        top_post_start = top_post.content.splitlines()[0]
    return render(request, 'index.html', {
        'posts': Post.objects.order_by('-date')[1: 10],
        'top_post': top_post,
        'top_post_start': top_post_start,
    })


def full_post(request, post_id):
    try:
        a = Post.objects.get(id=post_id)
    except:
        raise Http404('Post doesn\'t exist')

    return render(request, 'full_post.html', {'post_id': post_id, 'post': Post.objects.get(id=post_id)})


def add(request):
    # return render(request, 'add.html')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            print('VALID')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('index')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'add.html', {'form': form})

