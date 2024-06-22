from django.forms import ModelForm
from reviews.models import Review

class ReviewCreationForm(ModelForm):
    class Meta():
        model = Review
        fields = ["author", "title", "content"]
        