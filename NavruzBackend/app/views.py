from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django import http
from django.db.models import Q
from .models import AppUser, ImageModel, TrashBin, BinCategory
from .serializer import AppUserSerializer, ImageModelSerializer, TrashBinSerializer, BinCategorySerializer


class TrashBinsAPIView(APIView):
    serializer_class = TrashBinSerializer

    def get(self, request, *args, **kwargs):
        trashBins = TrashBin.objects.all()
        serializer = self.serializer_class(trashBins, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get("id")
            existingTrashbin = TrashBin.objects.filter(id = id).first()
            if existingTrashbin:
                return Response(self.serializer_class(existingTrashbin).data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AppUserSingleAPIView(APIView):
    serializer_class = AppUserSerializer


    def get_object(self, id: str) -> object:
        try: 
            return AppUser.objects.get(id = id)
        except:
            raise http.Http404

    def get(self, request, id, *args, **kwargs):
        user = self.get_object(id = id)
        serializer = self.serializer_class(user, many = False)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            existing_user = AppUser.objects.filter(id=id).first()
            if existing_user:
                return Response(self.serializer_class(existing_user).data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, format=None):
        id = request.data.get('id')
        existing_user = AppUser.objects.filter(id=id).first()

        if existing_user:
            serializer = self.serializer_class(existing_user, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print("Validation Errors:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    


class BinCategoryAPIView(APIView):
    serializer_class = BinCategorySerializer

    def get(self, request, *args, **kwards):
        categories = BinCategory.objects.all()
        serializer = self.serializer_class(categories, many = True)
        return Response(serializer.data)