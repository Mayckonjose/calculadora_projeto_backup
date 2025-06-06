from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from decimal import Decimal
from .models import OperationHistory

class CalculadoraView(CreateView):
    model = OperationHistory
    template_name = 'calculadora_app/calculadora.html'
    fields = ['first_number', 'operation', 'second_number']
    success_url = reverse_lazy('calculadora_app:calculadora')  # corrigido

    def form_valid(self, form):
        instance = form.save(commit=False)
        n1 = instance.first_number
        n2 = instance.second_number
        op = instance.operation

        if op == '+':
            instance.result = n1 + n2
        elif op == '-':
            instance.result = n1 - n2
        elif op == '*':
            instance.result = n1 * n2
        elif op == '/' and n2 != 0:
            instance.result = n1 / n2
        else:
            form.add_error('second_number', 'Divisão por zero não é permitida')
            return self.form_invalid(form)

        return super().form_valid(form)

class HistoricoView(ListView):
    model = OperationHistory
    template_name = 'calculadora_app/historico.html'
    context_object_name = 'operacoes'
    paginate_by = 10
