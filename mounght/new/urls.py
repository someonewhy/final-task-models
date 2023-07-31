from django.urls import path
from .views import PostDetailView, MessageCreateView,post_list,user_messages,PostCreateView

app_name = 'new'

urlpatterns = [
    # ... другие URL-шаблоны вашего приложения ...
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/send_message/', MessageCreateView.as_view(), name='send_message'),
    path('post_list/', post_list, name='post_list'),
    path('user_messages/',user_messages, name='user_messages'),
    path('post/create/',PostCreateView.as_view(), name='post_create'),
]
