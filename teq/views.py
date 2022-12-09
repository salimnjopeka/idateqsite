from django.shortcuts import render, redirect
from .models import Contact, Applicant, TrainningProgram, GirlsInCode, JuniorProgrammer, ItService, Courses

# Create your views here.
def home(request):
    return render(request, 'idateq/home.html')

def services(request):
    return render(request, 'idateq/services.html')

def contact(request):
    if request.method == "POST":
        if request.POST.get('Email') and request.POST.get('Phone') and request.POST.get('Message'):
            post = Contact()
            post.Email = request.POST.get('Email')
            post.Phone = request.POST.get('Phone')
            post.Message = request.POST.get('Message')
            post.save()

        return render(request, 'idateq/contact.html')
    else:
        return render(request, 'idateq/contact.html')

def girls(request):
    training = TrainningProgram.objects.all()
    girls = GirlsInCode.objects.all()
    context = {'training': training, 'girls': girls}
    return render(request, 'idateq/girls.html', context)

def junior(request):
    training = TrainningProgram.objects.all()
    context = {'training': training}
    return render(request, 'idateq/junior.html', context)

def apply(request):
    course = Courses.objects.all()
    context = {'course': course}
    if request.method == "POST":
        # Fname = request.POST['Fname']
        # Lname = request.POST['Lname']
        # Gender = request.POST.get('Gender', False)
        # Address = request.POST['Address']
        # Email = request.POST['Email']
        # Contact = request.POST['Contact']
        # School = request.POST['School']
        # Section = request.POST['Section']
        # Level = request.POST['Level']
        # courses = request.POST['courses']
        # print(Fname,Lname,Gender,Address,Email,Contact,School,Section,Level,courses)
        if request.POST.get('Fname') and request.POST.get('Lname') and request.POST.get('Gender') and request.POST.get('Address') and request.POST.get('Email') and request.POST.get('Contact') and request.POST.get('School') and request.POST.get('Section') and request.POST.get('Level') and request.POST.get('courses'):
            post = Applicant()
            post.Fname = request.POST.get('Fname')
            post.Lname = request.POST.get('Lname')
            post.Gender = request.POST.get('Gender', False)
            post.Address = request.POST.get('Address')
            post.Email = request.POST.get('Email')
            post.Contact = request.POST.get('Contact')
            post.School = request.POST.get('School')
            post.Section = request.POST.get('Section')
            post.Level = request.POST.get('Level')
            post.Courses = request.POST.get('courses')
            post.save()
            
        return render(request, 'idateq/apply.html', context)
    else:
        return render(request, 'idateq/apply.html', context)

def project(request):
    return render(request, 'idateq/project.html')