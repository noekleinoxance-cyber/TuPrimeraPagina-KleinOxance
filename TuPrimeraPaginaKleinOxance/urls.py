from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path(
        "accounts/logout/",
        LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
]
