from typing import Any
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Funcionario, Servico, Preco, Testemunho
from .forms import ContatoForm
from django.contrib import messages
# Create your views here.

class IndexView(TemplateView, FormView):
  template_name = 'index.html'
  form_class = ContatoForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super(IndexView, self).get_context_data(**kwargs) #Iniciando 'context' como o chamador de dados dos models, para ser exibido nos templates

    context['servicos'] = Servico.objects.all()
    context['funcionarios'] = Funcionario.objects.all()
    context['precos'] = Preco.objects.all()
    context['testemunhos'] = Testemunho.objects.all()

    return context
  
  def form_valid(self, form, **kwargs):
    form.send_email()
    messages.success(self.request, 'E-mail enviado com sucesso!')
    return super(IndexView, self).form_valid(form, **kwargs)
  
  def form_invalid(self, form, **kwargs):
    messages.error(self.request, 'Erro ao enviar o e-mail')
    return super(IndexView, self).form_invalid(form, **kwargs)