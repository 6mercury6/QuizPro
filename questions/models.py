from django.db import models

# Create your models here.
from pickle import FALSE
from tkinter import CASCADE
from django.db import models

from quizzes.models import Quiz
# Create your models here.
class Questions(models.Model):
    text=models.CharField(max_length=200)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)


    def __str__(self) :
        return str(self.text)
    

    def get_answers(self):
        return self.answer_set.all()

class Answers(models.Model):
    text=models.TextField(max_length=200)
    correct=models.BooleanField(default=False)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"sual:{self.question.text},cavab:{self.text},duzgun:{self.correct}"
