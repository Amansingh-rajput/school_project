from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = [
            "name",
            "address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_new_school', 'Add new School'))
        self.helper.layout = Layout(
            Row(
                Column('name'),
            ),
            Row(
                Column('address'),
            ),)

class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = [
            "name",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_new_standard', 'Add new Standard'))
        self.helper.layout = Layout(
            Row(
                Column('name'),
            ),)
           

class teacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "name",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('add_new_teacher', 'Add new Teacher'))
        self.helper.layout = Layout(
            Row(
                Column('name'),
            ),)