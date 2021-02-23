from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from posts.models import Post

from topics.models import Topic
from rest_auth.serializers import UserDetailsSerializer


class SimplifiedTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['created_at', 'updated_at', 'name', 'title', 'author', 'description', 'urlname']


class TopicSerializer(SimplifiedTopicSerializer):
    author = UserDetailsSerializer(read_only=True)
    posts = SerializerMethodField()

    def get_posts(self, instance):
        from posts.serializers import SimplifiedPostSerializer
        posts = Post.objects.filter(topic=instance.urlname)[:4]
        return SimplifiedPostSerializer(posts, read_only=True, many=True).data

    class Meta:
        model = Topic
        fields = ['created_at', 'updated_at', 'name', 'title', 'author', 'description', 'urlname', 'posts']
