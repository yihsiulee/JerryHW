from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post_list/', views.post_list, name='post_list'),
    url(r'^add/', views.add, name='add'),
    url(r'^edit/', views.edit, name="edit"),
    url(r'^delete/', views.delete, name="delete"),
]