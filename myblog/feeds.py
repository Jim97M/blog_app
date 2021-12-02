from django.contrib.syndication.views import Feed
from django.template.defaultfilters import title, truncatewords
from django.urls import reverse_lazy
from .models import Post

class LatestPostFeed(Feed):
    title = 'Super Blog'
    link = reverse_lazy('myblog:listview')
    description = 'New Post'

    def items(self):
        return Post.new_manager.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body