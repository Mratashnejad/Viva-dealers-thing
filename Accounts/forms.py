
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

STATES = (
    ('', 'Armenia'),
    ('Ir', 'Iran'),
    ('Ru', 'Russia'),
    ('En', 'England')
)


class RegisterForm(UserCreationForm):

    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Row(
            Column('email', css_class='form-group col-md-6 mb-0'),
            Column('password', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        'address_1',
        'address_2',
        Row(
            Column('city', css_class='form-group col-md-6 mb-0'),
            Column('state', css_class='form-group col-md-4 mb-0'),
            Column('zip_code', css_class='form-group col-md-2 mb-0'),
            css_class='form-row'
        ),
        'check_me_out',
        Submit('submit', 'Sign in')
    )


class Meta:
    model = User
    fields = ["username", "email",
              "password1", "password2"]
