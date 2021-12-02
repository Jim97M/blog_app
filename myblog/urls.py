from django.urls import path
from . import views
from .feeds import LatestPostFeed
app_name = 'myblog'
urlpatterns = [
      path("list/", views.post_list, name='listview'),
      path("detail/<int:pk>", views.post_detail, name='detailview'),
      path('<int:pk>/comment', views.comment_view, name='commentview'),
      path('search', views.search, name='search'),
      path('feed/', LatestPostFeed(), name='latest_post_feed')
]