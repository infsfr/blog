from django.contrib import admin
from name_blog.models import NameBlog

# Register your models here.

class NameBlogAdmin(admin.ModelAdmin):
	fields = ['name_blog']

admin.site.register(NameBlog, NameBlogAdmin)
