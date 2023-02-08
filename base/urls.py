from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.apiOverview, name='ApiOverview'),
    path('getItems/', views.getItems, name='GetItems'),
    path('itemDetail/<str:pk>/', views.itemDetail, name='ItemDetail'),
]
 
urlpatterns = format_suffix_patterns(urlpatterns)
