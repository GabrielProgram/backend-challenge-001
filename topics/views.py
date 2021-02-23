from topics.models import Topic
from rest_framework import viewsets
from rest_framework import permissions
from topics.serializers import TopicSerializer
from helpers.is_model_author_logged_user import is_model_author_logged_user
from rest_framework.response import Response
from rest_framework import status


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows topic to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('-updated_at')
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user).order_by('-updated_at')

    def destroy(self, request, pk):
        if is_model_author_logged_user(self.get_object(), request):
            return super().destroy(request, pk)

        return Response({'message': f'User {request.user.pk} is not the author.'}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        if is_model_author_logged_user(self.get_object(), request):
            return super().update(request, pk)

        return Response({'message': f'User {request.user.pk} is not the author.'}, status=status.HTTP_401_UNAUTHORIZED)
