from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms_system.models import Course, Lesson, Subscription
from lms_system.validators import YouTubeValidator


class LessonSerializer(ModelSerializer):
    """Сериализатор модели Урок"""

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeValidator(field="video_url")]


class CourseSerializer(ModelSerializer):
    """Сериализатор модели Курс"""

    lessons = LessonSerializer(many=True, read_only=True)
    subscription = SerializerMethodField()

    def get_subscription(self, course):
        request = self.context.get("request")
        if not request.user.is_authenticated:
            return False
        return Subscription.objects.filter(user=request.user, course=course).exists()

    class Meta:
        model = Course
        fields = "__all__"

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    """Сериализатор для добавления количества уроков одного курса"""

    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = SerializerMethodField()

    def get_subscription(self, course):
        request = self.context.get("request")
        if not request.user.is_authenticated:
            return False
        return Subscription.objects.filter(user=request.user, course=course).exists()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = "__all__"

