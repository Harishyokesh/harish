from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/',views.show_students,name="students"),
    path('about/',views.about,name="about"),
    path('address/',views.about,name="about")
]
