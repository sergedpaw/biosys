from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^home/?$', views.home_view, name="main_home"),
    url(r'/?$', RedirectView.as_view(pattern_name='main_home'))
]