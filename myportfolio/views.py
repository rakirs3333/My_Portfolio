from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .models import Projects,Contact,Skills
from .serializers import ProjectSerializer,SkillsSerializer


# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Projects.objects.all()
    serializer_class=ProjectSerializer

class ContactView(APIView):
    def post(self,request,*args,**kwargs):
        name=request.data.get("name")
        email=request.data.get("email")
        message=request.data.get("message")

        if name and email and message:
            Contact.objects.create(name=name,email=email,message=message)
            return Response({"success":"Message sent!"},status=status.HTTP_201_CREATED)
        return Response({"error":"All fields are required"},status=status.HTTP_404_BAD_REQUEST)


class SkillsView(viewsets.ModelViewSet):
    queryset=Skills.objects.all()
    serializer_class=SkillsSerializer
    def create(self,request,*args,**kwargs):
        name=request.data.get("name")
        percentage=request.data.get("percentage")
        image=request.data.get("image")
        if Skills.objects.filter(name=name,percentage=percentage).exists():
            raise ValidationError("Skills already present")
        
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            skills=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
        
    
