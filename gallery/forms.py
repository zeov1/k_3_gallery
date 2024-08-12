from django.forms import Form, IntegerField


class NewsSettingsForm(Form):
    page = IntegerField()
    show = IntegerField()
