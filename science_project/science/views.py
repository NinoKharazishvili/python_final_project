from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .models import Scientist  

class CustomLoginView(LoginView):
    template_name = 'science/login.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('scientists')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('scientists')
        return super().get(*args, **kwargs)

class RegisterPage(FormView):
    template_name = 'science/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('scientists')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('scientists')
        return super(RegisterPage, self).get(*args, **kwargs)

class ScientistList(ListView):
    model = Scientist
    context_object_name = 'scientists'
    template_name = 'science/scientist_list.html'  

    def get_queryset(self):
        queryset = super().get_queryset()
        search_input = self.request.GET.get('search_area', '')
        if search_input:
            queryset = queryset.filter(
                Q(full_name__icontains=search_input)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_input'] = self.request.GET.get('search_area', '')
        context['is_search'] = 'search_area' in self.request.GET and self.request.GET['search_area'] != ''
        return context

class ScientistDetail(DetailView):
    model = Scientist
    template_name = "science/scientist.html"
    context_object_name = 'scientist'

class ScientistCreate(LoginRequiredMixin, CreateView):
    model = Scientist
    fields = '__all__'
    success_url = reverse_lazy('scientists')

class ScientistUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Scientist
    fields = '__all__'
    success_url = reverse_lazy('scientists')

    def test_func(self):
        scientist = self.get_object()
        return self.request.user == scientist.user or self.request.user.is_superuser

class ScientistDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Scientist
    context_object_name = 'scientist'
    success_url = reverse_lazy('scientists')

    def test_func(self):
        return self.request.user.is_superuser
