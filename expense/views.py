from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from expense.forms import ExpenseCategoryCreateForm
from expense.models import *


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


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


class ExpenseUpdate(LoginRequiredMixin, CreateView):
    model = Expense


class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('expense-list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)