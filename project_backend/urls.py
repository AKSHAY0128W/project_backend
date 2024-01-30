from django.contrib import admin
from django.urls import path,include
from homepage import views as homepage_views
from login_registration import views as login_registration_views
from calculators import views as calculators_views
from display import views as display_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include



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

    path('myservices/', homepage_views.myservices, name="myservices"),

    #admin_panel_pages
    path('add_employee/',homepage_views.admin_create_employee, name="add_employee"),
    path('admin_homepage/', homepage_views.admin_homepage, name="admin_homepage"),
    path('admin_service_details', homepage_views.admin_service_details, name="admin_employee_details"),


    #display
    path('emp_display/', display_views.emp_display, name="emp_display"),
    path('emp_edit/', display_views.emp_edit, name="emp_edit"),
    path('update/<int:employee_id>', display_views.emp_update, name="update"),
    path('delete/<int:employee_id>', display_views.emp_delete, name="delete"),

    path('add_service/', display_views.add_service, name='add_service'),
    path('services_list/', display_views.services_list, name='services_list'),
    path('services_edit/', display_views.services_edit, name='services_edit'),
    path('services_update/<int:id>', display_views.services_update, name='services_update'),
    path('services_delete/<int:id>', display_views.services_delete, name='services_delete'),

    path('add_packages/', display_views.add_packages, name='add_packages'),
    path('packages_list/', display_views.packages_list, name='packages_list'),
    path('packages_edit/', display_views.packages_edit, name='packages_edit'),
    path('packages_update/<int:id>', display_views.packages_update, name='packages_update'),
    path('packages_delete/<int:id>', display_views.packages_delete, name='packages_delete'),

    path('customer_list/', display_views.customer_list, name='customer_list'),
    path('customer_delete/<int:id>', display_views.customer_delete, name='customer_delete'),
    # #Login Registration

    path('login/', login_registration_views.login_view, name="login"), 
    path('register/', login_registration_views.register, name="register"),  
    path('logout/', login_registration_views.logout_view, name="logout"),  

    #Calculators
    path('calculators/', calculators_views.Calculators, name="calculators"),



    #course
    path('course/', include('course.urls')),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

