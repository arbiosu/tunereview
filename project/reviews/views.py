from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Album, Review, Comment


def index(request):
    return render(request, 'reviews/home.html')


def reviews(request):
    """
    Get the users reviews.
    """
    my_reviews = Review.objects.filter(author=request.user)

    context = {
        'reviews': my_reviews
    }
    return render(request, 'reviews/reviews.html', context)


def recent_reviews(request):
    reviews = Review.objects.all().order_by('-date_posted')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/all_reviews.html', context)


class ReviewDetailView(DetailView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(review_id=self.object)
        return context


class ReviewCreateView(CreateView):
    model = Review
    fields = ['review_text', 'rating']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.album_id = Album.objects.get(pk=self.kwargs['album_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.get(pk=self.kwargs['album_id'])
        return context


class CommentDetailView(DetailView):
    model = Comment


class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment_text']

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        form.instance.review_id = Review.objects.get(
            pk=self.kwargs['review_id']
            )
        return super().form_valid(form)
