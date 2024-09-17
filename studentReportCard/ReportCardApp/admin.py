from django.contrib import admin
from .models import *
from django.db.models import Sum
# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)

admin.site.register(Student)
class SubjectMarksAdmin(admin.ModelAdmin):
     list_display=['student','subject','marks']
admin.site.register(Subject)
admin.site.register(SubjectMarks,SubjectMarksAdmin)
class RankAdmin(admin.ModelAdmin):
         list_display=['student','student_rank','total_marks','date_of_report_card_generation']
         ordering =  ['student_rank']
         def total_marks(self, obj):
                 subject_marks=SubjectMarks.objects.filter(student= obj.student)
                 marks=subject_marks.aggregate(marks=Sum('marks'))
                 return marks['marks']           

admin.site.register(Rank,RankAdmin)