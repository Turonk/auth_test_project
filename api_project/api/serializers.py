from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Обратите внимания импорт идет как дефолтного юзера
# но использоваться будем вами переопределенный.
User = get_user_model()

# Оба сериализатора не зависят от моделей.
class SingUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # def validate_username(self, value):
    #   тут можно провалидировать имена пользователей.


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

# Сериализатор для вывода всех полей нашего кастомного юзера
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'