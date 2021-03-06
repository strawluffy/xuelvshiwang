from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xuelfshiwang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'login.views.hello'),
    url(r'^hook/', include('github_hook.urls')),
    url(r'^deploy/$', 'login.views.deploy'),
    url(r'^$', 'login.views.index'),
)
