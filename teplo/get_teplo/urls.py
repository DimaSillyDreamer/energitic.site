
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('heat-calc', views.heat_calc, name="heat_calc"),
    path('pump-calc', views.pump_calc, name="pump_calc"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
    path('tools-page', views.tools_page, name="tools_psge"),
    path('instruments', views.instruments, name="instruments"),
    path('fuel-calc', views.fuel_calc, name='fuel_calc'),
    path('articles', views.articles, name='articles'),
    path('fuel-tank', views.fuel_tank, name='fuel_tank'),
    path('contacts', views.contacts, name='contacts'),
    path('questionnaires', views.questionnaires, name='questionnaires'),
    path('news', views.news, name='news')
]

