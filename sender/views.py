from django.shortcuts import render
from django.core.mail import EmailMessage

from django.http import HttpResponse

from celery import shared_task

@shared_task
def send():
    subject='Hourly Hydration Alert'
    # to=['anisha24092003@gmail.com'],
    from_email='Water <hellotester4803@gmail.com>'
    to=['vilasmv910@gmail.com']

    body = 'Drink upto 150ml of water immediately!'
    email = EmailMessage(subject, body, from_email, to)
    email.send()