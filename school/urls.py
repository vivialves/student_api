from django.contrib import admin
from django.urls import path, include

from student.urls import router


urlpatterns = [
    path('api/', include('student.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
