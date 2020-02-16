from django.contrib.auth import get_user_model
from django.db import models
from datetime import date

STATUS_CHOICES = [
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
]


class ExpenseCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Expense Categories'


class Project(models.Model):
    title = models.CharField(max_length=300)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    income = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payee = models.CharField(max_length=100)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
