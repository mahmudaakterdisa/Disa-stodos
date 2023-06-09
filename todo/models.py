from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.id}--{self.title}"
