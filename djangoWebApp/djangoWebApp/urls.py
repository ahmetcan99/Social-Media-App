from django.contrib import admin
from django.urls import path, include
from users import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", userViews.register, name="register"),
    path('', include("blog.urls")),
]
