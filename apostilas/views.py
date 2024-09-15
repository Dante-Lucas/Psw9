from django.shortcuts import render, redirect
from .models import Apostila,ViewApostila
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def adicionar_apostilas(request):
    if request.method == 'GET':
        apostilas = Apostila.objects.filter(user=request.user)

        views_totais = ViewApostila.objects.filter(apostila__user=request.user).count()
        return render(request, 'apostilas/adicionar_apostilas.html', {'apostilas': apostilas})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo = request.FILES['arquivo']

        apostila = Apostila(user=request.user, titulo=titulo, arquivo=arquivo)
        apostila.save()

    
        messages.add_message(request, constants.SUCCESS, 'Apostila adicionada com sucesso.')
        return redirect('/apostilas/adicionar_apostilas/')

@login_required    
def apostila(request, id):
    apostila = Apostila.objects.get(id=id)
    views_unicas = ViewApostila.objects.filter(apostila=apostila).values('ip').distinct().count()
    views_totais = ViewApostila.objects.filter(apostila=apostila).count()

    
    view = ViewApostila(
        ip=request.META['REMOTE_ADDR'],
        apostila=apostila
    )
    view.save()
    return render(request, 'apostila.html', {'apostila': apostila, 'views_totais':views_totais, 'views_unicas': views_unicas})   