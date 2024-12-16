from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lms_system/", include("lms_system.urls", namespace="lms")),
    path("users/", include("users.urls", namespace="users")),
]
