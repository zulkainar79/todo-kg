
from django.contrib import admin
from django.urls import path
from main.views import homepage, test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path("test/", test, name="test"),
    path("check/". check)
]
