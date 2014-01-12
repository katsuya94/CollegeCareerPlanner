from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pending(models.Model):
	user = models.OneToOneField(User)
	string = models.CharField(max_length=25)
	added = models.DateTimeField(auto_now_add=True)