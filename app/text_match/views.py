from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils.helper import calculate_matching_percentage

import csv


@api_view(['GET'])
def get_key(request):
    response_list = list()

    with open("Dummy_medical_dataset.csv", 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader: 
           response_list.append(row.get('Key'))
    
    return Response({"keys": response_list}, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_values(request):
    file = open("Dummy_medical_dataset.csv", 'r')
    csvreader = csv.DictReader(file)
    payload = request.data.get('key')
    
    response_list = list()
    
    for row in csvreader:
        percentage = calculate_matching_percentage(payload, row.get('Values'))
        if percentage > 50 and row.get('Values'):
                response_list.append((row.get('Values'), percentage))
    
    if response_list:
        return Response({f"{payload}": response_list}, status=status.HTTP_200_OK)
    else:
        return Response("No match found", status=status.HTTP_404_NOT_FOUND)
