from django.views.generic import ListView, DetailView
from .models import Matéria, Assunto
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MateriaForm, AssuntoForm

def materia_new(request):
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            materia = form.save(commit=False)
            # Aqui você pode adicionar algum processamento adicional
            # antes de salvar o objeto Matéria, caso necessário
            materia.save()
            return redirect('materia_detail', pk=materia.pk)
    else:
        form = MateriaForm()
    return render(request, 'materia_form.html', {'form': form})

def materia_edit(request, pk):
    materia = get_object_or_404(Matéria, pk=pk)
    if request.method == "POST":
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            materia = form.save(commit=False)
            # Aqui você pode adicionar algum processamento adicional
            # antes de salvar o objeto Matéria, caso necessário
            materia.save()
            return redirect('materia_detail', pk=materia.pk)
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materia_form.html', {'form': form})

def materia_delete(request, pk):
    materia = get_object_or_404(Matéria, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('materia_list')
    return render(request, 'materia_confirm_delete.html', {'materia': materia})

def assunto_new(request):
    if request.method == "POST":
        form = AssuntoForm(request.POST)
        if form.is_valid():
            assunto = form.save(commit=False)
            # Aqui você pode adicionar algum processamento adicional
            # antes de salvar o objeto Assunto, caso necessário
            assunto.save()
            return redirect('assunto_detail', pk=assunto.pk)
    else:
        form = AssuntoForm()
    return render(request, 'assunto_form.html', {'form': form})

def assunto_edit(request, pk):
    assunto = get_object_or_404(Assunto, pk=pk)
    if request.method == "POST":
        form = AssuntoForm(request.POST, instance=assunto)
        if form.is_valid():
            assunto = form.save(commit=False)
            # Aqui você pode adicionar algum processamento adicional
            # antes de salvar o objeto Assunto, caso necessário
            assunto.save()
            return redirect('assunto_detail', pk=assunto.pk)
    else:
        form = AssuntoForm(instance=assunto)
    return render(request, 'assunto_form.html', {'form': form})

def assunto_delete(request, pk):
    assunto = get_object_or_404(Assunto, pk=pk)
    if request.method == 'POST':
        assunto.delete()
        return redirect('assunto_list')
    return render(request, 'assunto_confirm_delete.html', {'assunto': assunto})

class MateriaListView(ListView):
    queryset = Matéria.objects.all()
    context_object_name = 'materias'
    template_name = 'materia_list.html'


class MateriaDetailView(DetailView):
    model = Matéria

class AssuntoListView(ListView):
    model = Assunto

class AssuntoDetailView(DetailView):
    model = Assunto

