from rest_framework import serializers
from .models import Projects,Skills

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=["id","title","description","link","created_at"]

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields=["id","name","percentage","image"]