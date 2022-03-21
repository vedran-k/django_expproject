import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    catName = models.CharField(max_length=50)

    def __str__(self):
        return self.catName


class SubCategory(models.Model):
    subCatName = models.CharField(max_length=50)

    def __str__(self):
        return self.subCatName


class Expense(models.Model):
    cost = models.IntegerField(default = 0)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdOn = models.DateTimeField()

    def __str__(self):
        return f'{self.cost} {self.cat} {self.subcat}'

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.createdOn <= now

    def get_absolute_url(self):
        return reverse('costless:my-expenses')