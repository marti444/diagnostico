## Crea un programa que solicite al usuario ingresar un número del 1 al 7, representando cada
día de la semana (1 para lunes, 2 para martes, y así sucesivamente). Utiliza esta entrada para
calcular y mostrar el nombre correspondiente al día de la semana.
Pasos a seguir:
1. Entrada de Datos:
• Solicita al usuario ingresar un número del 1 al 7.
2. Cálculo del Día:
• Utiliza una estructura de control switch para determinar el nombre del día de la
semana basándote en el número ingresado por el usuario. Asigna el nombre del día
correspondiente a una variable.
3. Salida de Resultados:
• Imprime en la pantalla el nombre del día de la semana calculado

  def obtener_nombre_dia(numero):
    nombre_dia = ""
    if numero == 1:
        nombre_dia = "Lunes"
    elif numero == 2:
        nombre_dia = "Martes"
    elif numero == 3:
        nombre_dia = "Miércoles"
    elif numero == 4:
        nombre_dia = "Jueves"
    elif numero == 5:
        nombre_dia = "Viernes"
    elif numero == 6:
        nombre_dia = "Sábado"
    elif numero == 7:
        nombre_dia = "Domingo"
    else:
        nombre_dia = "Número inválido"
    return nombre_dia

numero_dia = int(input("Ingrese un número del 1 al 7 para representar un día de la semana: "))
nombre_dia = obtener_nombre_dia(numero_dia)
print("El día correspondiente al número ingresado es:", nombre_dia)
