from django.shortcuts import render
from django.shortcuts import render_to_response
from name_blog.models import NameBlog

# Create your views here.

def f_nameblog(request):
	return render_to_response('nameblog.html', {'name': NameBlog.objects.all()})
