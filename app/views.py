from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage, send_mail
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .decorators import admin_only, unauthenticated_user
from .forms import CreateUserForm
from .models import *
from django.template.loader import render_to_string, get_template

from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def HomeView(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        print(course)

    return render(request, 'home.html', {})
@unauthenticated_user
def SignupView(request):    
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # fullname = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            
            # messages.success(request, 'Account was created for ' + username)

            subject = "Hello from Exobytes!"
            message = render_to_string('gmail-template.html')
            text_content = strip_tags(message)

            email_obj = EmailMultiAlternatives (
                subject,
                text_content,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email_obj.attach_alternative(message, "text/html")
            email_obj.send()
            # send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
            # template = render_to_string('accounts/email_template.html', {'name':username})

            # email = EmailMessage(
            #     'This is a test email from Django',
            #     template,
            #     settings.EMAIL_HOST_USER,
            #     [email],
            # )

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'signup.html', context)

@unauthenticated_user
def LoginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(username)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    print('logged out the user')
    return redirect('home')

# @login_required(login_url='login')
# # @authenicated_user
# def userPage(request):
#     context = {'orders': 'my_order'}
#     return render(request, 'user.html', context)
def DashboardView(request):
    # print("here")
    # if request.user.groups.filter(name="Verified"):
    #     print("inside if")
    #     if request.user.groups.filter(name="Subsystems"):
    #         print("inside another if")
    #         course = CourseType.objects.get(course_name="SS")
    #         context = {'links':ZoomLinks.objects.filter(course=course)}
    #         # print(str(context), "I'm here")
    #         return render(request, 'dashboard.html', context)
    #     elif request.user.groups.filter(name="Motion1"):
    #         course = CourseType.objects.get(course_name="M1")
    #         context = {}
    #         return render(request, 'dashboard.html', context)
    #     else:
    #         course = CourseType.objects.get(course_name="M2")
    #         # context = {'links':ZoomLinks.objects.filter(course=course).get()}
    #         context = {}
    #         # print(context)
    #         return render(request, 'dashboard.html', context)
    # else:
    #     return render(request, 'not-verified.html', {})
    
    # return render(request, 'dashboard.html', {})
    group = Group.objects.get(name='Verified')
    print('here')
    course_selection = ''
    if request.body:
        print('inside set group')
        group.user_set.add(request.user)
        course_selection = request.body
        print(course_selection)
    if request.user.groups.filter(name="Verified"):
        if course_selection == "SS":
            course = CourseType.objects.get(course_name="SS")
            # context = {'links':ZoomLinks.objects.filter(course=course)}
            context = {}
            return render(request, 'dashboard.html', context)
        elif course_selection == "M1":
            course = CourseType.objects.get(course_name="M1")
            context = {}
            return render(request, 'dashboard.html', context)
        else:
            course = CourseType.objects.get(course_name="M2")
            # context = {'links':ZoomLinks.objects.filter(course=course).get()}
            context = {}
            # print('gonna redirect')
            # return redirect('dashboard')
            return render(request, 'dashboard.html', context)
    else:
        return render(request, 'not-verified.html', {})

def CourseDetailView(request, course_id):
    if course_id != 'SS' and course_id != 'M1' and course_id != 'M2':
        return redirect('home')
    return render(request, 'course-details.html', {'course':course_id})

# def GmailThingView(request):
#     return render(request, 'gmail-template.html', {})