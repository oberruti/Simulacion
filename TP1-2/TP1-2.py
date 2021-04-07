from random import randint
#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

min_ruleta = 0
max_ruleta = 36
numeros_ruleta = 37.0
verde = 0
max_tiradas = 10

def ini_ruleta():
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    pares = []
    impares = []
    docenas = [[],[],[]]
    columnas = [[],[],[]]
    for i in range(1,int(numeros_ruleta)):
        if i%2 == 0:
            pares.append(i)
        if i%2 != 0:
            impares.append(i)
        if i<=12:
            docenas[0].append(i)
        elif i>12 and i<= 24:
            docenas[1].append(i)
        elif i>24:
            docenas[2].append(i)
    col_in = 1
    while col_in <= 34:
        columnas[0].append(col_in)
        col_in = col_in+3
    col_in = 2
    while col_in <= 35:
        columnas[1].append(col_in)
        col_in = col_in+3
    col_in = 3
    while col_in <= 36:
        columnas[2].append(col_in)
        col_in = col_in+3
    ruleta = {
        'rojos': rojos, 
        'negros': negros,
        'pares': pares,
        'impares': impares,
        'docenas': docenas,
        'columnas': columnas,
    }
    return ruleta


def girar_ruleta():
    vueltas = randint(5, 150)
    for i in range(0,vueltas):
        resultado = randint(min_ruleta, max_ruleta)
    return resultado

def apuesta_deseada(fondos):
    apuesta_validado = -1
    while (apuesta_validado < 0 or apuesta_validado > fondos):
        apuesta_deseada = float(input("Ingresa tu apuesta: $"))
        if (apuesta_deseada > 0 and apuesta_deseada <= fondos):
            apuesta_validado = apuesta_deseada
    return apuesta_deseada

def get_resultado_deseado():
    resultado_deseado = []
    resultado_deseado_validado = -1
    while (resultado_deseado_validado < 0 or resultado_deseado_validado > max_ruleta):
        res_des = int(input("Resultado deseado: "))
        resultado_deseado.append(res_des)
        if (resultado_deseado[0] > 0 and resultado_deseado[0] <= max_ruleta):
            resultado_deseado_validado = resultado_deseado[0]
    return resultado_deseado


def apuesta_simple(fondos, apuesta_actual, resultado_deseado, multiplicador):
    print('Resultado/s deseado/s: ',resultado_deseado)
    print('Apuesta simple: ')
    resultados_as = []
    capital_inicial = fondos
    cont_giros = 0
    while fondos > 0 and cont_giros < max_tiradas:
        resultado_obtenido = girar_ruleta()
        print('Resultado: ', resultado_obtenido)
        if (resultado_obtenido in resultado_deseado):
            fondos+= apuesta_actual*multiplicador
            print('Ganaste! Capital actual: ', fondos)
        elif (resultado_obtenido not in resultado_deseado):
            fondos-= apuesta_actual
            print('Perdiste! Capital actual: ', fondos)
        resultados_as.append(resultado_obtenido)
        cont_giros = cont_giros + 1;
        # print('cantidad de giros', cont_giros)
    print(resultados_as)

def martin_gala(fondos, apuesta_actual, resultado_deseado, multiplicador):
    print('Resultado/s deseado/s: ',resultado_deseado)
    print('Martingala: ')
    resultados_mg = []
    capital_inicial = fondos
    apuesta_base = apuesta_actual
    cont_giros = 0
    while fondos > 0 and cont_giros < max_tiradas:
        fondos = fondos - apuesta_actual
        resultado_obtenido = girar_ruleta()
        print('Resultado: ', resultado_obtenido)
        if (resultado_obtenido in resultado_deseado):
            premio = apuesta_actual*multiplicador
            fondos = fondos + premio
            print('Ganaste, volves a la apuesta inicial! Capital actual: $', fondos)
            apuesta_actual = apuesta_base
        elif (resultado_obtenido not in resultado_deseado):
            apuesta_actual = apuesta_actual * 2
            print('Perdiste, duplicas! Capital actual: $', fondos)
            if (fondos <= apuesta_base * 2):
                print('No quedan fondos suficientes para seguir haciendo MartinGala')
                resultados_mg.append(resultado_obtenido)
                break
        resultados_mg.append(resultado_obtenido)
        cont_giros = cont_giros + 1;
        # print('cantidad de giros', cont_giros)
    print(resultados_mg)


