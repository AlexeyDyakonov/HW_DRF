from rest_framework.serializers import ModelSerializer

from lms_system.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор модели Курс"""

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    """Сериализатор модели Урок"""

    class Meta:
        model = Lesson
        fields = "__all__"