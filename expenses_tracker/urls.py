from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("expenses/", include("expenses.urls")),
    path("admin/", admin.site.urls),
]
