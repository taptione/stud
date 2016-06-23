# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from students.settings import ADMIN_EMAIL


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label=u"Ваша Емейл Адреса")

    subject = forms.CharField(
        label=u"Заголовок листа",
        max_length=128)
    message = forms.CharField(
        label=u"Текст повідомлення",
        widget=forms.Textarea)

def contact_admin(request):
    # check whether user data is valid
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            #send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = u'Під час відправки виникла непередбачувана помилка. Спробуйте скористайтесь даною формою пізніше'
            else:
                message = u'Повідомлення успішно надіслане!'

        # redirect 2 same ontact page with success  message
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})