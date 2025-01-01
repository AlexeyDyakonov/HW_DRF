from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    """Модель курса"""

    name = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="course_previews/",
        verbose_name="Превью курса",
        **NULLABLE,
        help_text="Загрузите превью курса"
    )
    description = models.TextField(
        verbose_name="Описание курса", **NULLABLE, help_text="Введите описание курса"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец",
        related_name="course"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель урока"""

    name = models.CharField(
        max_length=150,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", **NULLABLE, help_text="Введите описание урока"
    )
    preview = models.ImageField(
        upload_to="lessons_previews/",
        verbose_name="Превью урока",
        **NULLABLE,
        help_text="Загрузите превью урока"
    )
    video_url = models.URLField(
        verbose_name="Видеоурок", **NULLABLE, help_text="ссылка на видео"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="lessons",
        **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец",
        related_name="lesson"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = (
            "name",
            "course",
        )


class Subscription(models.Model):
    """Модель подписки"""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="subscription",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="subscription",
    )
    sign_up = models.BooleanField(
        default=False,
        verbose_name="Подписка"
    )

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
