from django.db import models

# Create your models here.

class NameBlog(models.Model):
	class Meta():
		db_table = "nameblog"
	name_blog = models.TextField(max_length=100)
	