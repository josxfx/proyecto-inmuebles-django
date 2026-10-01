from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InmuebleForm, RegistroForm, UsuarioForm
from .models import Inmueble, Usuario, Region, Comuna, SolicitudArriendo


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            user = form.save()

            Usuario.objects.create(
                user=user,
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                rut=form.cleaned_data['rut'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                correo_electronico=form.cleaned_data['correo_electronico'],
                tipo_usuario=form.cleaned_data['tipo_usuario']
            )

            return redirect('login')

    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

@login_required
def perfil(request):
    usuario = Usuario.objects.get(user=request.user)

    return render(request, 'perfil.html', {'usuario': usuario})

@login_required
def editar_perfil(request):
    usuario = Usuario.objects.get(user=request.user)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect('perfil')

    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def agregar_inmueble(request):

    usuario = Usuario.objects.get(user=request.user)

    if usuario.tipo_usuario != 'arrendador':
        return redirect('perfil')

    if request.method == 'POST':
        form = InmuebleForm(request.POST)

        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = usuario
            inmueble.save()

            return redirect('mis_inmuebles')

    else:
        form = InmuebleForm()

    return render(request, 'agregar_inmueble.html', {'form': form})

@login_required
def mis_inmuebles(request):

    usuario = Usuario.objects.get(user=request.user)

    if usuario.tipo_usuario != 'arrendador':
        return redirect('perfil')

    inmuebles = Inmueble.objects.filter(arrendador=usuario)

    return render(
        request,
        'mis_inmuebles.html',
        {'inmuebles': inmuebles}
    )

@login_required
def editar_inmueble(request, inmueble_id):

    usuario = Usuario.objects.get(user=request.user)

    if usuario.tipo_usuario != 'arrendador':
        return redirect('perfil')

    inmueble = Inmueble.objects.get(
        id=inmueble_id,
        arrendador=usuario
    )

    if request.method == 'POST':
        form = InmuebleForm(
            request.POST,
            instance=inmueble
        )

        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = usuario
            inmueble.save()

            return redirect('mis_inmuebles')

    else:
        form = InmuebleForm(instance=inmueble)

    return render(
        request,
        'editar_inmueble.html',
        {'form': form, 'inmueble': inmueble}
    )

@login_required
def eliminar_inmueble(request, inmueble_id):

    usuario = Usuario.objects.get(user=request.user)

    if usuario.tipo_usuario != 'arrendador':
        return redirect('perfil')

    inmueble = Inmueble.objects.get(
        id=inmueble_id,
        arrendador=usuario
    )

    if request.method == 'POST':
        inmueble.delete()
        return redirect('mis_inmuebles')

    return redirect('mis_inmuebles')

@login_required
def solicitar_arriendo(request, inmueble_id):

    usuario = Usuario.objects.get(user=request.user)

    if usuario.tipo_usuario != 'arrendatario':
        return redirect('oferta_inmuebles')

    inmueble = Inmueble.objects.get(id=inmueble_id)

    solicitud_existente = SolicitudArriendo.objects.filter(
        arrendatario=usuario,
        inmueble=inmueble,
        estado='pendiente'
    ).exists()

    if solicitud_existente:
        return redirect('mis_solicitudes')

    if request.method == 'POST':

        SolicitudArriendo.objects.create(
            arrendatario=usuario,
            inmueble=inmueble,
            estado='pendiente'
        )

        return redirect('mis_solicitudes')

    return render(
        request,
        'solicitar_arriendo.html',
        {'inmueble': inmueble}
    )

@login_required
def mis_solicitudes(request):

    usuario = Usuario.objects.get(user=request.user)

    if usuario.tipo_usuario != 'arrendatario':
        return redirect('perfil')

    solicitudes = SolicitudArriendo.objects.filter(
        arrendatario=usuario
    ).select_related(
        'inmueble',
        'inmueble__comuna',
        'inmueble__comuna__region'
    )

    return render(
        request,
        'mis_solicitudes.html',
        {'solicitudes': solicitudes}
    )

def oferta_inmuebles(request):

    inmuebles = Inmueble.objects.all()

    usuario = None

    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user=request.user)

    regiones = Region.objects.all().order_by('nombre')
    comunas = Comuna.objects.all().order_by('nombre')

    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')

    if region_id:
        inmuebles = inmuebles.filter(
            comuna__region_id=region_id
        )

    if comuna_id:
        inmuebles = inmuebles.filter(
            comuna_id=comuna_id
        )

    return render(
        request,
        'oferta_inmuebles.html',
        {
            'inmuebles': inmuebles,
            'regiones': regiones,
            'comunas': comunas,
            'region_seleccionada': region_id,
            'comuna_seleccionada': comuna_id,
            'usuario': usuario,
        }
    )
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def bienvenido(request):

    usuario = Usuario.objects.get(user=request.user)

    return render(
        request,
        'bienvenido.html',
        {'usuario': usuario}
    )

def logout_exitoso(request):
    return render(request, 'logout.html')


