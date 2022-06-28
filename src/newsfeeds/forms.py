from django.forms import ModelForm
from .models import Post

class MyForm(ModelForm):
    class Meta:
        model = Post
        fields = [  
            'fname',
            'lname',
            'oname',
            'planguage',
            'university',
            'resume',
            'mail',
            'more',
        ]