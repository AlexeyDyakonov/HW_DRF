from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyAPIView,
                         UserListApiView, UserRetrieveAPIView,
                         UserUpdateAPIView, PaymentCreateAPIView)

app_name = UsersConfig.name

router = SimpleRouter()
#router.register("", PaymentViewSet, basename="payments")


class PaymentListAPIView:
    pass


urlpatterns = [
    path(
        "user/",
        UserListApiView.as_view(),
        name="users_list"
    ),
    path(
        "user/register/",
        UserCreateAPIView.as_view(),
        name="register"
    ),
    path(
        "user/<int:pk>/retrieve/",
        UserRetrieveAPIView.as_view(),
        name="users_retrieve"
    ),
    path(
        "user/<int:pk>/update/",
        UserUpdateAPIView.as_view(),
        name="users_update"
    ),
    path(
        "user/<int:pk>/delite/",
        UserDestroyAPIView.as_view(),
        name="users_delite"
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path(
        "payment/",
        PaymentCreateAPIView.as_view(),
        name="payment_create"
    ),
]

urlpatterns += router.urls
