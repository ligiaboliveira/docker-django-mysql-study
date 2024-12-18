from django.db import models

class Example(models.Model):
    # Defina os campos da tabela 'example'. Exemplo:
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Indica o nome da tabela no banco de dados
    class Meta:
        db_table = 'example'
    def __str__(self):
        return self.name
