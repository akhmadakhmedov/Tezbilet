from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=25, label="Имя пользователя")
    password = forms.CharField(max_length=50, label="Пароль", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50, label="Подтвердите пароль", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password!=confirm:
            raise forms.ValidationError("Ваш пароль не соответствует")
        values = {
            "username": username,
            "password": password
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
