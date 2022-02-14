from django.db import models

class Quiz(models.Model):
    name=models.CharField(max_length=200)
    topic=models.CharField(max_length=200)
    number_of_questions=models.IntegerField()
    time=models.IntegerField(help_text="Imtahanin vaxti")
    required_score=models.IntegerField(help_text="Kecme bali")


    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

    


