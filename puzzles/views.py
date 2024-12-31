from django.views.generic import ListView, DetailView, CreateView
from .models import MathProblem
from django.urls import reverse_lazy
from .utils import solve_math_problem

# Create your views here.
class MathProblemCreateView(CreateView):
    model = MathProblem
    fields = ['questions']
    template_name = 'puzzles/mathproblem_form.html'
    success_url = reverse_lazy('mathproblem_list')
    
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
    
    
class MathProblemDetailView(DetailView):
    model = MathProblem
    template_name = 'puzzles/mathproblem_detail.html'
    context_object_name = 'mathproblem'
    