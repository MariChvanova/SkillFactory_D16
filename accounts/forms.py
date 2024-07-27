from django import forms
from allauth.account.forms import SignupForm
from django.core.mail import send_mail



class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        send_mail(
            subject='Добро пожаловать!',
            message=f'Рады приветствовать, {user.username}, Вы успешно зарегистрировались на сайте!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )
        return user

class FormCode(forms.Form):
    code = forms.IntegerField(label="Код для регистрации")