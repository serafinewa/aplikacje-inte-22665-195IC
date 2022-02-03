from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from bzkRestApis.tutorials.models import Tutorial


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):

 @api_view(['GET', 'PUT', 'DELETE'])
 def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE tutorial


@api_view(['GET'])
def tutorial_list_published(request):
    # blad indent expected????
    {}
