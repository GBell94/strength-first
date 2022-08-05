from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post
    template_name = 'index.html'
    paginate_by = 5


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'author', 'topic', 'content']


class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'topic', 'content']
    
