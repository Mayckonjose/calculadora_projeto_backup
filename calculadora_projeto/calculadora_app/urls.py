from django.urls import path
from .views import CalculadoraView, HistoricoView

app_name = 'calculadora_app'  # <- ESSENCIAL

urlpatterns = [
    path('', CalculadoraView.as_view(), name='calculadora'),
    path('historico/', HistoricoView.as_view(), name='historico'),
]
