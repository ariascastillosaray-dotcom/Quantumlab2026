def calcular_peso(masa, gravedad):
    peso = masa * gravedad
    return peso

masa = float(input("Ingrese la masa en kg: "))
gravedad = 9.81
resultado = calcular_peso(masa, gravedad)
print(resultado)
