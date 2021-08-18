from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListShortenerAPIView.as_view(),name="shortener_list"),
    path("create/", views.CreateShortenerAPIView.as_view(),name="shortener_create"),
    path("update/<int:pk>/",views.UpdateShortenerAPIView.as_view(),name="update_shortener"),
    path("delete/<int:pk>/",views.DeleteShortenerAPIView.as_view(),name="delete_shortener")
]