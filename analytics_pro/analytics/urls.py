from django.urls import path
from .views import track_visit, profile_view, upload_photo, send_message, like_post, comment_on_post, dashboard

urlpatterns = [
    path('track_visit/', track_visit, name='track_visit'),
    path('profile_view/', profile_view, name='profile_view'),
    path('upload_photo/', upload_photo, name='upload_photo'),
    path('send_message/', send_message, name='send_message'),
    path('like_post/', like_post, name='like_post'),
    path('comment_on_post/', comment_on_post, name='comment_on_post'),
    path('dashboard/', dashboard, name='dashboard'),
]





#analytics/comment_on_post/
#C:\Users\Faisal\OneDrive\Desktop\task\analytics_pro>