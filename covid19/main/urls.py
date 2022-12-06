from django.urls import path
from . import views
urlpatterns = [
    path('',views.showData),
    path('adddata.html',views.addData),
    
]