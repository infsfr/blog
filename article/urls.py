from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^get/(?P<article_id>[-\d]+)/$', 'article.views.article'),
    url(r'^all/$', 'article.views.articles'),

)
