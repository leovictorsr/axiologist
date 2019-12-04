from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cartesian/', include('cartesian.urls')),
    path('admin/', admin.site.urls),
]