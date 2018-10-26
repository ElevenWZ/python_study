from django.conf.urls import url, include
from booktest import views
app_name='[booktest]'
urlpatterns = [
    url(r'^index/$', views.index ),
    url(r'^book/(\d+)', views.detail)

]