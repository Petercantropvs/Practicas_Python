from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
init_time = datetime.now()
# Contador de aciertos:
aciertos = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    if operator == '/':
        while number_2 == 0:
            number_2 = randrange(10)

    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    result = input("resultado: ")

    # Primer forma de resolverlo:
    if (operator == '+'):
        rta = number_1 + number_2
        if (rta == int(result)):
            print('Muy bien! Respuesta correcta ;)')
            aciertos = aciertos + 1
        else:
            print('Respuesta incorrecta! La respuesta era ', rta)

    elif (operator == '-'):
        rta = number_1 - number_2
        if (rta == int(result)):
            print('Muy bien! Respuesta correcta ;)')
            aciertos = aciertos + 1
        else:
            print('Respuesta incorrecta! La respuesta era ', rta)

    elif (operator == '*'):
        rta = number_1 * number_2
        if (rta == int(result)):
            print('Muy bien! Respuesta correcta ;)')
            aciertos = aciertos + 1
        else:
            print('Respuesta incorrecta! La respuesta era ', rta)

    elif (operator == '/'):
        rta = number_1 / number_2
        if (rta == float(result)):
            print('Muy bien! Respuesta correcta ;)')
            aciertos = aciertos + 1
        else:
            print('Respuesta incorrecta! La respuesta era ', rta)


# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
total_time = end_time - init_time
print(f"\n Tardaste {total_time.seconds} segundos.")

# Mostramos la cantidad de aciertos y errores:
print('tuviste ', aciertos, 'aciertos y ', times-aciertos, 'errores.')