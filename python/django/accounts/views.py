from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView

from accounts.serializers import MemberSerializer, CreateUpdateUserSerializer

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
    serializer_class = CreateUpdateUserSerializer


class EditProfileView(UpdateAPIView):
    serializer_class = CreateUpdateUserSerializer
    
    def get_object(self):
        user = self.request.user
        return user
