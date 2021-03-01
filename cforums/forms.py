from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()