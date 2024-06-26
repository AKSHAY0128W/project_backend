from django.contrib import admin
from django.urls import path,include
from homepage import views as homepage_views
from login_registration import views as login_registration_views
from calculators import views as calculators_views
from display import views as display_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from course import views as course_views


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


    path('test/', homepage_views.test, name="test"),

    path('customer_homepage/', homepage_views.customer_homepage, name="customer_homepage"),
    path('employee_schedule/', homepage_views.employee_schedule, name="employee_schedule"),
    path('employee_panel/', homepage_views.employee_panel, name="employee_panel"),
    path('admin_login/', homepage_views.admin_login, name="admin_login"),
    
    path('services/', homepage_views.services, name="services"),
    path('service_booking/<int:id>/', homepage_views.service_booking, name='service_booking'),
    path('myservices/', homepage_views.myservices, name="myservices"),
    path('service_booking_admin/', display_views.service_booking_admin, name='service_booking_admin'),
    path('booking_delete/<int:id>', display_views.booking_delete, name='booking_delete'),


    path('package_booking/<int:id>/', homepage_views.package_booking, name='package_booking'),
    path('package_booking_admin/', display_views.package_booking_admin, name='package_booking_admin'),


    #admin_panel_pages
    path('admin_homepage/', homepage_views.admin_homepage, name="admin_homepage"),
    path('admin_service_details', homepage_views.admin_service_details, name="admin_employee_details"),
    path('admin_employee_service_schedule', homepage_views.admin_employee_service_schedule, name="admin_employee_service_schedule"),
    path('admin_package_schedule', homepage_views.admin_package_schedule, name="admin_package_schedule"),
    path('admin_appointment_list', display_views.admin_appointment_list, name="admin_appointment_list"),
    #packages

    path('packages/', homepage_views.mypackages, name="packages"),


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


    #Emoploee
    path('employee_customer_list/', display_views.employee_customer_list, name='employee_customer_list'),
    path('employee_appointment_list/', display_views.employee_appointment_list, name='employee_appointment_list'),
    path('employee_service_booking_list/', display_views.employee_service_booking_list, name='employe_service_booking_list'),
    path('employee_payment_list/', display_views.employee_payment_list, name='employee_payment_list'),
    path('employee_package_booking_list/', display_views.employee_package_booking_list, name='employee_package_booking_list'),

    #course
    path('course/', include('course.urls')),
    path('customer_my_courses',course_views.customer_my_courses, name="customer_my_courses"),
    path('admin_course_create/',course_views.course_create_view, name="admin_course_create"),
    path('course_booking/<int:id>', course_views.course_booking, name='course_booking'),
    path('admin_course_booking_details', homepage_views.admin_course_booking_details, name='admin_course_booking_details'),
    path('admin_course_details/',course_views.course_list_view, name="admin_course_details"),
    path('course_update_view/<int:id>',course_views.course_update_view, name="course_update_view"),
    path('course_delete_view/<int:id>',course_views.course_delete_view, name="course_delete_view"),
    # path('make_payment/<int:id>', homepage_views.make_payment, name="make_payment"),
    path('payment_list/', display_views.payment_list, name='payment_list'),


# calcutators  
    path('income_tax_calculator/', calculators_views.income_tax_calculator, name="income_tax_calculator"),
    path('sip_calculator/', calculators_views.sip_calculator, name="sip_calculator"),
    path('gst_calculator/', calculators_views.gst_calculator, name="gst_calculator"),



    #customers
    path('customer_my_services/', homepage_views.customer_my_services, name="customer_my_services"),
    path('customer_my_packages/', homepage_views.customer_my_packages, name="customer_my_packages"),
    path('customer_my_profile/', login_registration_views.customer_my_profile, name="customer_my_profile"),
    path('customer_my_appointments/', homepage_views.customer_my_appointments, name="customer_my_appointments"),
    

    # path('temp', login_registration_views.temp, name="temp"),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

