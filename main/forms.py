from django import forms

class FlashcardSetForm(forms.Form):
    setname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_input'}))
    ersteller = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form_input'}))
    passwort = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    beschreibung = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form_input', 'rows': 3}))

class FlashcardForm(forms.Form):
    value_a = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form_input', 'rows': 3}), label='')
    value_b = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form_input', 'rows': 3}), label='')

class EditFlashcardSetForm(forms.Form):
    setname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_input'}))
    ersteller = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form_input'}))
    passwort = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class': 'form_input'}))

class SearchFlashcardSetForm(forms.Form):
    setname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_input'}))
    ersteller = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form_input'}))
