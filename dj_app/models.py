from django.db import models

# Create your models here.
class client_info(models.Model):
    client_name = models.CharField(max_length=100)
    client_age = models.IntegerField()
    client_city = models.CharField(max_length=100)
    client_food = models.CharField(max_length=100, null=True)
    client_phone = models.CharField(max_length=20, null=True)
    client_image = models.CharField(max_length=200, null=True)
    client_id = models.IntegerField()

    def __str__(self):
        return f"{self.client_name} {self.client_city} {self.client_age}"

class client_payments(models.Model):
    client_name = models.CharField(max_length=100)
    client_money = models.IntegerField()
    client_id = models.IntegerField()

    def __str__(self):
        return f"{self.client_name} {self.client_money}"