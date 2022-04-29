from django.shortcuts import redirect
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


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "mealplans/detail.html"


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "mealplans/new.html"
    fields = ["name", "date", "recipes"]
    # success_url = reverse_lazy("mealplans_list")

    # def get_success_url(self) -> str:
    #     return reverse_lazy("mealplan_detail", args[self.object.id])

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("mealplans_detail", pk=plan.id)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "mealplans/edit.html"
    fields = ["name"]
    success_url = reverse_lazy("mealplans_list")


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "mealplans/delete.html"
    success_url = reverse_lazy("mealplans_list")
