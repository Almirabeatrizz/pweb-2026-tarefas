from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='posts/')
    texto = models.TextField()
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo