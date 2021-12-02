from django.forms import ModelForm

from contentapp.models import Content


class ContentCreationForm(ModelForm):
    class Meta:
        model = Content
        fields = ['image', 'title', 'description']