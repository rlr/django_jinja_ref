from django.conf.urls import url

from django_jinja_ref.superadvanced import views

urlpatterns = [
    url(r'^$', views.django, name='django'),
    url(r'^jinja$', views.jinja, name='jinja'),
]
