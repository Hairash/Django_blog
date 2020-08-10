from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.full_post, name='post'),
    path('add/', views.add, name='add'),
    # path('add_process/', views.add_process, name='add_process'),
]
