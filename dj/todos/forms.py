from django.forms import ModelForm
from todos.models import Todo

class TodoForm(ModelForm):
	class Meta:
		model = Todo

		
