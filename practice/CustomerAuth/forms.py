from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Submit

class RegistrationForm(forms.Form):
        username    = forms.CharField(label=(u'User Name'))
        email       = forms.EmailField(label=(u'Email Address'))
        password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1   = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

        def __init__(self , *args , **kwargs):
            super(RegistrationForm,self).__init__(*args,**kwargs)
            self.helper= FormHelper()
            self.helper.form_class='col-lg-6 col-sm-4'
            self.helper.add_input(Submit('submit', 'Submit'))
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-3'
            self.helper.field_class = 'col-lg-8'








