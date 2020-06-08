from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'books'

    def __str__(self):
        return self.name

    def __str__(self):
        return self.publisher.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    class Meta:
        default_related_name = 'stores'

    def __str__(self):
        return self.name

    def get_books(self):
        return ",".join([str(p) for p in self.books.all()])


class Details(models.Model):
    name = models.CharField(max_length=300)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    class Meta:
        default_related_name = 'details'

    def __str__(self):
        return self.name

    def __str__(self):
        return self.publisher.name

    def get_books(self):
        return ",".join([str(p) for p in self.books.all()])

