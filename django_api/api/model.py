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
    laccountid = models.IntegerField()
    raccountid = models.IntegerField()
    createdtime = models.DateTimeField()

    class Meta:
        db_table = 'Relations'


class Groups(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    createdtime = models.DateTimeField()

    class Meta:
        db_table = 'Groups'


class Chats(models.Model):
    id = models.IntegerField()
    sendid = models.IntegerField()
    recid = models.IntegerField()
    msg = models.CharField()
    isread = models.BooleanField()
    isgroup = models.BooleanField()
    createdtime = models.DateTimeField()

    class Meta:
        db_table = 'Chats'
