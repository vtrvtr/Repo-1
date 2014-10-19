from django.conf.urls import *
from django.contrib import admin
from django.views import *
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'transporte.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'transporte.views.home', name='home'),
    url(r'^blogs$', 'transporte.views.blogs', name='blogs'),
    url(r'^.*$', RedirectView.as_view(url='home', permanent=False), name='index')

)
