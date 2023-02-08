#* Get Item Detail
'''
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



'''



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
