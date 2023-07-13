from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'User/signup.html', {"form": form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password1"] == form.cleaned_data["password2"]:
                try:
                    user = User.objects.create_user(
                        form.cleaned_data["username"], password=form.cleaned_data["password1"])
                    user.save()
                    messages.success(request, 'Registro exitoso. ¡Bienvenido!')
                    return redirect('signin')
                except IntegrityError:
                    form.add_error('username', 'El nombre de usuario ya existe.')
            else:
                form.add_error('password2', 'Las contraseñas no coinciden.')
        
        # Si llegamos aquí, significa que hay errores en el formulario
        messages.error(request, 'Ocurrió un error en el formulario.')
        return render(request, 'User/signup.html', {"form": form})

def signout(request):
    logout(request)
    return redirect('signin')




def signin(request):
    if request.method == 'GET':
        return render(request, 'User/signin.html', {"form": AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos. Por favor, intenta nuevamente.')
        else:
            messages.error(request, 'Ocurrió un error en el formulario.')
        
        return render(request, 'User/signin.html', {"form": form})




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
            return redirect('list_usua')
        else:
            data["form"] = formulario3
    return render(request, 'User/form_usuario.html', data)

#Editar usuario
def editar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)

    if request.method == 'POST':
        formulario = CustomUserChangeForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect('list_usua')
    else:
        formulario = CustomUserChangeForm(instance=usuario)

    return render(request, 'User/edit_usuario.html', {'form': formulario})

#Eliminar usuario
def eliminar_usuario(request, id):
    usuarios = get_object_or_404(User, id=id)
    usuarios.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_usua")


def buscar_usuarios(request):
    query = request.GET.get('q')
    usuarios = User.objects.filter(username__icontains=query) if query else User.objects.all()
    
    context = {
        'listado': usuarios
    }
    
    return render(request, 'User/list_usuario.html', context)