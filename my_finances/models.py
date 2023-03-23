from django.db import models


# Create your models here.
class Income(models.Model):
    class IncomeTypes(models.IntegerChoices):
        SALARY = 1, "SALARY"
        BONUS = 2, "BONUS"
        GIFT = 3, "GIFT"
        DIVIDEND = 4, "DIVIDEND"
        OTHER = 5, "OTHER"

    class RepetitionInterval(models.IntegerChoices):
        NA = 1, 'N/A'
        DAY = 2, 'DAY'
        WEEK = 3, 'WEEK'
        MONTH = 4, 'MONTH'
        QUARTER = 5, 'QUARTER'
        SEMESTER = 6, 'SEMESTER'
        YEAR = 7, 'YEAR'

    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    income_type = models.PositiveSmallIntegerField(choices=IncomeTypes.choices)
    recurrent = models.BooleanField(default=False)
    recurrency_interval = models.PositiveSmallIntegerField(choices=RepetitionInterval.choices, default=1)
    recurrency_time = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Income {self.id} - {self.income_type} - {self.date.strftime("%d/%m/%Y")}'
    
    class Meta:
        verbose_name_plural = 'incomes'


class Outcome(models.Model):
    class OutcomeTypes(models.IntegerChoices):
        RENT = 1, 'RENT'
        BILLS = 2, 'BILLS'
        CAR = 3, 'CAR'
        TRAVEL = 4, 'TRAVEL'
        HEALTH = 5, 'HEALTH'
        GROCERIES = 6, 'GROCERIES'
        FUN = 7, 'FUN'
        CLOTHES = 8, 'CLOTHES'
        CHARITY = 9, 'CHARITY'
        INVESTMENT = 10, 'INVESTMENT'
        EDUCATION = 11, 'EDUCATION'

    class RepetitionInterval(models.IntegerChoices):
        NA = 1, 'N/A'
        DAY = 2, 'DAY'
        WEEK = 3, 'WEEK'
        MONTH = 4, 'MONTH'
        QUARTER = 5, 'QUARTER'
        SEMESTER = 6, 'SEMESTER'
        YEAR = 7, 'YEAR'

    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    outcome_type = models.PositiveSmallIntegerField(choices=OutcomeTypes.choices)
    recurrent = models.BooleanField(default=False)
    recurrency_interval = models.PositiveSmallIntegerField(choices=RepetitionInterval.choices, default=1)
    recurrency_time = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Outcome {self.id} - {self.outcome_type} - {self.date.strftime("%d/%m/%Y")}'
    
    class Meta:
        verbose_name_plural = 'outcomes'


class Balance(models.Model):
    class BalanceTypes(models.IntegerChoices):
        CURRENT = 1, 'CURRENT'
        SAVINGS = 2, 'SAVINGS'

    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    balance_type = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Balance {self.id} - {self.balance_type}'
    
    class Meta:
        verbose_name_plural = 'balances'
