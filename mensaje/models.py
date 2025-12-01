from django.db import models

class Saludo(models.Model):
    TIPO_CHOICES = [
        ('feliz', 'Feliz'),
        ('triste', 'Triste'),
    ]
    texto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='feliz', blank=True)

    def __str__(self):
        return self.texto