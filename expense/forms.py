from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
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

    def __init__(self):
        super().__init__()
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'

        self.helper.layout = Layout(
            Div(
                Div('first_name', css_class="col-sm-2"),
                Div('last_name', css_class="col-sm-2"),
                Div('middle_initial', css_class="col-sm-2"),
                Div('social_security_number', css_class="col-sm-2"),
                css_class='row',
            )
        )

    class Meta:
        model = Expense
        fields = ["project", "category", "payee"]
