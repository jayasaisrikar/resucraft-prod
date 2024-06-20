from django.contrib.auth.models import User
from django.db import models

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(default=0)
class Project(models.Model):
    projectnames=models.CharField(max_length=100)
    project_desc=models.TextField()
class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField() 
class Institution(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    years_studied = models.CharField(max_length=50)
    

class Job(models.Model):
    name = models.CharField(max_length=100)
    jobplace=models.CharField(max_length=40)
    duration = models.CharField(max_length=50)
    description = models.TextField()


class Language(models.Model):
    name = models.CharField(max_length=100)

class Expertise(models.Model):
    name = models.CharField(max_length=100)

class ComputerSkill(models.Model):
    name = models.CharField(max_length=100)

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_of_user=models.TextField(blank=True)
    title=models.TextField(blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    projects = models.ManyToManyField(Project,blank=True)
    work_experiences = models.ManyToManyField(Job, blank=True)
    education = models.ManyToManyField(Institution, blank=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True)
    expertises = models.ManyToManyField(Expertise, blank=True)
    links = models.ManyToManyField(Link, blank=True)
    computer_skills = models.ManyToManyField(ComputerSkill, blank=True)
