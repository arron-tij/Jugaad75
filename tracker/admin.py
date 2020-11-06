from django.contrib import admin

from .models import classroom,Lecture,lecture_copy
# Register your models here.

admin.site.register(classroom)
admin.site.register(Lecture)

admin.site.register(lecture_copy)