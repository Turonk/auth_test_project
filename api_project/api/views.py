from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny

from .serializers import SingUpSerializer, TokenSerializer, UserSerializer

# Используется катосный юзер, а вызывается как старндатный.
User = get_user_model()

# Использовать именно так не обязательно
# есть масса вариантов - это один из...
# https://www.django-rest-framework.org/api-guide/views/
class UserSignUp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SingUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Достаём данные из сериализатора.
        email = serializer.data['email']
        username = serializer.data['username']
        # Используем специальную конструкцию.
        # Удобно, т.к. если пользователь уже создан
        # просто запишется объект из базы.
        user, created = User.objects.get_or_create(email=email, username=username)
        # Тут по желанию -- а данном случае стандартный генератор.
        code = default_token_generator.make_token(user)
        # С отправкой уже сами.
        print(code)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.data.get('username')
        confirmation_code = serializer.data.get('confirmation_code')

        user = get_object_or_404(User, username=username)

        
        # Тут по идее надо проверить что confirmation_code пренадлежит юзеру
        # тогда создавать код доступа, а иначе выдавать HTTP_400_BAD_REQUEST.
        # Но в примере упрощено.
        token = AccessToken.for_user(user)
        return Response(
            {'token': str(token)}, status=status.HTTP_200_OK
        )

# Класс создан для только для того чтобы вывести пользователей
# и их поля, и показать что пользователи кастомные.
# Например есть поле bio.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


