from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):

    username = forms.CharField(max_length=120)
    email = forms.EmailField()

    def get_info(self):
        """
        Метод, который возвращает форматированную информацию
        """
        subject = 'Token'

        msg = 'Ваш токен: 2283221488'

        return subject, msg

    def send(self):
        """
        Метод, который отправляет сообщения
        """

        subject, msg = self.get_info()

        cl_data = super().clean()
        from_email = cl_data.get('email')

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email]
        )
