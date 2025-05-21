from django.db.migrations import AlterModelOptions
from rest_framework import serializers
from .models import *

class GoalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'email',
            ' password',

        ]


class StepSerializer(serializers.ModelSerializer):
    goal = GoalSerializer()
    class Meta:
        model = Step
        fields = "__all__"


