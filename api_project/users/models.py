from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Данный класс унаследован от встроенного в Django
    класса абстрактного юзера. Если переключатмя к AbstractUser
    Ctrl+LClick - в нем есть все необходимые поля.
    Для сооствествия части задания перепопределяеься
    поле email и добавляется поле bio.'''
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

# Эта модель лишь пример или основа того, что просят в задании.