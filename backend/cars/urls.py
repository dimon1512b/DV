from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('ajax_get_cars/', views.ajax_get_cars),
]