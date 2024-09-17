from django.forms import ModelForm
from main.models import Candy

class CandyEntryForm(ModelForm):
    class Meta:
        model = Candy
        fields = ["name", "price", "sweetness", "description"]