import django_filters

from expense.models import Expense, Project, ExpenseCategory, Payee


class ExpenseFilter(django_filters.FilterSet):
    # project = django_filters.ModelChoiceFilter(queryset=Project.objects.all())
    # payee = django_filters.ModelChoiceFilter(queryset=Payee.objects.all())
    # category = django_filters.ModelChoiceFilter(queryset=ExpenseCategory.objects.all())

    class Meta:
        model = Expense
        fields = ['project', 'payee', 'category', ]
