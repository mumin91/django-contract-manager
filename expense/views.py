from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

from expense.models import Project


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'expense/project_list.html'
    paginate_by = 2