from django.db import models
from common import TERM_CHOICES, TIMES_CHOICES, num2term

# Create your models here.
class Department(models.Model):
	label = models.CharField(max_length=50)
	def __unicode__(self):
		return self.label

class Course(models.Model):
	dept = models.ForeignKey(Department)
	num = models.CharField("Course Number", max_length=50)
	title = models.CharField(max_length=200)
	def __unicode__(self):
		return self.dept.label + " " + self.num

class Times(models.Model):
	# ex. 4:30 am is represented by 9
	# ex. 3:30 pm is represented by 31
	mon = models.IntegerField(choices=TIMES_CHOICES)
	tue = models.IntegerField(choices=TIMES_CHOICES)
	wed = models.IntegerField(choices=TIMES_CHOICES)
	thu = models.IntegerField(choices=TIMES_CHOICES)
	fri = models.IntegerField(choices=TIMES_CHOICES)
	duration = models.IntegerField()

class Offering(models.Model):
	course = models.ForeignKey(Course)
	year = models.IntegerField()
	term = models.IntegerField(choices=TERM_CHOICES)
	instructor = models.CharField(max_length=200)
	times = models.OneToOneField(Times)
	def __unicode__(self):
		return self.course.__unicode__() + " " + num2term(self.term) + " " + str(self.year)