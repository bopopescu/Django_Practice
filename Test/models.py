from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Thana(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IndustryTypeMaster(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IndustryTypeSlave(models.Model):
    name = models.CharField(max_length=200)
    industrytypemaster = models.ForeignKey(IndustryTypeMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=200, default=None, blank=True)
    country = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    industrytypeslave = models.ManyToManyField(IndustryTypeSlave)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

    def get_industrytypeslave(self):
        return ",".join([str(p) for p in self.industrytypeslave.all()])
