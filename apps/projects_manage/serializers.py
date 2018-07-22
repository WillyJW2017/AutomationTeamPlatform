from rest_framework import serializers

from .models import Projects, Sprints, Releases, Story, TestCases, SubTestCases

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

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Releases
        fields = ('id', 'name', 'project', 'startDate', 'endDate')

class ReleaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Releases
        fields = ('name', 'startDate', 'endDate')

class StorySerializer(serializers.ModelSerializer):
    # sprint = serializers.CharField(source='sprint.name')
    # release = serializers.CharField(source='release.name')
    id = serializers.CharField(source='story_id')
    class Meta:
        model = Story
        fields = ('id', 'summary', 'project', 'sprint', 'release', 'assignee')


class StoryUpdateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('sprint', 'release')

class SubTestCaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTestCases
        fields = ('application', 'os', 'platform', 'country', 'storyId', 'status', 'result')

class TestCaseSerializer(serializers.ModelSerializer):
    subcases = SubTestCaseInfoSerializer(many=True)
    class Meta:
        model = TestCases
        fields = '__all__'

class SubTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTestCases
        fields = '__all__'

class TestCaseInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCases
        fields = ('name', 'functionArea', 'framework', 'application', 'tag', 'description')