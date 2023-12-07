
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer
from rest_framework import viewsets,status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_works(request):
    works = Work.objects.all()
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)

    artist_serializer = ArtistSerializer(user.artist)
    return Response({'user_id': user.id, 'artist': artist_serializer.data}, status=status.HTTP_201_CREATED)