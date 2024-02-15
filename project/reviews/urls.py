from django.urls import path
from .views import (
    ReviewCreateView,
    ReviewDetailView,
    CommentCreateView,
    CommentDetailView)
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reviews/", views.reviews, name="reviews"),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path("reviews/new/", ReviewCreateView.as_view(), name='review-create'),
    path("reviews/all_reviews/", views.recent_reviews, name="recent-reviews"),
    path('reviews/comments/create_comment/', CommentCreateView.as_view(),
         name='comment-create'),
    path('reviews/comments/<int:pk>/', CommentDetailView.as_view(),
         name='comment-detail')
]
