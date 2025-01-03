from django.db.models import Q
from .models import MathProblem
from .forms import MathProblemForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .utils import solve_math_problem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.
class MathProblemCreateView(LoginRequiredMixin, CreateView):
    model = MathProblem
    form_class = MathProblemForm
    template_name = 'puzzles/mathproblem_form.html'
    success_url = reverse_lazy('mathproblem_list')
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        question = form.cleaned_data['question']
        
        try:
            solution = solve_math_problem(question)
            form.instance.solution = solution
        except ValueError as e:
            form.add_error('question', str(e))
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
    
class MathProblemListView(ListView):
    model = MathProblem
    template_name = 'puzzles/mathproblem_list.html'
    context_object_name = 'mathproblems'
    paginate_by = 5
        
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(question__icontains=query) |
                Q(solution__icontains=query)
            )
        return queryset
    
    
class MathProblemDetailView(DetailView):
    model = MathProblem
    template_name = 'puzzles/mathproblem_detail.html'
    context_object_name = 'mathproblem'
    
    
    
class MathProblemUpdateView(LoginRequiredMixin, UpdateView):
    model = MathProblem
    form_class = MathProblemForm
    template_name = 'puzzles/mathproblem_form.html'
    success_url = reverse_lazy('mathproblem_detail')    
    login_url = reverse_lazy('login')
    
    
class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    