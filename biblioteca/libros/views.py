from django.shortcuts import render,redirect
from .forms import AutorForm
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def Home(request):
    return render(request,'libros/index.html')

def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if (autor_form.is_valid()):
            autor_form.save()
            return redirect('index')
    else:
        autor_form= AutorForm()
    return render(request,'libros/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores=Autor.objects.filter(estado=True)
    return render(request,'libros/listar_autor.html',{'autores':autores})

def editarAutor(request,id):
    autor_form=None
    error=None
    try:
        autor=Autor.objects.get(id = id)
        if request.method=='GET':
            autor_form=AutorForm(instance=autor)
        else:
            autor_form=AutorForm(request.POST,instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')
       
    except ObjectDoesNotExist as e:
        error = e 
    
    return render(request,'libros/crear_autor.html',{'autor_form':autor_form, 'error':error})
                
def eliminarAutor(request,id):
    autor=Autor.objects.get(id=id)
    if request.method== 'POST':
        
        #autor.delete() eliminación base de datos
        # Eliminación logica
        autor.estado=False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request,'libros/eliminar_autor.html',{'autor':autor})