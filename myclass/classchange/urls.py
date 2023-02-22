from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('submitform/', views.submitform, name='submitform'),
    path('logs/', views.getchanges, name='getchanges'),
    path('deletechange/<str:key>', views.deletechange)
]
