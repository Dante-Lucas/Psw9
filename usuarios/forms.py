from django import forms


class CadastroForm(forms.Form):
    username = forms.CharField(label="Username", max_length = 100, widget = forms.TextInput(attrs={'class': 'input-form', 'placeholder': 'Nome do usuário...'}))
    email = forms.EmailField(label="Email", max_length = 320, widget = forms.EmailInput(attrs={'class': 'input-form', 'placeholder': 'Email...'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': 'Senha...'}))
    confirm_password = forms.CharField(label="Confirmar senha", widget = forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': 'Confirme a senha...'}))
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget = forms.TextInput(attrs={'class': 'input-form', 'placeholder': 'Nome do usuário...'}))
    password = forms.CharField(label="Senha", widget = forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': 'Sua senha...'}))
