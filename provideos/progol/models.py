from django.db import models

# Create your models here.
class tbl_usuarios(models.Model):
    nombre = models.CharField( max_length=50)
    idNomina = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return f"{self.idNomina}"
    
class tbl_videos(models.Model):
    nombreVideo = models.CharField( max_length=50)
    extVideo= models.CharField( max_length=10)
    idUsuario = models.ForeignKey(tbl_usuarios, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f"{self.idUsuario}"
   