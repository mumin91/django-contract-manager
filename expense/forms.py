from django import forms

from .models import ExpenseCategory, Expense


class ExpenseCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ("title",)

        # def __init__(self, *args, **kwargs):
        #     self.user = kwargs.pop('user')
        #     super(ExpenseCategoryCreateForm, self).__init__(*args, **kwargs)


class ExpenseFilterForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["project", "category", "payee"]
