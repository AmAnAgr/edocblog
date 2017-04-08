from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def list_view(request):         # list of recent posts

    query = Post.objects.all()
    paginator = Paginator(query, 5) # Show 5 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {

            'posts' : posts, 

    }


    return render(request, 'posts/index.html', context)


def detail_view(request, slug=None):

    post = get_object_or_404(Post, slug=slug)

    context = {

        'post' : post,
    }

    return render(request, 'posts/single.html', context)

def search_view(request):
    
    query = request.GET['q']

    results = Post.objects.filter(

                Q(title__icontains = query) |
                Q(content__icontains = query) 

        ).distinct()

    paginator = Paginator(results, 10) # Show 5 posts per page
    page = request.GET.get('page')

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results = paginator.page(paginator.num_pages)    



    return render(request, 'posts/index.html', { 'posts' : results })

