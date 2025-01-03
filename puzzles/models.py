from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MathProblem(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    question = models.TextField()
    solution = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return self.question