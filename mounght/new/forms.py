from django import forms
from .models import Message,Post,CATEGORIES

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(category, category) for category in CATEGORIES]