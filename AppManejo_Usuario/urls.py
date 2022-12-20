from django.urls import path
from AppManejo_Usuario.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ("", inicio, name = "inicio"),
    path ("registro/", registro_usuario, name = "registro_usuario"),
    path ("ingreso/", Pagina_de_ingreso, name = "Pagina_de_ingreso" ),
    path("desconectarse/", desconectarse, name = "desconectarse" ),
    path('editarusuario/', editarUsuario, name='Editar_Usuario' ),
    path('eliminarusuario/<id>', eliminarUsuario,name="Eliminar_Usuario"),
    path('usuariosregitrados', usuariosRegistrados, name="Usuarios_Registrados"),
]