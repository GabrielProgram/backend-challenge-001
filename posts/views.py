from posts.models import Post
from rest_framework import viewsets
from rest_framework import permissions
from posts.serializers import PostSerializer
from helpers.is_model_author_logged_user import is_model_author_logged_user
from rest_framework.response import Response
from rest_framework import status

from topics.models import Topic


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, topic_pk=None):
        self.queryset = Post.objects.filter(topic=topic_pk).order_by('-updated_at')
        return super().list(self, request)

    def retrieve(self, request, pk=None, topic_pk=None):
        self.queryset = Post.objects.filter(id=pk, topic=topic_pk)
        return super().retrieve(self, request)

    def perform_create(self, serializer):
        topic = Topic.objects.get(pk=self.request.resolver_match.kwargs['topic_pk'])
        serializer.save(author=self.request.user, topic=topic)

    def destroy(self, request, pk=None, topic_pk=None):
        self.queryset = Post.objects.filter(id=pk, topic=topic_pk)
        if is_model_author_logged_user(self.get_object(), request):
            return super().destroy(request, pk)

        return Response({'message': f'User {request.user.pk} is not the author.'}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None, topic_pk=None):
        self.queryset = Post.objects.filter(id=pk, topic=topic_pk)
        if is_model_author_logged_user(self.get_object(), request):
            return super().update(request, pk)

        return Response({'message': f'User {request.user.pk} is not the author.'}, status=status.HTTP_401_UNAUTHORIZED)
