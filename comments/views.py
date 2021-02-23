from comments.models import Comment
from rest_framework import viewsets
from rest_framework import permissions
from comments.serializers import CommentSerializer
from helpers.is_model_author_logged_user import is_model_author_logged_user
from rest_framework.response import Response
from rest_framework import status

from posts.models import Post


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comment to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, post_pk=None, topic_pk=None):
        self.queryset = Comment.objects.filter(post=post_pk, post__topic=topic_pk).order_by('-created_at')
        return super().list(self, request)

    def retrieve(self, request, pk=None, post_pk=None, topic_pk=None):
        self.queryset = Comment.objects.filter(id=pk, post=post_pk, post__topic=topic_pk)
        return super().retrieve(self, request)

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.request.resolver_match.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)

    def destroy(self, request, pk=None, post_pk=None, topic_pk=None):
        self.queryset = Comment.objects.filter(id=pk, post=post_pk, post__topic=topic_pk)
        if is_model_author_logged_user(self.get_object(), request):
            return super().destroy(request, pk)

        return Response({'message': f'User {request.user.pk} is not the author.'}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None, post_pk=None, topic_pk=None):
        self.queryset = Comment.objects.filter(id=pk, post=post_pk, post__topic=topic_pk)
        if is_model_author_logged_user(self.get_object(), request):
            return super().update(request, pk)

        return Response({'message': f'User {request.user.pk} is not the author.'}, status=status.HTTP_401_UNAUTHORIZED)
