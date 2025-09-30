class UnitConverter:
    def __init__(self, value):
        self.value = value

    # ---------- TEMPERATURA ----------
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    # ---------- MOEDAS (exemplo fictício) ----------
    @classmethod
    def from_real(cls, reais):
        """Cria um conversor a partir de reais (BRL)"""
        return cls(reais)

    def to_dolar(self):
        """Converte reais para dólares (cotação fictícia: 1 USD = 5 BRL)"""
        return round(self.value / 5, 2)

    def to_euro(self):
        """Converte reais para euros (cotação fictícia: 1 EUR = 6 BRL)"""
        return round(self.value / 6, 2)


if __name__ == "__main__":
    print("=== Conversor de Unidades ===")

    # Exemplo de uso de staticmethod
    c = 30
    print(f"{c}°C = {UnitConverter.celsius_to_fahrenheit(c)}°F")
    print(f"{c}°C = {UnitConverter.celsius_to_kelvin(c)}K")

    # Exemplo de uso de classmethod
    valor = 100
    conversor = UnitConverter.from_real(valor)
    print(f"R$ {valor} = $ {conversor.to_dolar()} dólares")
    print(f"R$ {valor} = € {conversor.to_euro()} euros")
