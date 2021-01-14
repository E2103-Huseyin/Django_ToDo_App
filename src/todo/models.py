from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-create_date',)
        
        
    def __str__(self):
        return self.title
    