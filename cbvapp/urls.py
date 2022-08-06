
from django.urls import path
from django.views.generic import TemplateView
from .import views as v

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('addemp', v.EmpFormView.as_view()),
    path('saveemp', v.EmpCreateView.as_view()),
    path('listemp', v.EmpListView.as_view()),
    path('editemp/<int:pk>', v.EmpEditView.as_view()),
    path('deleteemp/<int:pk>', v.EmpDeleteView.as_view()),
]
