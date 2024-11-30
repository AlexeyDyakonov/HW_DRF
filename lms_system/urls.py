from django.urls import path
from rest_framework.routers import SimpleRouter

from lms_system.apps import LmsSystemConfig
from lms_system.views import (CourseViewSet, LessonCreateApiView,
                              LessonDestroyApiView, LessonListApiView,
                              LessonRetrieveApiView, LessonUpdateApiView)

app_name = LmsSystemConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/",
         LessonListApiView.as_view(),
         name="lesson_list"
         ),
    path(
        "lessons/<int:pk>/retrieve/",
        LessonRetrieveApiView.as_view(),
        name="lesson_retrieve",
    ),
    path("lessons/create/",
         LessonCreateApiView.as_view(),
         name="lesson_create"
    ),
    path(
        "lessons/<int:pk>/delite/",
        LessonDestroyApiView.as_view(),
        name="lesson_delite",
    ),
    path(
        "lessons/<int:pk>/update/",
        LessonUpdateApiView.as_view(),
        name="lesson_update"
    ),
]

urlpatterns += router.urls
