from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user
from .serializers import ItemSerializer

# Create your views here.





class UserView(APIView):
    def get(self, request):
        items = user.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
  


def deleteuser(request):

    return HttpResponse("time to delet user")


def adduser(request):

    return HttpResponse("time to adduser ")



