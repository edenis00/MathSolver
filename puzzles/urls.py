from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.MathProblemListView.as_view(), name='mathproblem_list'),
    path('create/', views.MathProblemCreateView.as_view(), name='mathproblem_create'),
    path('detail/<int:pk>/', views.MathProblemDetailView.as_view(), name='mathproblem_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/logout/", LogoutView.as_view(next_page='mathproblem_list'), name="logout"),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
]
