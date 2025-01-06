from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    tokens = models.IntegerField(default=4000)

    # Add related_name arguments to resolve the clash
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='chat_user_set',
        related_query_name='chat_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='chat_user_set',
        related_query_name='chat_user',
    )

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField(default="Default response")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message[:20]}'