from rest_framework import serializers
from users.models import User
from issues.models import Issue


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

