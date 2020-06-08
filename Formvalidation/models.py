from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(blank=True)

    def __str__(self):
        return self.user.username


class IndustryType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Divisions(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=200, default=None, blank=True)
    divisions = models.ForeignKey(Divisions, on_delete=models.CASCADE)
    industrytype = models.ManyToManyField(IndustryType)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

    def get_industrytype(self):
        return ",".join([str(p) for p in self.industrytype.all()])
