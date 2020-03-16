from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from expense.forms import ExpenseCategoryCreateForm
from expense.models import Project, ExpenseCategory


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard.html'


# @method_decorator(login_required, name='dispatch')
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'expense/project_list.html'
    paginate_by = 10


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'status', 'income', 'start_date', 'end_date']
    template_name = 'expense/project_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'description', 'status', 'income', 'start_date', 'end_date']


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')


class CategoryList(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    context_object_name = 'categories'
    template_name = 'expense/expensecategory_list.html'


class CategoryCreate(CreateView):
    success_url = reverse_lazy('category-list')
    model = ExpenseCategory
    fields = ['title']
    template_name = 'expense/expensecategory_list.html'

    def get_context_data(self, **kwargs):
        kwargs['categories'] = ExpenseCategory.objects.order_by('id')
        return super(CategoryCreate, self).get_context_data(**kwargs)


class CategoryDelete(DeleteView):
    model = ExpenseCategory
    success_url = reverse_lazy('category-list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)