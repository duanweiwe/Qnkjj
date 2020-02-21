from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.app3_login, name='app3_login'),
    #url(r'^logout/$', views.kjj_logout, name='kjj_logout'),
]