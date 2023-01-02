from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='ApiOverview'),
    path('addItem/', views.addItem, name='AddItem'),
    path('getItems/', views.getItems, name='GetItems'),
    path('itemDetail/<str:pk>/', views.itemDetail, name='ItemDetail'),
    path('updateItem/<str:pk>/', views.updateItem, name='UpdateItem'),
    path('deleteItem/<str:pk>/', views.deleteItem, name='DeleteItem'),


]
 