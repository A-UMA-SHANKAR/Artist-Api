

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, WorkViewSet
from .views_api import get_works, register_user  # Import the new API view
from .views import UserRegistrationView,TokenObtainPairAndUserInfoView, UserLoginView
from . import views

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('token/', TokenObtainPairAndUserInfoView.as_view(), name='token-obtain-pair'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('works/', get_works, name='get_works'), 
    path('ls', views.StudentList.as_view(), name='student_list'),
    path('view/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
    path('new', views.StudentCreate.as_view(), name='student_new'),
    path('edit/<int:pk>', views.StudentUpdate.as_view(), name='student_edit'),
    path('delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
]
