from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'status', 'created_on')
    list_filter = ("status", "topic")
    search_fields = ['title', 'content']
    

admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on', )
    search_fields = ('name', 'body')
    #actions = ['approve_comments']

    #def approve_comments(self, request, queryset):
        #queryset.update(approved=True)