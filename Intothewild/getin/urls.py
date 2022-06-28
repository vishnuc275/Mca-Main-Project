from . import views
from django.contrib.auth import views as auth_view
from django.urls import path, include

app_name = "getin"

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('reg/', views.reg, name='reg'),
    path('staffreg/', views.staffreg, name='staffreg'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('userhome/', views.userhome, name='userhome'),
    path('snakehome/', views.snakehome, name='snakehome'),
    path('photohome/', views.photohome, name='photohome'),
    path('photoprofile/', views.photoprofile, name='photoprofile'),
    path('photofb/', views.photofb, name='photofb'),
    path('photopayment/', views.photopayment, name='photopayment'),
    path('caseregister/', views.caseregister, name='caseregister'),
    path('userfb/', views.userfb, name='userfb'),
    path('photoadd/', views.photoadd, name='photoadd'),
    path('wildgallery/', views.wildgallery, name='wildgallery'),
    path('staffreq/', views.staffreq, name='staffreq'),
    path('approvestaffreq/<str:email>', views.approvestaffreq, name='approvestaffreq'),
    path('staff/', views.staff, name='staff'),
    path('approvestaff/<str:email>', views.approvestaff, name='approvestaff'),
    path('deletestaff/<str:email>', views.deletestaff, name='deletestaff'),
    path('blockstaff/<str:email>', views.blockstaff, name='blockstaff'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),

]