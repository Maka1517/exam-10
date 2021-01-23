from django.urls import path

from webapp.views.views import IndexView, FriendChoseView, FriendDelView

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('friend/<int:pk>/like/', FriendChoseView.as_view(), name='friend_chose'),
    path('friend/<int:pk>/unlike/', FriendDelView.as_view(), name='friend_del'),

]