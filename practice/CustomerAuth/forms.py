from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from CustomerAuth.models import Cusomter

class RegistrationForm(ModelForm):
        username    = forms.CharField(label=(u'User Name'))
        email       = forms.EmailField(label=(u'Email Address'))
        password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1   = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

        class Meta:
                model = Cusomter
                exclude =  ('user',)
        def clean_username(self):
            username = self.cleaned_data['username']
            print username
            try:
                    User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError("that username is already taken, please select another")

        def clean_password(self):
            password1 = self.cleaned_data['password1']
            password  = self.cleaned_data['password']
            print password

            print password1
            if password != password1:
                raise forms.ValidationError("The passwords did not match , Please try again")
            return password




