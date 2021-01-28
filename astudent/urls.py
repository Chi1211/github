from django.urls import path
from . import views
from . import models
urlpatterns = [
	path('', views.GetStudent.as_view(), name='getstudent'),
	path('delete/<int:id>', views.DeleteStudent, name='delete'),
	path('add/', views.AddStudent.as_view(), name='add'),
	path('update/<int:id>', views.UpdateStudent.as_view(), name='update'),
	path('search/', views.Search, name='search'),
    ]