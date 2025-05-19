from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goal, Step
from .serializers import GoalSerializer, StepSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({'message': "Hello World"})





