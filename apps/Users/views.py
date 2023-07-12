from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'User/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'User/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
            
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('dashboard')

#-------- Usuarios -----------------------------------------------
#Listar usuarios
def list_usuarios(request):
    listado = User.objects.all();
    return render(request, 'User/list_usuario.html', {'listado':listado})

#Formulario de usuario
def form_usuario(request):

    data = {
        'form': UserCreationForm()

    }

    if request.method == 'POST':
        formulario3 = UserCreationForm (data=request.POST)
        if formulario3.is_valid():
            formulario3.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="list_usua")
        else:
            data["form"] = formulario3
    return render(request, 'User/form_usuario.html', data)

#Editar usuario
def editar_usuario(request, id):
    usuario= get_object_or_404(User, id=id)

    data = {
        'form': UserCreationForm(instance=usuario)
    }
    
    if request.method == 'POST':
        formulario = UserCreationForm (data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="list_usua")
        data["form"] = formulario
  

    return render (request, 'User/edit_usuario.html', data)

#Eliminar usuario
def eliminar_usuario(request, id):
    usuarios = get_object_or_404(User, id=id)
    usuarios.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_usua")
