from django.db import models

class Candy(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sweetness = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name