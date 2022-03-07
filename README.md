# DjangoSignals
DjangoSignals Under Study

# Content
## Post_Save Signal Function
### post_save signal function is sent at the end of the save() method.
1. Car signal that automatically creates a car model for new user

## Pre_Save  Signal Function
### This is sent at the beginning of a model’s save() method.
2. HumanID signal that adds an ID to created Human automatically

## Pre_delete Function
### Sent at the beginning of a model’s delete() method and a queryset’s delete() method.
1. Signal that records model deletion in HISTORY MODEL

# Signal Creation Flow
1. Design the signal function
2. Register the signal file to the apps.py
