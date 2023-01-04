from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from  base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Get All Items' : '/getItems/',
        'Single Item Detail' : '/itemDetail/<str:pk>/',
        'Select, Update, Delete Single Item' : '/itemMakeChange/<str:pk>/',
        'Create Item ' : '/addItem/',
        'Update Item ' : '/updateItem/<str:pk>/',
        'Delete Item ' : '/deleteItem/<str:pk>/',
    }
    return Response(api_urls, status.HTTP_200_OK)


#* Get all Items
@api_view(['GET'])
def getItems(request):
    if request.method == 'GET':
        try:    
            items = Item.objects.all()
        except:
            return Response({
            "error": "Books Not Found"
            }, status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(items, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response(serializer.error, status.HTTP_400_BAD_REQUEST)


#* Get Item Detail
@api_view(['GET'])
def itemDetail(request, pk):
    if request.method == 'GET':
        try:
            items = Item.objects.get(id=pk)
        except:
            return Response({
                "error": "Invalid book id"
            }, status.HTTP_404_NOT_FOUND)    

        serializer = ItemSerializer(items, many = False)
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response(serializer.error, status.HTTP_400_BAD_REQUEST)


#* Get Item, Update, or Delete item
@api_view(['GET', 'PUT', 'DELETE'])
def itemMakeChanges(request, pk):
    if request.method == 'GET':
        try:
            item = Item.objects.get(id = pk)
        except:
            return Response({
                "error": "Not Item Found"
            }, status.HTTP_404_NOT_FOUND)    

        serializer = ItemSerializer(item, many = False)
        return Response(serializer.data, status.HTTP_200_OK)

#* update item request
    if request.method == "PUT":
        try:
            item = Item.objects.get(id=pk)
        except:
            return Response({
                "error": "Not able to make changes to Item"
            }, status.HTTP_403_FORBIDDEN)  

        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)  
        return Response(serializer.error, status.HTTP_400_BAD_REQUEST)

#* delete item request
    if request.method == 'DELETE':
        item.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#* Create Items
@api_view(['POST'])
def addItem(request): 
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(status.HTTP_400_BAD_REQUEST)    


#* Update Item
@api_view(['POST'])
def updateItem(request, pk): 
    if request.method == 'POST':
        try:
            item = Item.objects.get(id=pk)
        except:
            return Response({
                "error": "Unable to update item"
            },status.HTTP_400_BAD_REQUEST)  

    serializer = ItemSerializer(instance=item,  data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)    
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#* Delete Item
@api_view(['DELETE'])
def deleteItem(request, pk):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(id=pk)
        except:
            return Response({
                "error": "Unable to delete item"
            }, status.HTTP_400_BAD_REQUEST)    
    item.delete()
    return Response("Item deleted successfully!!", status.HTTP_200_OK)    
