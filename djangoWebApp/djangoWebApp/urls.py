from django.contrib import admin
from django.contrib.auth import views as authViews
from django.urls import path, include
from users import views as userViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", userViews.register, name="register"),
    path("login/", authViews.LoginView.as_view(template_name = "users/login.html"), name="login"),
    path("logout/", userViews.logoutView, name="logout"),
    path("profile/", userViews.profile, name="profile"),
    path('', include("blog.urls")),
]
