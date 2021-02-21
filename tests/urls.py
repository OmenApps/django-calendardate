from django.conf import settings
from django.contrib import admin
from django.urls import path


app_name = "django_calendardate"

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
