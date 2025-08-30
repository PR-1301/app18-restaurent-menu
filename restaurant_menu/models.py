# To create a database model
from django.contrib.auth.models import User
from django.db import models

MEAL_TYPES = (("starters", "Starters"),
              ("salads", "Salads"),
              ("main_dishes", "Main dishes"),
              ("desserts", "Desserts")
              )

STATUS = ((0, "Unavailable"),
          (1, "Available"),
          )


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.CharField(max_length=100 ,choices=MEAL_TYPES)
    # PROTECT = user&dish, CASCADE= nouser&dish, SET_NULL=NOUSER, BUT DISH
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal

