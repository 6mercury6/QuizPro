from tkinter import CASCADE
from django.db import models

from django.contrib.auth.models import User
from quizzes.models import Quiz

class Result(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.FloatField()

    def __str__(self):
        return str(self.pk)

