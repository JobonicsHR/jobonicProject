from django.conf.urls import url
from jobonicUsers import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/login/$', views.user_login),
    url(r'^users/(?P<pk>[0-9a-z-]+)/$', views.user_details),
]