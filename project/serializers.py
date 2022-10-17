from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #el parametro id se crea por defecto, se puede confirmar en migrations
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )
