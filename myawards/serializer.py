from rest_framework import serializers
from .models import Project
from .models import Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','image', 'description', 'link', 'profile')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','image', 'description', 'link', 'profile')