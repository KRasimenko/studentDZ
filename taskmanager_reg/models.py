from django.contrib.auth.models import AbstractUser
from django.db import models

class Group(models.Model):
    """Группа студентов. Нужен для связи между пользователями и заданиями"""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """Возвращает имя группы"""
        return self.name

class CustomUser(AbstractUser):
    """Пользователь. Нужен для связи между пользователями и заданиями"""
    ROLES = (
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
    )
    
    role = models.CharField(max_length=10, choices=ROLES)
    full_name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        """Возвращает имя пользователя"""
        return f"{self.full_name} ({self.get_role_display()})"