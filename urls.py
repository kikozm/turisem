
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("travel_info.apps.api.urls")),  # Placeholder for API URLs
]
