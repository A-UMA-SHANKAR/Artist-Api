
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer
from rest_framework import permissions

from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, TokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student

# Create your views here.

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('templates/student_list.html')

class StudentUpdate(UpdateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('templates/student_list.html')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('templates/student_list.html')


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Generate token
        user = serializer.instance
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response_data = {
            'user_id': user.id,
            'username': user.username,
            'access_token': access_token,
            'is_staff': user.is_staff,
        }

        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data['refresh']
        access = response.data['access']
        user_id = self.user.id  # Assuming the user attribute is present in the view
        response.data['user_id'] = user_id

        # Store the refresh token in a cookie
        response.set_cookie('refresh_token', refresh, httponly=True, samesite='None', secure=True)

        return response

class TokenObtainPairAndUserInfoView(TokenObtainPairView):
    serializer_class = TokenSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]



