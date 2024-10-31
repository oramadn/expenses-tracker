from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('api/expenses/', include('expenses.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
] + debug_toolbar_urls()
