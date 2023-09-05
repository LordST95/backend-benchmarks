from rest_framework.generics import RetrieveAPIView, CreateAPIView

from accounts.serializers import MemberSerializer, CreateUserSerializer


class UserInfoView(RetrieveAPIView):
    serializer_class = MemberSerializer

    def get_object(self):
        user = self.request.user
        return user


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
