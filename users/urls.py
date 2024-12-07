from django.urls import path

from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserListApiView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", PaymentViewSet, basename="payments")

urlpatterns = [
    path(
        "user/",
        UserListApiView.as_view(),
        name="users_list"
    ),
    path(
        "user/register/",
        UserCreateAPIView.as_view(),
        name="register"),
    path(
        "user/<int:pk>/retrieve/",
        UserRetrieveAPIView.as_view(),
        name="users_retrieve"
    ),
    path(
        "user/<int:pk>/update/",
        UserUpdateAPIView.as_view(),
        name="users_update"),
    path(
        "user/<int:pk>/delite/",
        UserDestroyAPIView.as_view(),
        name="users_delite"),
]

urlpatterns += router.urls
