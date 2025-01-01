from django.urls import path
from . import views

urlpatterns = [
    path('', views.MathProblemListView.as_view(), name='mathproblem_list'),
    path('create/', views.MathProblemCreateView.as_view(), name='mathproblem_create'),
    path('detail/<int:pk>/', views.MathProblemDetailView.as_view(), name='mathproblem_detail'),
]
