from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from lms_system.models import Course, Subscription


@shared_task
def mailing_update_course(course_pk):
    """Функция отправления сообщений об обновлении курса."""
    email_list = []
    course = Course.objects.get(pk=course_pk)
    subs = Subscription.objects.filter(course=course)
    for sub in subs:
        email_list.append(sub.user.email)
    subject_mail = f"Обновление курса {course.name}"
    text_mail = (f"Добрый день, в курсе {course.name} произошли изменения.")
    send_mail(subject_mail, text_mail, settings.EMAIL_HOST_USER, email_list, fail_silently=True)
    print("Письмо отправленно")