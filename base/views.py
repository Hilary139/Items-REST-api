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
    }
    return Response(api_urls, status.HTTP_200_OK)



@api_view(['GET', 'POST'])
def getItems(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  



@api_view(['GET', 'PUT', 'DELETE'])
def itemDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)