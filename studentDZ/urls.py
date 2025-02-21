from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskmanager_reg.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Добавляем стандартные URL для аутентификации
]