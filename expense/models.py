from django.contrib.auth import get_user_model
from django.db import models
from datetime import date

from django.urls import reverse

STATUS_CHOICES = [
    ("ongoing", "Ongoing"),
    ("completed", "Completed"),
]


class ExpenseCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Expense Categories"


class Project(models.Model):
    title = models.CharField(max_length=300)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="open")
    income = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ["-start_date"]

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Project."""
        return reverse("project-detail-view", args=[str(self.id)])

    def __str__(self):
        """String for representing the Project object (in Admin site etc.)."""
        return self.title


class Payee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Expense."""
        return reverse("payee-list", args=[str(self.id)])

    def __str__(self):
        """String for representing the Expense object (in Admin site etc.)."""
        return str(self.name)


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payee = models.ForeignKey(Payee, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ["-created_at"]

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Expense."""
        return reverse("expense-detail-view", args=[str(self.id)])

    def __str__(self):
        """String for representing the Expense object (in Admin site etc.)."""
        return str(self.amount)


class CostLimit(models.Model):
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    reached_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # Metadata
    # class Meta:
    #     ordering = ['-created_at']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Expense."""
        return reverse("costlimit-detail-view", args=[str(self.id)])

    def __str__(self):
        """String for representing the Expense object (in Admin site etc.)."""
        return str(self.limit)
