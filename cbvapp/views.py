from django.shortcuts import render
from .models import Emp, EmpForm
from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView

class EmpFormView(FormView):
    form_class=EmpForm
    template_name='form.html'

class EmpCreateView(CreateView):
    model=Emp
    fields="__all__"
    success_url='/'

class EmpListView(ListView):
    model=Emp
    template_name='emplist.html'

class EmpEditView(UpdateView):
    model=Emp
    fields="__all__"
    template_name='empeditform.html'
    success_url='/listemp'

class EmpDeleteView(DeleteView):
    model=Emp
    template_name='delete.html'
    success_url='/listemp'