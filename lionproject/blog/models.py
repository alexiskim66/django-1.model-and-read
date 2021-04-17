from django.db import models

# Create your models here.
class Blog(models.Model):
    subject = models.CharField(max_length=100, default="")
    author = models.CharField(max_length=100)
    publishing_date = models.DateTimeField()
    contents = models.TextField()

    def __str__(self):
        return self.subject

    def summary(self):
        return self.contents[:100]
