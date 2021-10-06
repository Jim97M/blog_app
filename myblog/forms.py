from django import forms
from django.db.models import fields

from myblog.models import Comment
class EmailForm(forms.Form):
    name = forms.CharField(max_length=50)
    to = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')