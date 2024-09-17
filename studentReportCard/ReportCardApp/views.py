from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from .models import *
from .seed import *
# Create your views here.
def Home(request):
    return   render(request,'index.html')

def get_student(request):
    
    queryset= Student.objects.all()
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
  
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset= queryset.filter(  
         Q(student_name__icontains = search) |
        Q(department__department__icontains=search) |
        Q(student_id__student_id__icontains=search) |
        Q(student_email__icontains=search) |
        Q(student_age__icontains=search)
        )

    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request ,'student.html',context={'queryset':page_obj})
 
def see_marks(request, student_id):
      queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
      total_marks=queryset.aggregate(total_marks=Sum('marks'))        
      return render(request, 'see_marks.html',{'queryset':queryset,'total_marks':total_marks,})