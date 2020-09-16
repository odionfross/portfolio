from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('project/<int:id>', views.project),
    path('about', views.about),
    path('contact', views.contact),
    path('admin', views.admin),
    path('new_project', views.add_project),
    path('edit_project/<int:id>', views.edit_project),
    path('delete_project/<int:id>', views.delete_project),
    path('log_out', views.log_out),
]