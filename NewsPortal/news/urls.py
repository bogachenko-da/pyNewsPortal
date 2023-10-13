from django.urls import path
from .views import (NewsList,
                    PostDetail,
                    NewsSearchList,
                    PostCreate,
                    PostUpdate,
                    PostDelete,
                    UserProfileUpdate,
                    upgrade_me)


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', NewsSearchList.as_view(), name='posts_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('profile/edit/', UserProfileUpdate.as_view(), name='user_profile_edit'),
    path('upgrade/', upgrade_me, name='upgrade')
]
