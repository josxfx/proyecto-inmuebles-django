from django.urls import path
from django.contrib.auth import views as auth_views
from .views import mis_solicitudes, perfil, registro, inicio, bienvenido, logout_exitoso, editar_perfil, agregar_inmueble, mis_inmuebles, editar_inmueble, eliminar_inmueble, oferta_inmuebles, solicitar_arriendo

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', registro, name='register'),
    path('logout-exitoso/', logout_exitoso, name='logout_exitoso'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('inmuebles/agregar/', agregar_inmueble, name='agregar_inmueble'),
    path('mis-inmuebles/', mis_inmuebles, name='mis_inmuebles'),
    path('inmuebles/editar/<int:inmueble_id>/', editar_inmueble, name='editar_inmueble'),
    path('inmuebles/eliminar/<int:inmueble_id>/', eliminar_inmueble, name='eliminar_inmueble'),
    path('oferta-inmuebles/', oferta_inmuebles, name='oferta_inmuebles'),
    path('solicitar-arriendo/<int:inmueble_id>/', solicitar_arriendo, name='solicitar_arriendo'),
    path('mis-solicitudes/', mis_solicitudes, name='mis_solicitudes'),
]