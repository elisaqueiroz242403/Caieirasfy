from django.db import models

# Create your models here.

class Musica(models.Model):
    nome_musica = models.CharField(
        max_length=50,
        verbose_name='Nome da Musica'
    )
    nome_artista = models.CharField(
        max_length=50,
        verbose_name='Artista',
    )
    genero_musica = models.CharField(
        max_length=50,
        verbose_name='Genero',
    )
    link_musica = models.CharField(
        max_length=50,
        verbose_name='Link'
    )
    
    
    def __str__(self):
        return self.nome_musica + '' + self.nome_artista




