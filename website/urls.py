from django.urls import path
from . import views

urlpatterns = [
    # path("signup", views.signup, name="signup"),
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("show_record/<int:pk>", views.show_record, name="record"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path("add_record/<int:pk>", views.add_record, name="add_record"),
    path("update_record/<int:pk>", views.update_record, name="update_record"),
]
