from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)