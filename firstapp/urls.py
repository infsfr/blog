from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

<<<<<<< HEAD
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include('article.urls')),
    url(r'^', include('article.urls')),
    url(r'^', include('name_blog.urls')),
    

)


=======
urlpatterns = patterns(
    '',
    url(r'^$', 'article.views.articles'),
    url(r'^articles/', include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
>>>>>>> upstream/master
