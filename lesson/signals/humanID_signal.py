# Signal import(s)
from django.db.models.signals import post_save
from django.dispatch import receiver
# Local Imports
from lesson.models.human_model import Human
from lesson.utils import generate_humanID

# Signal Functions
@receiver(post_save, sender=Human)
def addIDToHuman(sender, **kwargs):
    if kwargs['created']:
        getHuman        = kwargs['instance']
        getHuman.humanID= generate_humanID()
        getHuman.save()

        

