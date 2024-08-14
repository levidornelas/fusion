from django.db import models
from stdimage.models import StdImageField
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
    ('lni-steam', 'Jogos'),
    ('lni-python', 'Python')
  )

  servico = models.CharField('Serviço', max_length=100)
  descricao = models.CharField('Descrição', max_length=200)
  icone = models.CharField('Icone', max_length=15, choices=ICONE_CHOICES)

  class Meta:
    verbose_name = 'Serviço'
    verbose_name_plural = 'Serviços'

  def __str__(self) -> str:
    return self.servico
  
class Cargo(Base):
  cargo = models.CharField('Cargo', max_length=100)

  def __str__(self) -> str:
    return self.cargo
  
class Funcionario(Base):
  nome = models.CharField('Nome', max_length=100)
  cargo = models.ForeignKey(Cargo, verbose_name='Cargo', on_delete=models.CASCADE) #Chamando a chave estrangeira de outra tabela 'cargo' para inserir na tabela de funcionários
  bio = models.TextField('bio', max_length=200)
  imagem = StdImageField('Imagem', upload_to='Equipe', variations={'thumb': {'width': 400, 'height': 400, 'crop': True}}) # 'Upload_to' -> Indica o diretório de inserção das imagens em 'media'
  facebook = models.CharField('Facebook', max_length=100, default='#')
  twitter = models.CharField('Twitter', max_length=100, default='#')
  instagram = models.CharField('Instagram', max_length=100, default='#')

  class Meta:
    verbose_name = 'Funcionário'
    verbose_name_plural = 'Funcionários'

  def __str__(self) -> str:
    return self.nome
  
class Preco(Base):
  ICONE_CHOICES = (
    ('lni-package', 'Padrão'),
    ('lni-drop', 'Plus'),
    ('lni-star', 'Pro')
  )

  preco = models.IntegerField('Preços')
  titulo = models.CharField('Título', max_length=50)
  descricao = models.TextField('Descrição', max_length=200)
  icone = models.CharField('Icone', max_length=15, choices=ICONE_CHOICES)

  class Meta:
    verbose_name = 'Preço'
    verbose_name_plural = 'Preços'

  def __str__(self) -> str:
    return self.titulo

class Testemunho(models.Model):
    STARS = (
        ('★☆☆☆☆', '1 estrela'),
        ('★★☆☆☆', '2 estrelas'),
        ('★★★☆☆', '3 estrelas'),
        ('★★★★☆', '4 estrelas'),
        ('★★★★★', '5 estrelas'),
    )

    nome = models.CharField('Nome', max_length=100)
    ocupacao = models.CharField('Ocupação', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('Imagem', upload_to='Clientes', variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})
    estrelas = models.CharField('Estrelas', max_length=100, choices=STARS)

    def __str__(self):    
        return self.nome


