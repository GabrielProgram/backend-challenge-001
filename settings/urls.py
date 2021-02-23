"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested import routers

from helpers.health_check_view import health_check

from topics.views import TopicViewSet
from posts.views import PostViewSet
from comments.views import CommentViewSet

router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet)

posts_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
posts_router.register(r'posts', PostViewSet, basename='topic-posts')

comments_router = routers.NestedSimpleRouter(posts_router, r'posts', lookup='post')
comments_router.register(r'comments', CommentViewSet, basename='post-comments')

###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include(router.urls)),
    url(r'^', include(posts_router.urls)),
    url(r'^', include(comments_router.urls)),

]
