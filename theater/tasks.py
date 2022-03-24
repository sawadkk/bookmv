from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from book_my_movie import settings

@shared_task(bind=True)
def test_func(self):
    mail_subject = "book_my_show login token"
    message = "book_my_movie one time theater login link:  http://127.0.0.1:8000/theater/test2"
    to_email = "ssawad09@gmail.com"
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
    )
    return "Done"
    #operations
    #for i in range(10):
    #    print(i)
    #return "Done"

@shared_task(bind=True)
def send_mail_func(self,token_user):
    users = get_user_model().objects.filter(username='sawad')
    for user in users:
        mail_subject = "book_my_show login token"
        message = "book_my_movie one time theater login link:  http://127.0.0.1:8000/theater/test2"+token_user+""+user.username
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"

@shared_task(bind=True)
def show_canceled_task():
    users = get_user_model().objects.filter(username='sawad')
    for user in users:
        mail_subject = "show canceled"
        message = "show is canceled"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"