from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView

from accounts.serializers import MemberSerializer, CreateUserSerializer

from accounts.models import Member


class UserInfoView(RetrieveAPIView):
    serializer_class = MemberSerializer

    def get_object(self):
        user = self.request.user
        return user


class UsersListView(ListAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
