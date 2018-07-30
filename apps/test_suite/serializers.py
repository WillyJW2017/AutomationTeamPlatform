from rest_framework import serializers

from .models import TestSuite, TestSuiteResult, SubTestCaseResult


class TestSuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuite
        fields = '__all__'

class SubTestCaseResultSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='case_name.case_name')
    class Meta:
        model = SubTestCaseResult
        fields = '__all__'

class TestSuiteResultSerializer(serializers.ModelSerializer):
    details = SubTestCaseResultSerializer(many=True)
    config = serializers.CharField(source='suiteId.config')
    class Meta:
        model = TestSuiteResult
        fields = '__all__'

