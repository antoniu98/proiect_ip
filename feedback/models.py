from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Feedback(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title
