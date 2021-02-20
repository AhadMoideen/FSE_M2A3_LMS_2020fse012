from django.contrib import admin

from .models import Course, Module,EvaluationComponent

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(EvaluationComponent)