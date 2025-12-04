from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib.auth import logout
from .forms import SignupForm

"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""

class UserLogin(LoginView):
    template_name = "users/login.html"

    # this or use LOGIN_REDIRECT_URL on settings.py
    def get_success_url(self):
        return reverse_lazy("home")
    


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect("home")


class UserSignup(CreateView):
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")
    form_class = SignupForm

    def form_valid(self, form):
        # if the data is valid, will save the record
        user = form.save(commit=False)
        pass_text = form.cleaned_data["password"]
        user.set_password(pass_text) # encrypt/hash the password
        user.save()

        return super().form_valid(form)
    