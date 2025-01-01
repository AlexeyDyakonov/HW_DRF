from datetime import timedelta, date
from users.models import User
from celery import shared_task

@shared_task
def check_last_login():
    users = User.objects.filter(is_active=True, is_staff=False, is_superuser=False, last_login__isnull=False)
    date_delta = timedelta(30)
    for user in users:
        date_block = date.today() - date_delta
        if user.last_login <= date_block:
            print("Пользователь не активен")
            user.is_active = False
            user.save()