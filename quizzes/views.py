from django.shortcuts import render

# Create your views here.
from .models import Quiz
from django.views.generic import ListView

class QuizListView(ListView):
    model = Quiz
    template_name='quizzes/main.html'


def quiz_view(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    context={
        'obj':quiz
    }
    return render(request,'quizzes/quiz.html',context)