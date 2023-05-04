from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form to post a new titbit
    """
    content = forms.CharField(required=True,
                              label='',
                              widget=forms.widgets.Textarea(attrs={
                                'rows': '3',
                                'placeholder': 'Post the news :-)',
                                'class': 'form-control',
                                }))

    class Meta:
        model = Post
        fields = ['content']


class CommentForm(forms.ModelForm):
    """
    Form to comment a post
    """
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Comment this post :-)',
        })
    )

    class Meta:
        model = Comment
        fields = ['comment']
