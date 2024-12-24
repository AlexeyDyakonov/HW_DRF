from django.urls import path
from rest_framework.routers import SimpleRouter

from lms_system.apps import LmsSystemConfig
from lms_system.views import (CourseViewSet, LessonCreateApiView,
                              LessonDestroyApiView, LessonListApiView,
                              LessonRetrieveApiView, LessonUpdateApiView, SubscriptionCreateAPIView,
                              SubscriptionListAPIView)

app_name = LmsSystemConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path(
        "lessons/",
         LessonListApiView.as_view(),
         name="lesson-list"
    ),
    path(
        "lessons/<int:pk>/",
        LessonRetrieveApiView.as_view(),
        name="lesson-retrieve",
    ),
    path(
        "lessons/create/",
         LessonCreateApiView.as_view(),
         name="lesson-create"),
    path(
        "lessons/<int:pk>/delite/",
        LessonDestroyApiView.as_view(),
        name="lesson-delite",
    ),
    path(
        "lessons/<int:pk>/update/",
        LessonUpdateApiView.as_view(),
        name="lesson-update"
    ),
    path(
        "subscription/create/",
        SubscriptionCreateAPIView.as_view(),
        name="subscription-create",
    ),
    path(
        "subscription/",
         SubscriptionListAPIView.as_view(),
         name="subscriptions"
    ),
]


urlpatterns += router.urls
