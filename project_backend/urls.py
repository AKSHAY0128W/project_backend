from django.contrib import admin
from django.urls import path
from homepage import views as homepage_views
from login_registration import views as login_registration_views
from calculators import views as calculators_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Homepage
    path('', homepage_views.default, name="default"),
    path('homepage/', homepage_views.homepage, name="homepage"),
    path('aboutus/', homepage_views.aboutus, name="aboutus"),
    path('appointment/', homepage_views.appointment, name="appointment"),
    path('dashboard/', homepage_views.dashboard, name="dashboard"),

    # #Login Registration
    path('login/', login_registration_views.login_view, name="login"),  # Corrected line
    path('register/', login_registration_views.register, name="register"),  # Corrected line
    path('logout/', login_registration_views.logout_view, name="logout"),  # Corrected line
    #Calculators
    path('calculators/', calculators_views.Calculators, name="calculators"),
]