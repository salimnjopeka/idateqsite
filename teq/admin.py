from django.contrib import admin
from .models import Courses, Applicant, Contact, TrainningProgram, GirlsInCode, JuniorProgrammer, ItService, Project
# Register your models here.
admin.site.register(Applicant)
admin.site.register(Courses)
admin.site.register(Contact)
admin.site.register(TrainningProgram)
admin.site.register(GirlsInCode)
admin.site.register(JuniorProgrammer)
admin.site.register(ItService)
admin.site.register(Project)
