from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField() #닐짜, 시간까지 저장하기 위해 DateTimeField로 due_date 선언

    def __str__(self):
        return self.title
        
from django.contrib import admin
admin.site.register(Todo)

