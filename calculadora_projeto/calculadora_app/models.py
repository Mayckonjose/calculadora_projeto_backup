from django.db import models

class OperationHistory(models.Model):
    OPERATION_CHOICES = [
        ('+', 'Adição'),
        ('-', 'Subtração'),
        ('*', 'Multiplicação'),
        ('/', 'Divisão'),
    ]
    
    first_number = models.DecimalField(max_digits=10, decimal_places=2)
    second_number = models.DecimalField(max_digits=10, decimal_places=2)
    operation = models.CharField(max_length=1, choices=OPERATION_CHOICES)
    result = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Histórico de Operação'
        verbose_name_plural = 'Histórico de Operações'

    def __str__(self):
        return f'{self.first_number} {self.operation} {self.second_number} = {self.result}'