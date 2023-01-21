# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Post


# create a ModelForm
class Posts(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Post
        fields = "__all__"