from django.db import models


class Account(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    password = models.CharField()
    createdtime = models.DateTimeField()

    class Meta:
        db_table = 'Account'


class Relations(models.Model):
    id = models.IntegerField()
    lAccountId = models.IntegerField()
    rAccountId = models.IntegerField()

    class Meta:
        db_table = 'Relations'
