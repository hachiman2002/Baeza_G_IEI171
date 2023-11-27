from django.db import models

# Create your models here.
class Socios(models.Model):
    nombreSocio = models.CharField(max_length=80, verbose_name="Nombre socio")
    fechaIncorporacion = models.DateField(verbose_name="Fecha incorporacion")
    anioNacimiento = models.DateField(verbose_name="Año nacimiento")
    telefono = models.CharField(max_length=12, verbose_name="Numero de telefono")#Aqui coloque charfield en vex de integer suponiendo que el usuario podria agregar el caracter (+)
    correoElectronico = models.EmailField("Corredo electronico")
    sexo = models.CharField(max_length=20, verbose_name="Sexo")
    estado = models.CharField(max_length=20, verbose_name="Estado")
    observacion = models.TextField(blank=True, null=True, verbose_name="Observacion")
    
    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"
        
    def __str__(self):
        return self.name