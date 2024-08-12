from django.forms import Form, IntegerField, ChoiceField


class NewsSettingsForm(Form):
    page = IntegerField(initial=1)
    show = IntegerField(initial=15)
    sort = ChoiceField(choices=(
        ('date', 'date'),
        ('publisher', 'publisher'),
    ))
