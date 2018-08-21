from django import forms
from .models import Car, Comment

class CarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = ('make', 'model', 'year', 'img_url')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('comment', 'car')
