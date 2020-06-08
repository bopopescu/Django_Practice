from django.db import models


# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return "%s (%s)" % (
    #         self.name,
    #         ", ".join(topping.name for topping in self.toppings.all()),
    #     )
    def get_toppings(self):
        return ",".join([str(p) for p in self.toppings.all()])

    def toppings_name(self):
        return self.toppings.name
