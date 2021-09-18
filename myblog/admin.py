from django.contrib import admin
from .models import Post
# Register your models here.
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title')}