from rest_framework import serializers

from .models import Projects, Sprints

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprints
        fields = ('id', 'name', 'project', 'startDate', 'endDate')

class SprintInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprints
        fields = ('name', 'startDate', 'endDate')
