from django.db import models
import datetime

# Create your models here.
class Experience(models.Model):
    name_of_company=models.CharField(max_length=200)
    starting_date=models.DateTimeField('Starting Date')
    ending_date=models.DateTimeField('Ending Date')
    is_current_work=models.BooleanField()
    