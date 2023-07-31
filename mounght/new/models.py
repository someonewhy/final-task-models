from django.db import models
from ckeditor.fields import RichTextField


class User(models.Model):
    username = models.CharField(max_length=50)  # Поле с именем пользователя
    email = models.EmailField()  # Поле с адресом электронной почты

    def __str__(self):
        return self.username
CATEGORIES = [
    'Танки',
    'Хилы',
    'ДД',
    'Торговцы',
    'Гилдмастеры',
    'Квестгиверы',
    'Кузнецы',
    'Кожевники',
    'Зельевары',
    'Мастера заклинаний',
]

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')  # Внешний ключ, связывающий сообщение с отправителем
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')  # Внешний ключ, связывающий сообщение с получателем
    content = models.TextField()  # Поле с содержанием сообщения
    sent_date = models.DateTimeField(auto_now_add=True)  # Поле с датой отправки сообщения

    def __str__(self):
        return f"From: {self.sender.username}, To: {self.receiver.username}"
