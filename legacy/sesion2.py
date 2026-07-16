gravedades = [9.81, 3.71, 1.62]
masa = float(input("Ingrese la masa en kg: "))
planeta = input("Ingrese el cuerpo celeste (Tierra, Marte, Luna): ")
if planeta == "Tierra":
    gravedad = gravedades[0]
elif planeta == "Marte":
    gravedad = gravedades[1]
elif planeta == "Luna":
    gravedad = gravedades[2]
peso = masa * gravedad
print ("Peso:", peso,  "N")


