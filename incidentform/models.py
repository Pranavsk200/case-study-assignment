from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Incident(models.Model):
    location = models.CharField(max_length=60)
    incidentDept = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField()
    incidentLoc = models.TextField()
    initialSeverity = models.CharField(max_length=60)
    cause = models.TextField()
    actionTaken = models.TextField()
    envInc = models.BooleanField(default= False)
    injury = models.BooleanField(default= False)
    properties = models.BooleanField(default=False)
    Vehical = models.BooleanField(default = False)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
