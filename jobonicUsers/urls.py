from django.conf.urls import url
from jobonicUsers import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_details),
    url(r'^users/login/(?P<user_name>[a-z0-9]+)/(?P<password>[a-zA-Z0-9-/@$])/$', views.user_login)
]