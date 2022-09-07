from django.db import models


class Event(models.Model):
    url= models.URLField(max_length = 200)
    no_of_seats= models.IntegerField()
    # do_you_want_any_specific_seat=models.BooleanField()
    account=models.CharField(max_length=30)
    filter=models.CharField(max_length=30)
    hours=models.IntegerField()
    minute=models.IntegerField()

class Account(models.Model):
    email = models.EmailField()
    password=models.CharField(max_length=50)
    card_no=models.IntegerField()
    expiry_date=models.DateField()
    cvv_no=models.IntegerField()
    fname=models.CharField(max_length=23)
    lname=models.CharField(max_length=43)
    Address1=models.TextField()
    Address2 = models.TextField()
    city = models.CharField(max_length=29)