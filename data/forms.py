from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('todo_job', 'todo_job_detail', 'category', 'is_finished',)  # 'user', 'created_date')

