from django.contrib import admin

from lms_system.models import Course, Lesson
from users.models import Payment, User


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = (
        "id",
        "name",
        "preview",
        "description",
        "owner",
    )
    list_display = (
        "id",
        "name",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    search_fields = (
        "id",
        "name",
        "preview",
        "description",
        "owner",
    )
    list_display = (
        "id",
        "name",
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = (
        "email",
        "phone",
        "city",
        "avatar",
    )
    list_display = (
        "id",
        "email",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = (
        "user",
        "date",
        "course",
        "lesson",
        "amount",
        "method",
    )
    list_display = (
        "user",
        "amount",
        "method",
    )
