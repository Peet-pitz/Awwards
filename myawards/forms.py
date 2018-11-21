from django import forms
from .models import Project,Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['link','description','profile','image','title']