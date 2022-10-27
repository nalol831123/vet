from django.db import models

# Create your models here.
class Register(models.Model):
    Number = models.AutoField(primary_key=True)
    Animal = models.CharField(max_length=150)
    Species = models.CharField(max_length=150)
    Sex = models.CharField(max_length=150)
    Neuter = models.CharField(max_length=150)
    Age = models.CharField(max_length=150,null=True)
    Name = models.CharField(max_length=150)
    Phone = models.CharField(max_length=150)
    Addr = models.CharField(max_length=150,null=True)
    ID = models.CharField(max_length=150,null=True)
    Doctor = models.CharField(max_length=150,null=True)
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Number)

class Patient(models.Model):
    Number = models.AutoField(primary_key=True)
    Memo = models.CharField(max_length=500,null=True)
    History = models.CharField(max_length=500,null=True)
    Phy = models.CharField(max_length=500,null=True)
    Blood = models.CharField(max_length=500,null=True)
    Image = models.CharField(max_length=500,null=True)
    Diag = models.CharField(max_length=500,null=True)
    Treat = models.CharField(max_length=500,null=True)
    Drug = models.CharField(max_length=500,null=True)
    UpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Number)

class Med(models.Model):
    MedChiName = models.CharField(max_length=150)
    MedEngName = models.CharField(max_length=150)
    Unit = models.CharField(max_length=150)
    Price = models.FloatField()

    def __str__(self):
        return str(self.MedChiName)
