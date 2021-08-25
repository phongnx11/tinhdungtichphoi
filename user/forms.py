from django.contrib.auth.forms import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs=
        {'multiple': True, 'webkitdirectory': True, 'directory': True}))