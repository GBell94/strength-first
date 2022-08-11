from django.shortcuts import render
#from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
#from django.contrib.auth.models import User
from .models import Post, Comment
#from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    model = Post
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5

    
cats = ('KB', 'BB', 'BW')

def CategoryView(request, cats):
	    category_posts = Post.objects.filter(category=cats)
	    return render(request, 'categories.html', {'cats': cats, 'category_posts':category_posts})
       

#def category_view(request):
    #category_posts = Post.objects.filter(topic='KB')
    #return render(request, 'categories.html', {'category_posts': category_posts})


def category_view(request):
    category_posts = Post.objects.filter(topic='KB')
    return render(request, 'categories.html', {'category_posts': category_posts})


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'topic', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'topic', 'content']
    

class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddComment(generic.CreateView):
    model = Comment
    #form_class = CommentForm
    fields = ['body']
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        return super().form_valid(form)
