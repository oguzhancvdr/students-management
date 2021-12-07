from django import forms
from .models import Students


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type": "email",
        'class': 'form-control',
        'placeholder': 'Your email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        "type": "tel",
        'placeholder': 'your phone number'
    }))
    gender = forms.CharField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
            choices=(
                ('0', '---------------'),
                ('1', 'Female'),
                ('2', 'Male'),
                ('3', 'Other'),
                ('4', 'Prefer to not say'),
            )))

    number = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        'class': 'form-control',
        'placeholder': 'Your student number',
        "maxlength": "4",
        "minlength": "4",
    }))

    image = forms.FileField(widget=forms.TextInput(attrs={
        "type": "file",
        'class': 'form-control',
        'placeholder': 'image',
        "accept": "image/*",
        "name": 'image'
    },), required=False,)

    class Meta:
        model = Students
        fields = "__all__"
