from django.urls import path
from reviews import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reviews/", views.reviews, name="reviews"),
    path("create_review/", views.create_review, name="create_review")
]