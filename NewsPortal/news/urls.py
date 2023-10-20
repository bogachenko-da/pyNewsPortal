from django.urls import path
from .views import (NewsList,
                    PostDetail,
                    NewsSearchList,
                    PostCreate,
                    PostUpdate,
                    PostDelete,
                    UserProfileUpdate,
                    upgrade_me,
                    CategoriesList,
                    CategoryPostsList,
                    subscribe,
                    unsubscribe)


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', NewsSearchList.as_view(), name='posts_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('profile/edit/', UserProfileUpdate.as_view(), name='user_profile_edit'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('categories/', CategoriesList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryPostsList.as_view(), name='category_posts_list'),
    path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('category/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe')
]
