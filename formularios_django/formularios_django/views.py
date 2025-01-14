from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm


def form(request):
    comment_form = CommentForm({'name': 'Raúl', 'url':'https://google.es', 'comment': 'Comentario'})
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    if request.method != 'POST':
        return HttpResponse("Método no permitido")
    
    return HttpResponse(request.POST['name'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Válido")
        else:
            return render(request, 'widget.html', {'form': form})