from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),
    path('list/', home, name="home"),
    path('add/', entry_change, name="entry_change"),


]
