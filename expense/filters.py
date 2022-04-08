import django_filters
from django.forms import forms

from expense.models import Expense, Project, ExpenseCategory, Payee


class ExpenseFilter(django_filters.FilterSet):
    # TODO: Change field style
    # project = django_filters.ModelChoiceFilter(widget=TextInput(attrs={
    #     'placeholder': 'Search place', 'class': 'input__search'}))
    # payee = django_filters.ModelChoiceFilter(queryset=Payee.objects.all())
    # category = django_filters.ModelChoiceFilter(queryset=ExpenseCategory.objects.all())

    class Meta:
        model = Expense
        fields = [
            "project",
            "payee",
            "category",
        ]
