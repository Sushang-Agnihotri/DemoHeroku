from django.shortcuts import render
from .models import demomodel
from .serializers import demoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class DemoAPIView(APIView):
    serializer_class = demoSerializer
    def post(self, request, format=None):
        serializer = demoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
        		'status' : True,
        		'message' : 'Success',
        		'list' : serializer.data})
                
        else :
            return Response({
	    		'status' : False,
	    		'message' : 'Error!',})
