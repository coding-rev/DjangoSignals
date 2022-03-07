from django.db import models   

class DeletedHumansHistory(models.Model):
    name    = models.CharField(max_length=100)
    humanId = models.CharField(max_length=12)
    date    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    