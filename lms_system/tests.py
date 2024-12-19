from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from lms_system.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@test1.com", password="qwerty")
        self.course = Course.objects.create(name="Test1", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Test1", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms_system:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"),
            self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("lms_system:lesson-create")
        data = {
            "name": "Test2"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.count(),
            2
        )

    def test_lesson_update(self):
        url = reverse("lms_system:lesson-update", args=(self.lesson.pk,))
        data = {
            "name": "Python",
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"),
            "Python"
        )

    def test_lesson_delete(self):
        url = reverse("lms_system:lesson-delite", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.count(),
            0
        )

    def test_lesson_list(self):
        url = reverse("lms_system:lesson-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": "Test1",
                    "description": None,
                    "preview": None,
                    "video_url": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data,
            result
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@test.com", password="qwerty")
        self.course = Course.objects.create(name="Java", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        video_url = reverse("lms_system:subscription-create")
        data = {
            "course": self.course.pk,
        }
        response = self.client.post(video_url, data)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Subscription.objects.count(),
            1
        )
        self.assertEqual(
            data,
            {"message": "Подписка создана"}
        )

    def test_subscription_delete(self):
        video_url = reverse("lms_system:subscription-create")
        data = {
            "course": self.course.pk,
        }
        Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.post(video_url, data)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Subscription.objects.count(),
            0
        )
        self.assertEqual(
            data,
            {"message": "Подписка удалена"}
        )
