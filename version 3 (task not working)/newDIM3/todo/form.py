from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todo.models import Task, List, Group

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('list_name', 'group')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'date_due', 'assigned_to')
