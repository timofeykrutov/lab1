from django import forms
from my_app.models import *


class RegistrForm(forms.ModelForm):
    class Meta:
        model = groups
        fields = ["id_groups", "group_number", "stud"]
        #widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}

class HumanForm(forms.ModelForm):
    class Meta:
        model = teachers
        fields = ["id_teacher", "teacher_fio", "teacher_department"]
        #widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}
