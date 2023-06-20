from django.db import models

# Create your models here.
class Autor(models.Model):
    #representacion clave primaria
    id = models.AutoField(primary_key= True)
    nombre=models.CharField(max_length= 200, blank = False , null = False) # Este campo nunca se deje en blanco
    apellidos= models.CharField(max_length=200, blank=False, null= False)
    nacionalidad = models.CharField(max_length=100, blank=False, null =False)
    descripcion = models.TextField(blank=False, null = False)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now= True, auto_now_add= False)
    
    class Meta:
        verbose_name= 'autor'
        verbose_name_plural= 'autores'
        ordering=["apellidos"]
    def __str__(self):
        return self.apellidos
        
class libro(models.Model):

    id=models.AutoField(primary_key=True)
    titulo= models.CharField("titulo", max_length=255, blank= False,null=False)
    fecha=models.DateField("Fecha de publicacion", max_length=255,blank=False,null=False)
    #Este es una relación de uno a muchos
    #autor_id=models.OneToOneField(Autor, on_delete= models.CASCADE)
    # Para una relación de unos a muchos utilizamos a forein key
    #autor_id=models.ForeignKey(Autor, on_delete= models.CASCADE)
    # Cmo un libro puede tener varios autores 
    autor_id=models.ManyToManyField(Autor)  # no requiere la relación on_delete
    
    class Meta:
        verbose_name= 'Libro'
        verbose_name_plural= 'Libros'
        ordering=['titulo']
    def __str__(self):
        return self.titulo