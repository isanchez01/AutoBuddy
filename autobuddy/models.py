from django.db import models

# Create your models here.
class RepairCost(models.Model):
    car_year = models.CharField(max_length=4)
    car_make = models.CharField(max_length=30)
    car_model = models.CharField(max_length=60)
    
    repair_name = models.CharField(max_length = 70)
    repair_cost = models.IntegerField(blank= True)

    def __str__(self) -> str:
        return self.car_year + " " + self.car_make + " " + self.car_model + " " + self.repair_name + " $" + str(self.repair_cost)