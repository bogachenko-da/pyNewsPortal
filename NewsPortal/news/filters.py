from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from .models import Post, Category, Author
from django import forms


class PostFilter(FilterSet):
    title = CharFilter(
        lookup_expr='icontains',
        label='Название',
    )
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Все авторы',
    )
    date = DateFilter(
        field_name='post_created',
        lookup_expr='date__gte',
        label='Позже указанной даты',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    category = ModelChoiceFilter(
        field_name='postcategory__category__name',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Все категории',
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'date', 'category']
