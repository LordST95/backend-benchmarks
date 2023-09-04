from rest_framework import serializers
from django.contrib.auth.models import Permission

from accounts.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = ['password', 'groups']
        depth = 2
