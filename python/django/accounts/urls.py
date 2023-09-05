from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts import views


urlpatterns = [
    # auth
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # accounts
    path("create_user/", views.CreateUserView.as_view(), name='create_user'),
    path("all/", views.UsersListView.as_view(), name='all_users'),
    path("user_info/", views.UserInfoView.as_view(), name='user_info'),
    path('user_info/edit/', views.EditProfileView.as_view(), name='edit_user_info'),

]
