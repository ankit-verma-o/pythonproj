from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('squirrels/', include('squirrels.urls')),
    path('admin/', admin.site.urls),
]
