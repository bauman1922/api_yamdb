from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import ContactForm


class ContactView(FormView):
    """
    Метод проверки формы отправялет электронное письмо,
    только если все поля формы действительны
    """

    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Вызывает пользовательский метод отправки
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    """
    Покажет пользователю сообщение об успехе
    """

    template_name = 'contact/success.html'
