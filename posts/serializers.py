from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from comments.models import Comment
from posts.models import Post
from rest_auth.serializers import UserDetailsSerializer

from topics.serializers import SimplifiedTopicSerializer


class SimplifiedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']


class PostSerializer(SimplifiedPostSerializer):
    author = UserDetailsSerializer(read_only=True)
    topic = SimplifiedTopicSerializer(read_only=True)
    comments = SerializerMethodField()

    def get_comments(self, instance):
        from comments.serializers import SimplifiedCommentSerializer
        comments = Comment.objects.filter(post=instance.id)[:4]
        return SimplifiedCommentSerializer(comments, read_only=True, many=True).data

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'topic', 'author', 'comments']
