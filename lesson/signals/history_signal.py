# Signal import(s)
from django.db.models.signals import pre_delete
from django.dispatch import receiver
# Local Imports
from lesson.models.human_model import Human
from lesson.models.history_model import DeletedHumansHistory

# Signal Functions
@receiver(pre_delete, sender=Human)
def recordDeletedHuman(sender, **kwargs):
    record = DeletedHumansHistory.objects.create(
        name = kwargs['instance'].full_name,
        humanId = kwargs['instance'].humanID
    )

