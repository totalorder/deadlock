from django.conf.urls import patterns, include, url

from django.contrib import admin
import blog

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('bootlog.urls')),
    url(r'blog/', include('blog.urls')),
    url(r'', blog.views.about, name="about"),
)
