from django.db import models

# Create your models here.

class STUDENT(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    qualification=models.CharField(max_length=50)
    mail_id=models.CharField(max_length=50)
    duration=models.IntegerField(null=True)
    joining_date=models.DateField(null=True)
    paid_amount=models.IntegerField(null=True)
    balance_amount=models.IntegerField(null=True)


class PHONE(models.Model):
    ph_number=models.BigIntegerField(max_length=30)
    ph=models.ForeignKey(STUDENT,on_delete=models.CASCADE,null=True)

class COURSE(models.Model):
    course=models.CharField(max_length=50)
    number=models.ManyToManyField(STUDENT)
