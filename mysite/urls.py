from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
