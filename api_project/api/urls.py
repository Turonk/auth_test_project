from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserSignUp, TokenView, UserViewSet

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet)


urlpatterns = [
    path('signup/', UserSignUp.as_view()),
    path('token/', TokenView.as_view()),
    path('v1/', include(v1_router.urls))
]
