from django import forms

from .models import ExpenseCategory


class ExpenseCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ('title',)

        # def __init__(self, *args, **kwargs):
        #     self.user = kwargs.pop('user')
        #     super(ExpenseCategoryCreateForm, self).__init__(*args, **kwargs)
