from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form to post a new titbit
    """
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Post the news :-)',
        })
    )

    class Meta:
        model = Post
        fields = ['content']
