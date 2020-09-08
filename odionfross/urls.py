from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('project/<int:p_id>', views.project),
    path('about', views.about),
    path('contact', views.contact),
]