from datetime import timedelta, datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from expense.models import *


class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboard.html'

    def get(self, request):
        number_of_projects = Project.objects.count()
        total_expense_last_seven_days = Expense.objects.values('amount').filter(
            created_at__gte=timezone.now() - timedelta(days=7)).aggregate(total=Sum('amount'))

        context = {
            "total_number_of_projects": number_of_projects,
            "total_expense_last_seven_days": total_expense_last_seven_days['total'],
        }
        return render(request, self.template_name, context)


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'expense/project_list.html'
    paginate_by = 10


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'status', 'income', 'start_date', 'end_date']
    template_name = 'expense/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'description', 'status', 'income', 'start_date', 'end_date']
    template_name = 'expense/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CategoryList(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    context_object_name = 'categories'
    template_name = 'expense/expensecategory_list.html'


class CategoryCreate(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('category-list')
    model = ExpenseCategory
    fields = ['title']
    template_name = 'expense/expensecategory_list.html'

    def get_context_data(self, **kwargs):
        kwargs['categories'] = ExpenseCategory.objects.order_by('id')
        return super(CategoryCreate, self).get_context_data(**kwargs)


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = ExpenseCategory
    success_url = reverse_lazy('category-list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'expense/expense_list.html'
    paginate_by = 10


class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    success_url = reverse_lazy('expense-list')
    fields = ['amount', 'payee', 'category', 'project', ]
    template_name = 'expense/expense_form.html'


class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ['amount', 'payee', 'category', 'project', ]


class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('expense-list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CostLimitList(LoginRequiredMixin, ListView):
    model = CostLimit
    context_object_name = 'cost_limits'
    template_name = 'expense/costlimit_list.html'


class CostLimitCreate(LoginRequiredMixin, CreateView):
    model = CostLimit
    fields = ['limit', 'category', 'project']
    template_name = 'expense/costlimit_form.html'
    success_url = reverse_lazy('costlimit-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CostLimitUpdate(LoginRequiredMixin, UpdateView):
    model = CostLimit
    fields = '__all__'
    template_name = 'expense/costlimit_form.html'
    success_url = reverse_lazy('costlimit-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CostLimitDelete(LoginRequiredMixin, DeleteView):
    model = CostLimit
    success_url = reverse_lazy('costlimit-list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class PayeeList(LoginRequiredMixin, ListView):
    model = Payee
    context_object_name = 'payees'
    template_name = 'expense/payee_list.html'


class PayeeCreate(LoginRequiredMixin, CreateView):
    model = Payee
    fields = '__all__'
    template_name = 'expense/payee_form.html'
    success_url = reverse_lazy('payee-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PayeeUpdate(LoginRequiredMixin, UpdateView):
    model = Payee
    fields = '__all__'
    template_name = 'expense/payee_form.html'
    success_url = reverse_lazy('payee-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PayeeDelete(LoginRequiredMixin, DeleteView):
    model = CostLimit
    success_url = reverse_lazy('payee-list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)