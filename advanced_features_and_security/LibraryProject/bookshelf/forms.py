from django import forms

ExampleForm
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
