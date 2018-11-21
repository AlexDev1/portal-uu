
from django.urls import path
from .views import (LatestNewsFeed, NewsList, NewsView, news_pk,
                    TaggetNews, news_items_more)

urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('news/items/<int:offset>/', news_items_more, name='news-offset'),
    path('news/<int:year>/<int:month>/<int:day>/<int:pk>/', NewsView.as_view(), name='news_view'),
    path('news/<int:year>/<int:month>/', NewsList.as_view(), name='news_month'),
    path('news/<int:pk>/', news_pk, name='newsitem_comment_post'),
    path('news/rss/', LatestNewsFeed(), name='news_rss'),
    path('news/tag/<slug:tag>/', TaggetNews.as_view(), name='news_tag_detail'),
]
