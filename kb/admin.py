from django.contrib import admin
from kb.models import Department, Course, Offering, Times

class OfferingInline(admin.TabularInline):
	model = Offering
	extra = 1

class CourseAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'title')
	inlines = [OfferingInline]

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Department)
admin.site.register(Offering)
admin.site.register(Times)