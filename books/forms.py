from django.forms import ModelForm, CharField, TextInput
from .models import Book


class BookCreateForm(ModelForm):
    title = CharField(
        required=False,
        widget=TextInput(attrs={'class': 'clrtxt', 'placeholder': 'Название'})
    )
    author = CharField(
        required=False,
        widget=TextInput(attrs={'class': 'clrtxt', 'placeholder': 'Автор'})
    )
    price = CharField(
        required=False,
        widget=TextInput(attrs={'class': 'clrtxt', 'placeholder': 'Цена'})
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']


class BookEditForm(BookCreateForm):
    title = CharField(required=False, widget=TextInput())
    author = CharField(required=False, widget=TextInput())
    price = CharField(required=False, widget=TextInput())
