from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(username, email):
    send_mail(
        subject='Welcome!',
        message=f'Hello {username}, thank you for registering!',
        from_email='noreply@example.com',
        recipient_list=[email],
        fail_silently=False,
    )
