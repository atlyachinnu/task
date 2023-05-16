from django.db import models
from django.db.models import options


# Create your model
DISTRICT_CHOICES=(
    ('kannur','KANNUR'),
    ('eranakulam','ERANAKULAM'),
    ('malappuram','MALAPPURAM'),
    ('palakkad','PALAKKAD'),
    ('kollam','KOLLAM')
)
ACCOUNT_CHOICES=(
    ('current account','CURRENT ACCOUNT'),
    ('savings account','SAVINGS ACCOUNT')
)
class bankkk(models.Model):
    name=models.CharField(max_length=200)
    dob=models.DateField(max_length=8)
    age=models.IntegerField()
    Gender=models.CharField(max_length=100)
    phn=models.IntegerField()
    mail=models.EmailField(max_length=254)
    address=models.CharField(max_length=50)
    des=models.CharField(max_length=18,choices=DISTRICT_CHOICES)
    branch=models.CharField(max_length=18,choices=DISTRICT_CHOICES)
    accounttype=models.CharField(max_length=20,choices=ACCOUNT_CHOICES)
    materialprovide=models.BooleanField('debit card',default=False)
    materialprovide1 = models.BooleanField('credit card', default=False)
    materialprovide2 = models.BooleanField('cheque book', default=False)



