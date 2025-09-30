#  Conversor de Unidades

Um projeto simples em **Python** para demonstrar o uso de **@staticmethod** e **@classmethod** em classes.  
Ele realiza conversões de **temperatura** e **moedas** (com valores fictícios).

## Funcionalidades
- 🌡️ Conversões de temperatura:
  - Celsius → Fahrenheit
  - Fahrenheit → Celsius
  - Celsius → Kelvin
- 💱 Conversões de moedas:
  - Reais (BRL) → Dólares (USD)
  - Reais (BRL) → Euros (EUR)

## Exemplos de Uso
```python
from converter import UnitConverter

# Usando staticmethod
print(UnitConverter.celsius_to_fahrenheit(30))  # 86.0

# Usando classmethod
conversor = UnitConverter.from_real(100)
print(conversor.to_dolar())  # 20.0
print(conversor.to_euro())   # 16.67
