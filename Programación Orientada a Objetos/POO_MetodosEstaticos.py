class UtilidadesFinancieras:
    @staticmethod
    def calcular_margen_beneficio(ingresos, costos):
        margen = (ingresos - costos) / ingresos * 100
        return margen

# Ejemplo de uso
ingresos = 10000
costos = 7000

margen = UtilidadesFinancieras.calcular_margen_beneficio(ingresos, costos)
print(f"El margen de beneficio es: {margen}%")