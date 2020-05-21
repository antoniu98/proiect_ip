from django.db import models

# Create your models here.
class Advertisment(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    capacity = models.IntegerField(blank = True, null = True)
    conditions = models.CharField(max_length = 100, blank = True)
    image = models.ImageField(upload_to = 'ads/imgs/', null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

