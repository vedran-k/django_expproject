from django.contrib import admin
from .models import *

class ExpenseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['cost', 'cat', 'subcat','user']}),
        ('Date information', {'fields': ['createdOn']}),
    ]

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Expense, ExpenseAdmin)