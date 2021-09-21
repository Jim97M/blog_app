from django.contrib import admin
from django.urls import path, include
from myblog import views
import myblog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myblog.urls"))
]
