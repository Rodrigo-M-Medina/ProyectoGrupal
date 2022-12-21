from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from AppManejo_Usuario.forms import CrearUsuario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


def inicio(request):
    return render (request, "Inicio.html")

#--- Pagina de registro ---#

def registro_usuario(request):
    if request.method=="POST":
        form=CrearUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "Inicio.html")
    else:
        form = CrearUsuario()
    return render(request, 'registro_usuario.html',{"form":form})

#--- Login ---#

def Pagina_de_ingreso(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombreusuario = form.cleaned_data.get("username")
            claveusuario = form.cleaned_data.get("password")
            usuario = authenticate (username=nombreusuario, password=claveusuario)
            if usuario is not None:
                login(request, usuario)
                return render (request, "Inicio.html")
            else:
                return render (request, "Pagina_de_ingreso.html", {"form":form})
        else:
            return render (request, "Pagina_de_ingreso.html",{"form":form})
    else:
        form=AuthenticationForm()
    
    return render (request, "Pagina_de_ingreso.html",{"form":form})

#--- Logout ---#

def desconectarse(request):
    logout(request)
    return render(request, "Inicio.html", {"mensaje": "Desconectado existosamente"})

#------------- editar usuario -------------

def editarUsuario(request):

    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():

            info = formulario.cleaned_data
            usuario.username = info['username']
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']

            usuario.save()
            return render(request, "Inicio.html")
        else:
            return render(request, "editar_perfil.html", {"Formulario": formulario, "usuario": usuario, "mensaje": "error al editar el perfil"})
    else:
        formulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "editar_perfil.html", {"Formulario": formulario, "usuario": usuario})

#----------- borrar usuario -----------------

def eliminarUsuario(request, pk):
    usuario = User.objects.filter(id=pk)
    usuario.delete()
    usuarios=User.objects.all()
    return usuariosRegistrados(request)

#------------ mostrar usuarios --------------

def usuariosRegistrados(request):
    usuarios = User.objects.all()
    return render(request, "usuarios_registrados.html", {"usuarios":usuarios} )


#------------- eliminar usuarios ---------

'''    class EliminarUsuarios(DeleteView):
    model = User
    success_url = reverse_lazy ("inicio")'''





