from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.fields import CommaSeparatedIntegerField
from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from apps.backend.users.forms import BlogForm, EventsForm, UserRegistrationForm, EnquiryForm
from apps.backend.users.models import Blog, Enquiry,Events
from django.contrib import messages
from django.urls import reverse_lazy
from  apps.backend.users.models import User
from django.views.generic.edit import FormView

# Create your views here.

# def userRegister(request):
#     print('hello',request.method)
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
#         mobile = request.POST['mobile']
#         user = userReg.objects.filter(Email=email) 
#         if user:
#             message="User already exist"
#             print(message)
#             return render(request,"frontend/signup.html", {'msg':message}) 
#         else:
#             if password==cpassword:
#                 newuser = userReg.objects.create(Firstname=fname,Lastname=lname,Password=password,Email=email,Mobile=mobile)
#                 message="registration sucessfull"
#                 newuser.save()
#                 print(message)
#                 return redirect(reverse_lazy("hotel:userReg"))
#                 # return render(request,"frontend/index.html",{'msg':message})    
#             else:
#                 message="password doesn't match"
#                 print(message)
#                 return render(request,"frontend/signup.html", {'msg':message})

#     else:
#         return HttpResponse("none")      

      
class staffField(SuccessMessageMixin, CreateView):
        template_name='frontend/signup.html'
     
        form_class = UserRegistrationForm
        success_message = 'User Successfully Created'
        success_url = reverse_lazy('hotel:home')
       

        def form_valid(self, form):
            user = form.save(commit=False)
            user.is_buyer = True           
            user.save()
            messages.success(self.request, self.success_message)
            return redirect(self.success_url)

class StaffLogoutField(LogoutView):
    template_name = 'frontend/home.html'



class StaffLoginField(LoginView):
    template_name = 'frontend/login.html'  

    def get_success_url(self):
        return redirect(reverse_lazy('hotel:home'))

    # return super().get_success_url()

class ContactUsField(SuccessMessageMixin, CreateView):
    template_name = 'frontend/contact-us.html'



class EnquiryView(FormView):
   
    template_name = 'frontend/contact-us.html'
    form_class = EnquiryForm
    # print("1")

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.save()   
        print("2")
        return redirect(reverse_lazy('hotel:home')) 

class Eventsview(FormView):

    template_name = 'frontend/addevent.html'
    form_class = EventsForm
    
    def form_valid(self,form):
        event = form.save(commit=False)
        event.save()

        return redirect(reverse_lazy('hotel:events'))

def Eventdisplay(request):
    data = Events.objects.all()

    return render(request,'frontend/events.html',{'data':data})

class Blogview(FormView):

    template_name = 'frontend/addblog.html'
    form_class = BlogForm

    def form_valid(self,form):
        blog = form.save(commit= False)
        blog.image = form.cleaned_data['image']
        blog.save()

        return redirect(reverse_lazy('hotel:blog'))

def Blogdisplay(request):

    data = Blog.objects.all()

    return render(request,'frontend/blog.html',{'data':data})        




    
    
