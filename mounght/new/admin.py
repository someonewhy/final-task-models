from django.contrib import admin
from .models import Post, Message, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pub_date', 'category']
    list_filter = ['category', 'pub_date', 'author']
    search_fields = ['title', 'content', 'author__username']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'sent_date']
    list_filter = ['sent_date', 'sender', 'receiver']
    search_fields = ['content', 'sender__username', 'receiver__username']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)
