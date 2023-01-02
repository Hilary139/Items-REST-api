from rest_framework.response import Response
from rest_framework.decorators import api_view
from  base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Get All Items' : '/getItems/',
        'Single Item Detail' : '/itemDetail/<str:pk>/',
        'Create Item ' : '/addItem/',
        'Update Item ' : '/updateItem/<str:pk>/',
        'Delete Item ' : '/deleteItem/<str:pk>/',
    }
    return Response(api_urls)


#* Get all Items
@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)


#* Get Item Detail
@api_view(['GET'])
def itemDetail(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, many = False)
    return Response(serializer.data)


#* Create Items
@api_view(['POST'])
def addItem(request): 
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#* Update Item
@api_view(['POST'])
def updateItem(request, pk): 
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item,  data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    


#* Delete Item
@api_view(['DELETE'])
def deleteItem(request, pk): 
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("Item deleted successfully!!")    
