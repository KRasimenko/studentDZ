from django import forms
from .models import CustomUser, Group

class RegistrationForm(forms.ModelForm):
    """Форма регистрации пользователя"""
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        """Мета класс для формы регистрации пользователя"""
        model = CustomUser
        fields = ['role', 'full_name', 'group', 'username', 'password']
    
    def clean(self):
        """Очистка данных формы"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data