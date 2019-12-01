from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about,name='about'),
    path('student', views.student,name='student'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
]