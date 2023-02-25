from django.db import models


class Make (models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Car(models.Model):
    year = models.CharField(max_length=124)
    make = models.ForeignKey(Make, on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.year + " " + str(self.make) + " " + str(self.model)