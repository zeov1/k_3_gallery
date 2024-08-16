from django.forms import Form, IntegerField, ChoiceField, ModelForm

from gallery.models import Image


class NewsSettingsForm(Form):
    page = IntegerField(initial=1)
    show = IntegerField(initial=15)
    sort = ChoiceField(choices=(
        ('date', 'date'),
        ('publisher', 'publisher'),
    ))


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['img', 'caption']
