from django.db import models

# Human model
class Human(models.Model):
    full_name   = models.CharField(max_length=100)
    age         = models.IntegerField(default=20)
    humanID     = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.full_name

