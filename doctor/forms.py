from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets = {
            'ID': forms.TextInput(attrs={'class': 'form-control', 'id':'ID'}),
            'Number': forms.TextInput(attrs={'class': 'form-control', 'id':'Number'}),
            'Animal': forms.TextInput(attrs={'class': 'form-control', 'id':'Animal'}),
            'Species': forms.TextInput(attrs={'class': 'form-control', 'id':'Species'}),
            'Sex': forms.TextInput(attrs={'class': 'form-control', 'id':'Sex'}),
            'Neuter': forms.TextInput(attrs={'class': 'form-control', 'id':'Neuter'}),
            'Age': forms.TextInput(attrs={'class': 'form-control', 'id':'Age'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'id':'Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'id':'Phone'}),
            'Addr': forms.TextInput(attrs={'class': 'form-control', 'id':'Addr'}),
            'Doctor': forms.TextInput(attrs={'class': 'form-control', 'id':'Doctor'}),
        }
        labels = {"Number": 'Number', "Animal": 'Animal',
                  'Species': 'Species', 'Sex': 'Sex',
                  'Neuter': 'Neuter', 'Age': 'Age',
                  'Name': 'Name', 'Phone': 'Phone',
                  'Addr': 'Addr', 'ID': 'ID', 'Doctor': 'Doctor'}
