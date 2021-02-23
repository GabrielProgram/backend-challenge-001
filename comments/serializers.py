from rest_framework import serializers

from comments.models import Comment
from rest_auth.serializers import UserDetailsSerializer

from posts.serializers import SimplifiedPostSerializer


class SimplifiedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']


class CommentSerializer(SimplifiedCommentSerializer):
    author = UserDetailsSerializer(read_only=True)
    post = SimplifiedPostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'post', 'author']
