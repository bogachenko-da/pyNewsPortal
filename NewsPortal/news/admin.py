from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    search_fields = ('user__username', 'rating')


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'post_created', 'title', 'rating')
    list_filter = ('author', 'post', 'post_created', 'rating')
    search_fields = ('author__user__username', 'title', 'rating')


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.get_fields()]
    search_fields = ('user__username', 'post__title', 'text', 'rating')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
