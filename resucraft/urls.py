from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('userdata/', views.userdata, name='userdata'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('adddata/',views.adddata,name='adddata'),
    path('templates/',views.templates,name='templates'),
    path('template1',views.template1,name='template1'),
    path('template2',views.template2,name='template2'),
    path('template3',views.template3,name='template3'),
    path('template4',views.template4,name='template4'),
    path('template5',views.template5,name='template5'),
    path('template6',views.template6,name='template6'),
    path('template7',views.template7,name='template7'),
    path('template8',views.template8,name='template8'),
    path('template9',views.template9,name='template9'),


    path('terms',views.terms,name='terms'),
    path('privacy',views.privacy,name='privacy'),
path('about',views.about,name='about'),   
path('contact',views.contact,name='contact'),    
path('update_data/', views.update_data, name='update_data'),

]