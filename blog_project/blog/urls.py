from django.urls import path

from blog import views

urlpatterns = [
    path('', views.home_page, name='home'),  # /blog/

    path('posts/', views.get_posts, name="posts"),  # /blog/posts/
    path('posts/new/', views.create_post, name="create_post"),  # /blog/posts/new/
    path('posts/<int:post_id>/', views.post_by_id),

    path('login/', views.login_view),
    path('logout/', views.logout_view)
]
