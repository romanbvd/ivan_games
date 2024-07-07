from django.urls import path
from games_info import views
 
urlpatterns = [
    path('', views.index, name='home'),
]