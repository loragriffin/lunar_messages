from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    # overwrites model field with this custom form field
    # widget modifies how CharField is displayed
    message = forms.CharField(max_length=500, min_length=5, widget=forms.Textarea)

    class Meta:
        model = Post
        fields = [
            "user",
            "message"
        ]
