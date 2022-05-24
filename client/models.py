from django.db import models

GENDER = [('f', 'Female'), ('m', 'Male')]
CIVIL_STATUS = [('s', 'Single'), ('m', 'Married'), ('w', 'Widower'), ('d', 'Divorced')]

class Client(models.Model):
   name = models.CharField(max_length=100)
   gender = models.CharField(max_length=1, choices=GENDER)
   civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS)
   phone = models.CharField(max_length=11, blank=True)
   email = models.EmailField(blank=True)

   def __str__(self):
      return self.name
