from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import UserData
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserData, Skill, Language, Expertise, ComputerSkill, Institution, Job, Link,Project
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
from django.shortcuts import redirect
@login_required(login_url='/login/')


def view_profile(request):
    try:
        user_data = request.user.userdata
        return render(request, 'result.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'result.html', {'no_data_message': no_data_message})
@login_required(login_url='/login/')
def template1(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume1.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume1.html', {'no_data_message': no_data_message})
@login_required(login_url='/login/')
def template2(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume2.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume2.html', {'no_data_message': no_data_message})


@login_required(login_url='/login/')
def template3(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume3.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume3.html', {'no_data_message': no_data_message})

@login_required(login_url='/login/')
def template4(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume4.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume4.html', {'no_data_message': no_data_message})

@login_required(login_url='/login/')
def template5(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume5.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume5.html', {'no_data_message': no_data_message})
@login_required(login_url='/login/')
def template6(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume4.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume4.html', {'no_data_message': no_data_message})
@login_required(login_url='/login/')
def template7(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume8.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume8.html', {'no_data_message': no_data_message})
@login_required(login_url='/login/')
def template8(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume8.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume8.html', {'no_data_message': no_data_message})
@login_required(login_url='/login/')
def template9(request):
    try:
        user_data = request.user.userdata
        return render(request, 'resume4.html', {'user_data': user_data})
    except UserData.DoesNotExist:
        no_data_message = "You've not entered any data."
        return render(request, 'resume4.html', {'no_data_message': no_data_message})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or any other desired URL after logout
    
def userdata(request):
    if request.method == 'POST':
        # Extract data from the form
        user = request.user
        name = request.POST.get('name')
        title=request.POST.get('title')
        description = request.POST.get('desc')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        skills = request.POST.getlist('skills[]')
        skill_percentages = request.POST.getlist('skill_percentages[]')
        projectnames=request.POST.getlist('projectnames[]')
        projects=request.POST.getlist('projects[]')
        languages = request.POST.getlist('languages[]')
        expertises = request.POST.getlist('expertises[]')
        computer_skills = request.POST.getlist('computer_skills[]')
        institutions = request.POST.getlist('institutions[]')
        eddescription=request.POST.getlist('eddescription[]')
        years_studied = request.POST.getlist('years_studied[]')
        job_names = request.POST.getlist('job_names[]')
        job_place=request.POST.getlist('job_place[]')
        job_durations = request.POST.getlist('job_durations[]')
        job_descriptions = request.POST.getlist('job_descriptions[]')
        link_names = request.POST.getlist('link_names[]')
        links = request.POST.getlist('links[]')

        # Save the uploaded profile picture
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name, profile_picture)

        # Create a new UserData instance and save it
        new_data = UserData(
            user=user,
            name_of_user=name,
            title=title,
            description=description,
            
            contact_email=email,
            phone_number=phone,
            profile_picture=profile_picture,
            address=address
        )
        new_data.save()

        # Add skills to the UserData instance
        for i in range(len(skills)):
            skill_name = skills[i]
            if i < len(skill_percentages):
                skill_percentage = skill_percentages[i]
            else:
                skill_percentage = 0  # Default value if not provided
            skill, created = Skill.objects.get_or_create(skill=skill_name, percentage=skill_percentage)
            new_data.skills.add(skill)

        for i in range(len(projects)):
            project_names=projectnames[i]
            if i<len(projects):
                project_descr=projects[i]
            else:
                project_descr=''
            project,created= Project.objects.get_or_create(projectnames=project_names,project_desc=project_descr)
            new_data.projects.add(project)

        # Add languages to the UserData instance
        for language_name in languages:
            language, created = Language.objects.get_or_create(name=language_name)
            new_data.languages.add(language)

        # Add expertises to the UserData instance
        for expertise_name in expertises:
            expertise, created = Expertise.objects.get_or_create(name=expertise_name)
            new_data.expertises.add(expertise)

        # Add computer skills to the UserData instance
        for computer_skill_name in computer_skills:
            computer_skill, created = ComputerSkill.objects.get_or_create(name=computer_skill_name)
            new_data.computer_skills.add(computer_skill)

        # Add education to the UserData instance
        for i in range(len(institutions)):
            institution_name = institutions[i]
            if i < len(years_studied):
                years_studied_value = years_studied[i]
            else:
                years_studied_value = ''
            if i < len(eddescription):
                eddescriptions = eddescription[i]
            else:
                eddescriptions = ''
            institution, created = Institution.objects.get_or_create(name=institution_name, years_studied=years_studied_value,description=eddescriptions)
            new_data.education.add(institution)

        # Add jobs to the UserData instance
        for i in range(len(job_names)):
            job_name = job_names[i]
            if i < len(job_durations):
                job_duration = job_durations[i]
            else:
                job_duration = ''  # Default value if not provided
            if i < len(job_descriptions):
                job_description = job_descriptions[i]
            else:
                job_description = ''
            if i<len(job_place):
                job_places=job_place[i]
            else:
                job_places=''
            job, created = Job.objects.get_or_create(name=job_name,jobplace=job_places, duration=job_duration, description=job_description)
            new_data.work_experiences.add(job)

        for i in range(len(link_names)):
            link_name = link_names[i]
            if i < len(links):
                link_value = links[i]
            else:
                link_value = ''  # Default value if not provided
            link, created = Link.objects.get_or_create(name=link_name, link=link_value)
            new_data.links.add(link)

        # Redirect to a success page or render a success message
        return render(request, 'result.html')

    # Render the user data form
    return render(request, 'result.html')

def templates(request):
    return render(request,'templates.html')

def about(request):
    return render(request,'about.html')
    
def privacy(request):
    return render(request,'privacy.html')
    
def terms(request):
    return render(request,'term.html')
def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['passw']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html') 
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')

 
    else:
        return render(request, 'login.html')
        
@login_required(login_url='/login/')
def adddata(request):
    if request.user.is_authenticated:
        user = request.user
        user_data = UserData.objects.filter(user=user).first()
        if user_data:
            # If user data exists, render an update form
            return render(request, 'update.html', {'user_data': user_data})
        else:
            user_data_exists = False  # Set the flag accordingly
            context = {
                'user_data_exists': user_data_exists,
            }
            return render(request, 'input.html', context)
    else:
        # If the user is not authenticated, handle it as needed (redirect to login or show a message)
        return render(request, 'login_required.html')
    
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['passw1']
        confpassw = request.POST['passw2']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            return render(request, 'register.html')
        if password == confpassw:
            user = User.objects.create_user(username=username, password=password, email=email)
            auth.login(request, user)  
            return render(request, 'login.html') 
        else:
            alert_msg="password is not matching"
            return render(request, 'register.html',{'alert_msg':alert_msg})

    return render(request, 'register.html')

def home(request):

    return render(request,'home.html')
# views.py
# views.py
from django.shortcuts import get_object_or_404

@login_required(login_url='/login/')
def update_data(request):
    if request.method == 'POST':
        user = request.user
        user_data = UserData.objects.filter(user=user).first()

        if user_data:
            # Update existing UserData instance
            user_data.name_of_user = request.POST.get('name')
            user_data.title = request.POST.get('title')
            user_data.description = request.POST.get('desc')
            user_data.contact_email = request.POST.get('email')
            user_data.phone_number = request.POST.get('phone')
            user_data.address = request.POST.get('address')

            # Update profile picture if provided
            profile_picture = request.FILES.get('profile_picture')
            if profile_picture:
                user_data.profile_picture = profile_picture

            # Update skills
            user_data.skills.clear()
            skills = request.POST.getlist('skills[]')
            skill_percentages = request.POST.getlist('skill_percentages[]')
            for i in range(len(skills)):
                skill_name = skills[i]
                if i < len(skill_percentages):
                    skill_percentage = skill_percentages[i]
                else:
                    skill_percentage = 0  # Default value if not provided
                skill, created = Skill.objects.get_or_create(skill=skill_name, percentage=skill_percentage)
                user_data.skills.add(skill)

            # Update projects
            user_data.projects.clear()
            projectnames = request.POST.getlist('projectnames[]')
            projects = request.POST.getlist('projects[]')
            for i in range(len(projectnames)):
                project_name = projectnames[i]
                if i < len(projects):
                    project_descr = projects[i]
                else:
                    project_descr = ''
                project, created = Project.objects.get_or_create(projectnames=project_name, project_desc=project_descr)
                user_data.projects.add(project)

            # Update expertises
            user_data.expertises.clear()
            expertises = request.POST.getlist('expertises[]')
            for expertise_name in expertises:
                expertise, created = Expertise.objects.get_or_create(name=expertise_name)
                user_data.expertises.add(expertise)

            # Update computer skills
            user_data.computer_skills.clear()
            computer_skills = request.POST.getlist('computer_skills[]')
            for computer_skill_name in computer_skills:
                computer_skill, created = ComputerSkill.objects.get_or_create(name=computer_skill_name)
                user_data.computer_skills.add(computer_skill)

            # Update education
            user_data.education.clear()
            institutions = request.POST.getlist('institutions[]')
            years_studied = request.POST.getlist('years_studied[]')
            eddescription = request.POST.getlist('eddescription[]')
            for i in range(len(institutions)):
                institution_name = institutions[i]
                if i < len(years_studied):
                    years_studied_value = years_studied[i]
                else:
                    years_studied_value = ''
                if i < len(eddescription):
                    eddescriptions = eddescription[i]
                else:
                    eddescriptions = ''
                institution, created = Institution.objects.get_or_create(name=institution_name, years_studied=years_studied_value, description=eddescriptions)
                user_data.education.add(institution)

            # Update jobs
            user_data.work_experiences.clear()
            job_names = request.POST.getlist('job_names[]')
            job_place = request.POST.getlist('job_place[]')
            job_durations = request.POST.getlist('job_durations[]')
            job_descriptions = request.POST.getlist('job_descriptions[]')
            for i in range(len(job_names)):
                job_name = job_names[i]
                if i < len(job_durations):
                    job_duration = job_durations[i]
                else:
                    job_duration = ''  # Default value if not provided
                if i < len(job_descriptions):
                    job_description = job_descriptions[i]
                else:
                    job_description = ''
                if i < len(job_place):
                    job_places = job_place[i]
                else:
                    job_places = ''
                job, created = Job.objects.get_or_create(name=job_name, jobplace=job_places, duration=job_duration, description=job_description)
                user_data.work_experiences.add(job)

            # Update languages
            user_data.languages.clear()
            languages = request.POST.getlist('languages[]')
            for language_name in languages:
                language, created = Language.objects.get_or_create(name=language_name)
                user_data.languages.add(language)

            # Update links
            user_data.links.clear()
            link_names = request.POST.getlist('link_names[]')
            links = request.POST.getlist('links[]')
            for i in range(len(link_names)):
                link_name = link_names[i]
                if i < len(links):
                    link_value = links[i]
                else:
                    link_value = ''  # Default value if not provided
                link, created = Link.objects.get_or_create(name=link_name, link=link_value)
                user_data.links.add(link)

            # Save the updated UserData instance
            user_data.save()

            return render(request, 'result.html', {'user_data': user_data})
        else:
            # Handle the case when user data does not exist
            no_data_message = "User data does not exist."
            return render(request, 'result.html', {'no_data_message': no_data_message})

    return render(request, 'update.html', {'user_data': user_data})
