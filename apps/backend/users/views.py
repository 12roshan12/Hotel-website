from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import templatize
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import EnquiryForm, UserRegistrationForm, UserUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Events, User
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
class UserRegistrationField(SuccessMessageMixin, CreateView):
    template_name = 'backend/user/register.html'
    form_class = UserRegistrationForm
    success_message = 'User Successfully Created'
    success_url = reverse_lazy('backend.users:index')
    

    def form_valid(self, form):
        
        user = form.save(commit=False)
        user_type = form.cleaned_data['user_types']
        if user_type == 'is_buyer':
            user.is_buyer = True
        elif user_type == 'is_seller':
            user.is_seller = True

        user.save()
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)


class UserLoginField(LoginView):
    template_name = 'backend/user/login.html'


class UserLogoutField(LogoutView):
    template_name = 'backend/user/login.html'


class IndexUserView(ListView):
    template_name = 'backend/user/index.html'
    model = User
    context_object_name = 'users'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexUserView, self).get_context_data(**kwargs)
        context['users'] = User.object.all()
        return context


class UpdateUserView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'backend/user/register.html'
    success_message = 'User Successfully Updated'
    success_url = reverse_lazy()
    form_class = UserUpdateForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateUserView, self).get(self, request, *args, **kwargs)

    def get_success_url(self):
        return reverse('backend.users:index')


class DeleteUserView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'backend/layouts/partial/delete.html'
    success_message = 'User Successfully deleted'
    success_url = reverse_lazy('backend.users:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(DeleteUserView, self).get(self, request, *args, **kwargs)


