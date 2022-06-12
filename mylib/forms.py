from django import forms
from .models import Book


class BookRegistration(forms.ModelForm):
 class Meta:
  model = Book
  fields = ['bookname', 'authorname']
  widgets = {
   'bookname': forms.TextInput(attrs={'class':'form-control'}),
   'authorname': forms.TextInput(attrs={'class':'form-control'}),
   
  }