from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from  base.models import Item
from .serializers import ItemSerializer
from rest_framework.parsers import JSONParser 



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
'''
@api_view(['GET'])
def getItems(request):
    if request.method == 'GET':
        try:    
            items = Item.objects.all()
        except:
            return Response({
            "error": "Items Not Found"
            }, status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(items, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response(serializer.error, status.HTTP_400_BAD_REQUEST)
'''

#* Create Items
@api_view(['GET','POST'])
def getItems(request, format=None):

    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        serializer = ItemSerializer(data=item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


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



