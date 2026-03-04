from django.db import models
from django.contrib.auth.models import User


class Materia(models.Model):
    nome = models.CharField(max_length=25)
    imagem = models.FileField(upload_to='materias/', blank=True, null=True)
    cor = models.CharField(max_length=10, default="#C8762B")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materias')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'

    def __str__(self):
        return f"{self.nome}"