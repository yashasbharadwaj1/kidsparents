from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/',views.post_search,name='post_search'),
    path('searchbloodbanks/',views.bloodbank_search,name='bloodbank_search'),
    path('searchblooddonors/',views.blooddonor_search,name='blooddonar_search'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]
