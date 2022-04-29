from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from mealplans.models import MealPlan


# Create your views here.
class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "mealplans/list.html"
    paginate_by = 8
    context_object_name = "banana"


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "mealplans/detail.html"


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "mealplans/new.html"
    fields = ["name"]
    success_url = reverse_lazy("mealplans_list")


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "mealplans/edit.html"
    fields = ["name"]
    success_url = reverse_lazy("mealplans_list")


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "mealplans/delete.html"
    success_url = reverse_lazy("mealplans_list")
