from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from reviews.forms import ReviewCreationForm

# Create your views here.
def reviews(request):
    reviews = Review.objects.all()

    context = {
        "reviews": reviews
    }

    return render(request, "reviews/reviews.html", context=context)

def index(request):
    return render(request, "reviews/index.html")

@login_required(login_url="/login")
def create_review(request):
    if request.method == "POST":
        form = ReviewCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("reviews")

    else:
        form = ReviewCreationForm()

    return render(request, "reviews/create_review.html", context={"form": form})