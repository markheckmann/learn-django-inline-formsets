from django.forms import ModelForm, inlineformset_factory
from .models import Bedarf, BedarfVZP


class BedarfForm(ModelForm):
    class Meta:
        fields = ("name",)
        model = Bedarf


class BedarfVZPForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = BedarfVZP


BedarfVZPFormset = inlineformset_factory(
    Bedarf, BedarfVZP, fields=("jahr", "vzp"), extra=0, can_delete=False
)
