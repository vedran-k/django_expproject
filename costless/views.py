from django.shortcuts import render
from .models import Expense
from django.views import generic
from django.db.models import F
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import *

class ExpensesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Expense
    template_name = 'costless/expenses_by_user.html'
    paginate_by = 10
    context_object_name = 'context'

    def get_context_data(self):
        latest_expenses_list = Expense.objects.filter(user=self.request.user).order_by('createdOn')
        s = 0
        for q in latest_expenses_list:
            s += q.cost
        context = {'latest_expenses_list': latest_expenses_list, 's': s}
        return context

class ExpensesByCategoryListView(LoginRequiredMixin, generic.ListView):
    model = Expense
    template_name = 'costless/expenses_by_cat.html'
    paginate_by = 10
    context_object_name = 'context'

    def get_context_data(self):
        latest_expenses_list = Expense.objects.filter(user=self.request.user)
        categories = set(q.cat.catName for q in latest_expenses_list)
        cat_list = []
        all = 0
        for c in categories:
            s = 0
            cat_exp = latest_expenses_list.filter(cat__catName = c)
            for q in cat_exp:
                s += q.cost
            cat_list.append((c, cat_exp, s))
            all += s
        context = {'cat_list': cat_list, 'all': all }
        return context

class ExpensesByDateListView(LoginRequiredMixin, generic.ListView):
    model = Expense
    template_name = 'costless/expenses_by_date.html'
    paginate_by = 10
    context_object_name = 'context'

    def get_context_data(self):
        latest_expenses_list = Expense.objects.filter(user=self.request.user)
        dates = set(q.createdOn.month for q in latest_expenses_list)
        date_list = []
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        all = 0
        for d in dates:
            s = 0
            date_exp = latest_expenses_list.filter(createdOn__month=d)
            for q in date_exp:
                s += q.cost
            date_list.append((months[d-1], date_exp, s))
            all += s
        context = {'date_list': date_list, 'all': all }
        return context

class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Expense
    template_name = 'costless/category.html'
    paginate_by = 10
    context_object_name = 'context'

    def get_context_data(self):
        level = self.kwargs.get('catName')
        latest_expenses_list = Expense.objects.filter(user=self.request.user).filter(cat__catName = level)
        s = 0
        for q in latest_expenses_list:
            s += q.cost
        context = {'cat_list': latest_expenses_list, 'all': s, 'level':level}
        return context

class SubCategoryListView(LoginRequiredMixin, generic.ListView):
    model = Expense
    template_name = 'costless/subcategory.html'
    paginate_by = 10
    context_object_name = 'context'

    def get_context_data(self):
        level = self.kwargs.get('subCatName')
        latest_expenses_list = Expense.objects.filter(user=self.request.user).filter(subcat__subCatName = level)
        s = 0
        for q in latest_expenses_list:
            s += q.cost
        context = {'cat_list': latest_expenses_list, 'all': s, 'level':level}
        return context

class NewExpenseView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = 'costless/newexpense.html'
    fields = ['cost', 'cat', 'subcat', 'createdOn']
    initial = {'createdOn': datetime.now()}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class IndexView(generic.ListView):
#     template_name = 'costless/expenses_by_user.html'
#     context_object_name = 'latest_expenses_list'
#     def get_queryset(self):
#         return Expense.objects.order_by('-createdOn')[:5]

        # latest_expenses_list = Expense.objects.order_by('-createdOn')[:5]
        # output = ', '.join([str(q.cat) for q in latest_expenses_list])
        # s = 0
        # for q in latest_expenses_list:
        #     s += q.cost
        # context = {'latest_expenses_list':latest_expenses_list, 's':s}
        # return render(request, 'costless/expenses_by_user.html',context)

# def stats_Cat(request, catName):
#     latest_expenses_list = Expense.objects.order_by('-createdOn')[:5]
#     latest_cat_list_by_id = [q for q in latest_expenses_list if q.cat.catName == catName]
#     s = 0
#     for q in latest_cat_list_by_id:
#         s += q.cost
#     context = {'latest_cat_list_by_id': latest_cat_list_by_id, 's':s}
#     return render(request, 'costless/expenses_by_cat.html', context)

# def stats_subCat(request, catName, subCatName):
#     latest_expenses_list = Expense.objects.order_by('-createdOn')[:5]
#     latest_subcat_list_by_id = [q for q in latest_expenses_list if q.subcat.subCatName == subCatName]
#     s = 0
#     for q in latest_subcat_list_by_id:
#         s += q.cost
#     context = {'latest_subcat_list_by_id': latest_subcat_list_by_id, 's': s}
#     return render(request, 'costless/category.html', context)