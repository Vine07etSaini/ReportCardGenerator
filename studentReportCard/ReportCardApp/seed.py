from faker import Faker
import random as rd
from .models import * 
from django.db.models import Sum
from .models import *
fake=Faker()


def create_subject_marks(n):
    try:
        student_objs= Student.objects.all()
        for student in student_objs:
                subjects = Subject.objects.all()
                for subject in subjects:
                     SubjectMarks.objects.create(
                         subject=subject,
                         student=student,
                        marks=rd.randint(0,100)
                 )
    except Exception as e:
        print(e)        
def seed_db(n=10)->None:
    for i in range(0,n):
        departments_objs=Department.objects.all()
        random_index=rd.randint(0,len(departments_objs)-1)
        department=departments_objs[random_index]
        student_id=f'STU-0{rd.randint(100,999)}'
        student_name=fake.name()
        student_email=fake.email()
        student_age=rd.randint(20,30)
        student_addess=fake.address()

        student_id_obj=StudentID.objects.create(student_id=student_id)
        Student.objects.create(
           department=department,
            student_id=student_id_obj,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_addess=student_addess
        )

def generate_report_card():
       current_rank=-1
       i=1
       ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
       for rank in ranks:
             Rank.objects.create(
             student=rank,
             student_rank=i)
             i=i+1
            