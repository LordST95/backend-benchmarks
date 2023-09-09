from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password

from accounts.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = ['password', 'groups']
        depth = 2


class CreateUpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Member
        fields = ['username', 'email', 'first_name' ,'last_name', 'password']

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