# En la fibonacci, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(fondos, apuesta_base, resultado_deseado, multiplicador):
    print('Resultado/s deseado/s: ',resultado_deseado)
    print('Fibonacci: ')
    resultados_fibo = []
    secuencia_fibo = []
    apuesta_actual = apuesta_base
    print('Apuesta inicial: ', apuesta_actual)
    fib_actual = 1
    n = 0
    cont_giros = 0
    for i in range(1, max_tiradas):
        secuencia_fibo.append(fib(i))
    while fondos > apuesta_base and cont_giros < max_tiradas-1:
        print('Fondo antes de la apuesta: $', fondos)
        fondos = fondos - apuesta_actual
        resultado_obtenido = girar_ruleta()
        print('Resultado de la tirada: ', resultado_obtenido)
        print('Apuesta actual: ', apuesta_actual)
        print('Fibonacci actual: ', fib_actual)
        print('Fondo despues de la apuesta: $', fondos)
        if (resultado_obtenido in resultado_deseado):
            premio = apuesta_actual*multiplicador
            fondos = fondos + premio
            print('Ganaste: $', premio)
            print('Volves a la apuesta anterior! Capital actual: $', fondos)
            fib_actual = fib_actual - 1
            apuesta_actual = apuesta_base * secuencia_fibo[fib_actual-1]
        elif (resultado_obtenido not in resultado_deseado):
            fib_actual = fib_actual + 1
            apuesta_actual = apuesta_base * secuencia_fibo[fib_actual-1]
            print('Perdiste! Capital actual: $', fondos)
            if (fondos < apuesta_base):
                print('No quedan fondos suficientes para seguir haciendo Fibonacci')
                resultados_fibo.append(resultado_obtenido)
                break
        resultados_fibo.append(resultado_obtenido)
        cont_giros += 1
    print(resultados_fibo)


def start_ruleta():
    # ingreso fondos y valido, si es 0 el capital tiene que ser infinito
    fondos = float(input("Ingrese el capital total (0, si desea capital infinito): $"))
    while fondos < 0:
        fondos = float(input("Ingrese el capital total: "))
    if fondos == 0:
        fondos = 99999999999

    # ingreso y valido cantidad a apostar.
    apuesta_actual = apuesta_deseada(fondos)
    
    # ingreso estrategia de apuesta
    estrategia_verificado = -1
    while(estrategia_verificado<0 or estrategia_verificado>5):
        estrategia_seleccionada = int(input(
        '''
        ¿Que estrategia desea utilizar?:
        1) Rojo/Negro [Premio: 1x1]
        2) Par/Impar [Premio: 1x1] 
        3) Docena [Premio: 2x1]
        4) Columna [Premio: 2x1]
        5) Pleno [Premio: 35x1]
        '''
        ))
        if estrategia_seleccionada > 0 and estrategia_seleccionada < 6:
            estrategia_verificado = estrategia_seleccionada

    print('Usted apostará $',apuesta_actual)
    if estrategia_seleccionada == 1:
        resultado_deseado = ruleta.get('rojos')
        apuesta_simple(fondos, apuesta_actual, resultado_deseado, 2)
        martin_gala(fondos, apuesta_actual, resultado_deseado, 2)
        #Fibonacci va solo en apuestas externas: Par/impar, rojo/negro, 1/18, 19/36
        fibonacci(fondos, apuesta_actual, resultado_deseado, 2)
    
    elif estrategia_seleccionada == 2:
        resultado_deseado = ruleta.get('pares')
        apuesta_simple(fondos, apuesta_actual, resultado_deseado, 2)
        martin_gala(fondos, apuesta_actual, resultado_deseado, 2)
        #Fibonacci va solo en apuestas externas: Par/impar, rojo/negro, 1/18, 19/36
        fibonacci(fondos, apuesta_actual, resultado_deseado, 2)
    
    elif estrategia_seleccionada == 3:
        resultado_deseado = ruleta.get('docenas')[0]
        apuesta_simple(fondos, apuesta_actual, resultado_deseado, 3)
        martin_gala(fondos, apuesta_actual, resultado_deseado, 3)
        fibonacci(fondos, apuesta_actual, resultado_deseado, 3)

    elif estrategia_seleccionada == 4:
        resultado_deseado = ruleta.get('columnas')[0]
        apuesta_simple(fondos, apuesta_actual, resultado_deseado, 3)
        martin_gala(fondos, apuesta_actual, resultado_deseado, 3)
        fibonacci(fondos, apuesta_actual, resultado_deseado, 3)
    
    elif estrategia_seleccionada == 5:
        resultado_deseado = get_resultado_deseado()
        apuesta_simple(fondos, apuesta_actual, resultado_deseado, 35)
        martin_gala(fondos, apuesta_actual, resultado_deseado, 35)
        fibonacci(fondos, apuesta_actual, resultado_deseado, 3)

def main():
    # creo la ruleta como variable global y la inicializo
    global ruleta
    ruleta = ini_ruleta()
    # inicio el juego
    start_ruleta()

if __name__ == "__main__":
    main()