from django import forms

from apps.blog.models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Your number'
        self.fields['message'].widget.attrs['placeholder'] = 'Your message'
