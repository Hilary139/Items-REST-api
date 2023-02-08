from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.apiOverview, name='ApiOverview'),
    #path('addItem/', views.addItem, name='AddItem'),
    path('getItems/', views.getItems, name='GetItems'),
    path('itemDetail/<str:pk>/', views.itemDetail, name='ItemDetail'),
    #path('itemMakeChanges/<str:pk>/', views.itemMakeChanges, name='ItemMakeChanges'),
    path('updateItem/<str:pk>/', views.updateItem, name='UpdateItem'),
    path('deleteItem/<str:pk>/', views.deleteItem, name='DeleteItem'),
]
 
urlpatterns = format_suffix_patterns(urlpatterns)
