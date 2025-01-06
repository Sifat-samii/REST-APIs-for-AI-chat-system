from django.urls import path
from .views import UserRegistrationView, UserLoginView, ChatView, TokenBalanceView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('tokens/', TokenBalanceView.as_view(), name='tokens'),
]