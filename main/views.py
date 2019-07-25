from django.shortcuts import render
from .serializers import FileSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

#APIView allow us to handel post and get requests

class FileView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    #to make the data into a for befor sending out to the web 

    #say what to do when there is a post request to our django website through our API
    def post(self, request, *args, **kwargs):
        
        # Create a serializer for the data we want to post.
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():

            #This does the HTTP POST request 
            file_serializer.save()

            #just get the status code from our website 
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
