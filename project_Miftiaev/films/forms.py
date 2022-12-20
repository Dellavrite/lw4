from django import forms
from django.forms import ModelChoiceField
from .models import Category

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.name)


class FilmForm(forms.Form): 
    name = forms.CharField(label="Название фильма")
    categorys = MyModelChoiceField(label="Жинр", queryset=Category.objects.all(), to_field_name="name")
    date_post = forms.DateField(label="Дата выпуска")
    actors = forms.CharField(label="Актёры", widget=forms.Textarea)
    date_view = forms.DateField(label="Дата показа")
