from django.urls import path
from . import views
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
]
