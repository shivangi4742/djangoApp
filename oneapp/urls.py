from django.urls import path

from . import views

urlpatterns = [
    path('city/', views.get_users),
    path('rbl/', views.get_city),
    path('shivangi/', views.shivangi.as_view()),

]