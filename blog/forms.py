from django import forms
from tinymce.widgets import TinyMCE

from .models import Post


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30, 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'onchange': 'image_onchage(this)'})
        self.fields['title'].widget.attrs.update({'placeholder': 'Введите название статьи'})

    class Meta:
        model = Post
        fields = ('title', 'image', 'content')
        # widgets = {
        #     'image': forms.ImageField(attrs={'onload': ''})
        # }
