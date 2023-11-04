from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from .models import tbl_usuarios ,tbl_videos
from .forms import UserForm ,VideoForm ,FormVideos
from django.contrib import messages


# Create your views here.
def progol(request):
    template = loader.get_template('editar_usuario.html')
    return HttpResponse(template.render())

def usuarios(request):
    usuarios = tbl_usuarios.objects.all().order_by('idNomina')
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def saveUser(request):
    nombre = request.POST.get('nombre', '')  
    id_nomina = request.POST.get('idNomina', '')
    #validad que no este vacio
    if not nombre or not id_nomina:  # Comprobar si alguno de los campos está vacío o nulo
        # Realizar alguna acción si los campos están vacíos, por ejemplo, mostrar un mensaje de error
        # Aquí puedes redirigir de nuevo al formulario o realizar otra acción apropiada
        messages.error(request, 'Ocurrió un error al enviar el formulario, campos en blanco.')
        return redirect('/usuarios/')
    
    inuser =  tbl_usuarios(nombre = request.POST['nombre'],idNomina = request.POST['idNomina'])
    inuser.save()
    return redirect('/usuarios/')

def deletUser(request,id):
    deleteusers = tbl_usuarios.objects.get(idNomina=id)
    print(id)
    deleteusers.delete()
    return redirect('/usuarios/')


def subirVideo(request,id):
    usuario_seleccionado = id
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid() and request.POST:
              form.save()
        return redirect('/usuarios/')
    else:
        form= VideoForm()
    return render(request, 'editar_video.html', {'form': form, 'idUsuario': usuario_seleccionado})

def listarVideos(request,id):
    listadoVideos = tbl_videos.objects.all().filter(idUsuario=id)
    ##print(listadoVideos)
    return render(request, 'videos.html', {'videos': listadoVideos})
    #return redirect('/usuarios/')
    
def editVideo(request,id):
    editVideo = tbl_videos.objects.get(id=id)
    forms = FormVideos(request.POST or None, instance=editVideo)
    if forms.is_valid() and request.POST:
        urlVideo ='/listarVideos/' + str(editVideo.idUsuario)
        print(urlVideo)
        forms.save()
        return redirect(urlVideo)
    return render(request, 'editarVideo.html', {'forms': forms, 'idUsuario': editVideo.idUsuario})

def editUser(request,id):
    editUsers = tbl_usuarios.objects.get(idNomina=id)
    forms = UserForm(request.POST or None, instance=editUsers)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/usuarios/')
    return render(request, 'editar_usuario.html', {'forms': forms})
#{"page_title": u"Consultar Ordenes", "c_orden": c_orden, 'perfil_usuario':perfil.nombre})