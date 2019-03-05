from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Credential
from . forms import CredentialForm

def index(request):
    users = Credential.objects.all()
    context = {
        'users': users
    }
    return render(request, 'crud/index.html', context)


def create(request):
    if request.method == 'POST':
        form = CredentialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('crud:index')
            # return render(request, 'crud/index.html', context)
    else:
        form = CredentialForm
        context = {
            'form': form
        }
        return render(request, 'crud/create.html', context)


def detail(request, id):
    user = get_object_or_404(Credential, pk=id)
    context = {
        'user': user
    }
    return render(request, 'crud/detail.html', context)


def update(request, id):
    user = Credential.objects.get(pk=id)

    if request.method == 'POST':
        form = CredentialForm(request.POST, instance=user)

        if form.is_valid():
            form.save(commit=False)

            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            user.save(update_fields=['name', 'username', 'email'])
            return redirect('crud:index')

    elif request.method == 'GET':
        form = CredentialForm()
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'crud/update.html', context)


def delete(request, id):
    user = Credential.objects.get(pk=id)
    user.delete()
    return redirect('crud:index')
