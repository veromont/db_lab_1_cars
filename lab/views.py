from django.views.generic import ListView
from lab.DAL.models import CarModel


class CarModelsListView(ListView):
    model = CarModel
    template_name = 'generic-model-view.html'
