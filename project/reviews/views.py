from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Album, Review, Comment


def index(request):
    return render(request, 'reviews/home.html')


def reviews(request):
    context = {
        'reviews': Review.objects.filter(author=request.user),
        'comments': Comment.objects.all()
    }
    return render(request, 'reviews/reviews.html', context)


def recent_reviews(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews/all_reviews.html', context)


class ReviewDetailView(DetailView):
    model = Review


class ReviewCreateView(CreateView):
    model = Review
    fields = ['review_text', 'rating']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.albumId = Album.objects.get(pk=1)
        return super().form_valid(form)


class CommentDetailView(DetailView):
    model = Comment


class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment_text']

    def form_valid(self, form):
        form.instance.commentAuthor = self.request.user
        form.instance.reviewId = Review.objects.get(pk=10)
        return super().form_valid(form)
