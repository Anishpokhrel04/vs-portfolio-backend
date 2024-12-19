from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Experience
from .serializers import ExperienceSerializer

# List all experiences or create a new experience
@api_view(['GET', 'POST'])
def experience_list_create(request):
    if request.method == 'GET':
        # List all experiences
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new experience
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a specific experience
@api_view(['GET', 'PUT', 'DELETE'])
def experience_detail(request, pk):
    experience = get_object_or_404(Experience, pk=pk)

    if request.method == 'GET':
        # Retrieve a specific experience
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update a specific experience
        serializer = ExperienceSerializer(experience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete a specific experience
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
