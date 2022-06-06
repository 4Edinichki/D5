from django.urls import path

from .views import PostList, PostDetail, create_post, NewsCreate, PostUpdate, PostDelete, ArticleCreate, ArticleList

urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('article/', ArticleList.as_view(), name='article_list'),

    path('<int:pk>', PostDetail.as_view(), name='post_detail'),

    path('create_news', NewsCreate.as_view(), name='news_create'),
    path('create_article', ArticleCreate.as_view(), name='article_create'),

    path('news/<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='article_delete'),

    path('news/<int:pk>/update', PostUpdate.as_view(), name='news_update'),
    path('article/<int:pk>/update', PostUpdate.as_view(), name='article_update'),
]
