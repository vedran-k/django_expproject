import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Expense


class ExpenseModelTests(TestCase):

    def test_was_added_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose createdOn
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_expense = Expense(createdOn=time)
        self.assertIs(future_expense.was_added_recently(), False)