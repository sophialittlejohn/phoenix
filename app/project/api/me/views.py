from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.api.me.serializers import UserSerializer, UserProfileUpdateSerializer
from project.api.permissions import IsUserOrReadOnly

User = get_user_model()


class GetUpdateUserProfileView(GenericAPIView):
    serializer_class = UserSerializer

    permission_classes = [
        IsAuthenticated,
        IsUserOrReadOnly
    ]

    def get(self, request, **kwargs):
        return Response(self.get_serializer(request.user).data)

    def post(self, request, **kwargs):
        serializer = UserProfileUpdateSerializer(data=request.data, context={
            'request': request
        })
        serializer.is_valid(raise_exception=True)
        user = serializer.save(serializer.validated_data)
        return Response(self.get_serializer(user).data)

    def delete(self, request, **kwargs):
        user = self.request.user
        user.is_active = False
        user.save()
        return Response('OK')
