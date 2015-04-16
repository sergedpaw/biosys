from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^main/', include('main.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Define Home
    url(r'^home/?$', RedirectView.as_view(pattern_name='main_home'), name='home'),
    url(r'^$', RedirectView.as_view(pattern_name='home')),
    url(r'^index.html', RedirectView.as_view(pattern_name='home')),

]
