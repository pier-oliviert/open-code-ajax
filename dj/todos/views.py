from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from todos.forms import TodoForm
from todos.models import Todo

def list(request):
	todos = Todo.objects.filter(done=False)
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
		
		if request.is_ajax():
			return render(request, 'todos/list.js', {'form': form}, content_type="text/javascript")
	else:
		form = TodoForm()

	return render(request, 'todos/list.html', {'todos': todos, 'form': form})

def done(request, pk):
    obj = get_object_or_404(Todo, pk=pk)

    obj.done = True
    obj.save()

    if request.is_ajax():
    	return render(request, 'todos/done.js', {'todo': obj}, content_type="text/javascript")
    else:
    	return redirect('/')
