from django.contrib import admin

from expense.models import Project, ExpenseCategory


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "created_at",
        "end_date",
        "status",
    )
    list_filter = ("title", "created_at", "end_date", "status")
    search_fields = (
        "title",
        "description",
    )


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
