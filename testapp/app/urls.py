from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('list/', views.obtener_socios, name='list' ),
]