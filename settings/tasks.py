from celery import shared_task
from django.conf import settings

from settings.models import Settings
from django.core.mail import send_mail

@shared_task
def send_mail_task(subject, name, email, message):
    print('Working ----------------------')
    send_mail(
        subject,
        f'message from {name} \n email : {email} \n Message : {message}',
        email,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
