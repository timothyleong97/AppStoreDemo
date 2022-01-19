# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=64)
    dob = models.DateField()
    since = models.DateField()
    customerid = models.CharField(primary_key=True, max_length=16)
    country = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'customers'


class Downloads(models.Model):
    customerid = models.OneToOneField(Customers, models.DO_NOTHING, db_column='customerid', primary_key=True)
    name = models.ForeignKey('Games', models.DO_NOTHING, db_column='name')
    version = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'downloads'
        unique_together = (('customerid', 'name', 'version'),)


class Games(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    version = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'games'
        unique_together = (('name', 'version'),)
