from .models import Socios
from .forms import SociosForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

# Create your views here.
class Index(TemplateView):
    template_name = "core/index.html"
    
class SociosListView(ListView):
    model = Socios
    
class SociosCreateView(CreateView):
    model = Socios
    form_class = SociosForm 
    success_url = reverse_lazy('socios:socios-list')

class SociosDeleteView(DeleteView):
    model = Socios
    success_url = reverse_lazy("socios:socios-list")
    
class SociosUpdateView(UpdateView):
    model = Socios
    form_class = SociosForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('socios:socios-list')