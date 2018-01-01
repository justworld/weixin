from django.db import models


class Account(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    password = models.CharField()
    createdtime = models.DateTimeField()

    class Meta:
        db_table = 'Account'
