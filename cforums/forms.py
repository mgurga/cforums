from django import forms
from django.conf import settings

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)

    def clean_image(self):
        image = self.cleaned_data["image"]
        if image:
            if image.size > settings.UPLOADSIZELIMIT:
                raise forms.ValidationError("Image too large, max size: " + settings.UPLOADSIZELIMIT)
            return image