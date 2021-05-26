from django.db import models



class Cliente(models.Model):
    Nombre=models.CharField('Nombre', max_length=15, help_text="Escriba su nombre")
    Email=models.EmailField()
    Password=models.CharField(max_length=30)
    titulo=models.CharField(max_length=20)
    fecha=models.DateField()


