from django.urls import path
from . import views



app_name = 'account'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    
                                                        
    path('profile/', views.profile, name='profile'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),                                                                                                                                                                                                                                                                                     
    path('profile/favourites/', views.favourite_list, name='favourite_list'),
 
]