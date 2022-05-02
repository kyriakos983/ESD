from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from allAccounts.models import User


class RegistserUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    # accountOption = forms.CharField(max_length=50, choices=userChoices.choices, default=None, null=True, blank=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'accountOptions')

    def __init__(self, *args, **kwargs):
        super(RegistserUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
