from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        
        nome_maiusculo = self.nome.upper()
        
       
        if self.nacionalidade:
            return f"{nome_maiusculo} ({self.nacionalidade}) ({self.id})"
        else:
            return f"{nome_maiusculo} ({self.id})"
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"