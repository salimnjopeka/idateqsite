from django.shortcuts import render, redirect
from .models import Contact, Applicant, TrainningProgram, GirlsInCode, JuniorProgrammer, ItService

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
    if request.method == "POST":
        if request.POST.get('courses') and request.POST.get('Fname') and request.POST.get('Lname') and request.POST.get('Gender') and request.POST.get('Address') and request.POST.get('Email') and request.POST.get('Contact') and request.POST.get('School') and request.POST.get('Section') and request.POST.get('Level'):
            application = Applicant()
            application.Courses = request.POST.get('Courses')
            application.Fname = request.POST.get('Fname')
            application.Lname = request.POST.get('Lname')
            application.Gender = request.POST.get('Gender')
            application.Address = request.POST.get('Address')
            application.Contact = request.POST.get('Contact')
            application.School = request.POST.get('School')
            application.Section = request.POST.get('Section')
            application.Level = request.POST.get('Level')
            application.save()
        return render(request, 'idateq/apply.html')
    else:
        return render(request, 'idateq/apply.html')

def project(request):
    return render(request, 'idateq/project.html')