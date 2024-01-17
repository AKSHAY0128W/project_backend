from django.contrib import admin
from django.urls import path,include
from homepage import views as homepage_views
from login_registration import views as login_registration_views
from calculators import views as calculators_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #pages
    path('', homepage_views.default, name="default"),
    path('homepage/', homepage_views.homepage, name="homepage"),
    path('aboutus/', homepage_views.aboutus, name="aboutus"),
    path('appointment/', homepage_views.appointment, name="appointment"),    
    path('dashboard/', homepage_views.dashboard, name="dashboard"),
    path('admin_dashboard/', homepage_views.admin_dashboard, name="admin_dashboard"),
    path('create_employee/', login_registration_views.create_employee, name='create_employee'),
    path('employee_panel/', homepage_views.employee_panel, name="employee_panel"),
    path('admin_login/', homepage_views.admin_login, name="admin_login"),
    path('services/', homepage_views.services, name="services"),

    # #Login Registration

    path('login/', login_registration_views.login_view, name="login"), 
    path('register/', login_registration_views.register, name="register"),  
    path('logout/', login_registration_views.logout_view, name="logout"),  

    #Calculators
    path('calculators/', calculators_views.Calculators, name="calculators"),
]