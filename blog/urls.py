django.contrib import admin
from django.urls import path
from django.urls import path
from myblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage)
]
