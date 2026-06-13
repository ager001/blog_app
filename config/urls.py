from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from books.views import SuperUserListView
from rest_framework.authtoken.views import obtain_auth_token
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # user auth pages (HTML views)
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # API routes
    path('api/token/', obtain_auth_token),
    path('api/', include('books.urls')),
    path('api/superusers/', SuperUserListView.as_view()),

    # blog app (frontend routes)
    path('', include('blog.urls')),
]