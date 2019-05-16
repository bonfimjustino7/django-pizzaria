from django.db import models 

# Create your models here.

class Cliente(models.Model):
    origem = models.CharField(max_length=10)
    def __str__(self):
        return self.origem
class Prato(models.Model):
    TIPO = (
        ('PF', 'PF'),
        ('Quentinha', 'Quentinha'),
        ('Comercial', 'Comercial'),
        ('Suco', 'Suco'),
        ('Refrigerante', 'Refrigerante'),
        ('Serveja', 'Serveja'),

    )
    tipo = models.CharField(max_length=50, choices=TIPO)
    valor = models.DecimalField(null=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.tipo

class Pedido(models.Model):
    CARNE = (
        ('Boi', 'Boi'),
        ('Frango', 'Frango'),
        ('Porco', 'Porco'),
        ('Picadinho', 'Picadinho'), 
        ('Linguiça', 'Linguiça')
    )
    origem = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido =  models.DateTimeField(auto_now=True)
    quantidade = models.IntegerField()
    prato = models.ManyToManyField(Prato)
    descricao = models.TextField(max_length=200, null=True)
    carne_opcao_1 = models.CharField(max_length=50, null=True, choices=CARNE)
    carne_opcao_2 = models.CharField(max_length=50, null=True, choices=CARNE)
    total = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    
    def __str__(self):
        return str(self.origem)
        
    def calcular_prato(self):
        for p in self.prato.filter(pedido=self.pk):
            self.total = (self.total + p.valor) * self.quantidade
        self.save()

    def zerar(self):
        self.total = 0
        self.save()
    