from django.db import models

# Create your models here.

class Base(models.Model):
  criado = models.DateField('Data de criação', auto_now_add=True)
  modificado = models.DateField('Data de atualização', auto_now=True)
  ativo = models.BooleanField('Ativo?', default=True)

  class Meta:
    abstract = True

class Servico(Base):
  ICONE_CHOICES = (
    ('lni-cog', 'Engrenagem'),
    ('lni-stats-up', 'Gráficos'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
  )

  servico = models.CharField('Serviço', max_length=100)
  descricao = models.CharField('Descrição', max_length=200)
  icone = models.CharField('Icone', max_length=15, choices=ICONE_CHOICES)

  class Meta:
    verbose_name = 'Serviço'
    verbose_name_plural = 'Serviços'

  def __str__(self) -> str:
    return self.servico