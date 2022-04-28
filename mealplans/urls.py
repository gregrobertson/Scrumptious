from django.urls import path

from mealplans.views import (
    MealPlanListView,
    MealPlanCreateView,
    MealPlanDetailView,
    MealPlanUpdateView,
    MealPlanDeleteView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="mealplans_list"),
    path("new/", MealPlanCreateView.as_view(), name="mealplans_new"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="mealplans_detail"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="mealplans_edit"),
    path(
        "<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal_plans_delete",
    ),
]
