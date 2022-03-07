# Signal import(s)
from django.db.models.signals import post_save
from django.dispatch import receiver
# Local Imports
from lesson.models.human_model import Human
from lesson.models.car_model import Car

# Signal Functions
@receiver(post_save, sender=Human)
def createCarForHuman(sender, **kwargs):
    if kwargs['created']:
        human_car = Car.objects.create(
            person = kwargs['instance']
        )

