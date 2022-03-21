from django.urls import path

from . import views

app_name = 'costless'
urlpatterns = [
    path('myexpenses/', views.ExpensesByUserListView.as_view(), name='my-expenses'),
    path('newexpense/', views.NewExpenseView.as_view(), name='new-expense'),
    path('mycategories/', views.ExpensesByCategoryListView.as_view(), name='my-categories'),
    path('bydate/', views.ExpensesByDateListView.as_view(), name='by-dates'),
    path('category/<str:catName>/', views.CategoryListView.as_view(), name='category'),
    path('subcategory/<str:subCatName>/', views.SubCategoryListView.as_view(), name='subcategory'),
]