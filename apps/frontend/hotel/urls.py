from django.urls import path
from . import views
from .views import *

from django.views.generic import TemplateView, RedirectView

app_name = 'hotel'
urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='home'),
    path('contact-us/', EnquiryView.as_view(), name='contact-us'),
    path('about-us/', TemplateView.as_view(template_name='frontend/about-us.html'), name='about-us'),
    path('gallery1/', TemplateView.as_view(template_name='frontend/gallery1.html'), name='gallery1'),
    path('gallery2/', TemplateView.as_view(template_name='frontend/gallery2.html'), name='gallery2'),
    path('login/',StaffLoginField.as_view() , name='login'),
    path('room/', TemplateView.as_view(template_name='frontend/room.html'), name='room'),
    path('room-list/', TemplateView.as_view(template_name='frontend/room-list.html'), name='room-list'),
    path('room-detail/', TemplateView.as_view(template_name='frontend/room-detail.html'), name='room-detail'),
    # path('signup/', TemplateView.as_view(template_name='frontend/signup.html'), name='signup'),
    # path('register', views.userRegister, name='userReg'),
    # path('logout/', staffLogout.as_view(),name='logout'),
    path('signup/',staffField.as_view(),name="signup"),
    path('logout/',StaffLogoutField.as_view(),name="logout"),
    path('staff/', TemplateView.as_view(template_name='frontend/staff.html'), name='staff'),
    path('addevent/',Eventsview.as_view(),name='addevent'),
    path('events/',Eventdisplay,name='events'),
    path('blog/', Blogdisplay,name='blog'),
    path('addblog/', Blogview.as_view(), name='addblog')
    
]
