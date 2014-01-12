from django.db import models
from django.contrib.auth.models import User
from kb.models import Course, Offering
from common import TERM_CHOICES

# Create your models here.
class TermPlan(models.Model):
	year = models.IntegerField()
	term = models.IntegerField(choices=TERM_CHOICES)
	taking = models.ManyToManyField(Offering)

class Plan(models.Model):
	user = models.OneToOneField(User)
	grad_year = models.IntegerField()
	grad_term = models.IntegerField(choices=TERM_CHOICES)
	reqs = models.ManyToManyField(Course, blank=True)
	term_plans = models.ManyToManyField(TermPlan, blank=True)