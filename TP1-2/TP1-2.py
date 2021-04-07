from random import randint
#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

min_ruleta = 0
max_ruleta = 36
numeros_ruleta = 37.0
verde = 0
max_tiradas = 1500
estrategia_multiplicador = {
    'rojos': 2, 
    'pares': 2,
    'docenas': 3,
    'columnas': 3,
    'pleno': 35,
}

def get_pares(pares, i):
    if i%2 == 0:
        pares.append(i)
    return pares

def get_impares(impares, i):
    if i%2 != 0:
        impares.append(i)
    return impares

def get_docenas(docenas, i):
    if i<=12:
        docenas[0].append(i)
    elif i>12 and i<= 24:
        docenas[1].append(i)
    elif i>24:
        docenas[2].append(i)
    return docenas

def get_columnas(columnas):
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
    return columnas

def ini_ruleta():
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    pares = []
    impares = []
    docenas = [[],[],[]]
    columnas = [[],[],[]]
    columnas = get_columnas(columnas)
    for i in range(1,int(numeros_ruleta)):
        pares = get_pares(pares, i)
        impares = get_impares(impares, i)
        docenas = get_docenas(docenas, i)
    valores_ruleta = {
        'rojos': rojos, 
        'negros': negros,
        'pares': pares,
        'impares': impares,
        'docenas': docenas,
        'columnas': columnas,
    }
    return valores_ruleta


def girar_ruleta():
    tiros = randint(5, 150)
    for i in range(0,tiros):
        resultado = randint(min_ruleta, max_ruleta)
    return resultado

def get_apuesta_deseada(fondos):
    apuesta_validada = -1
    while (apuesta_validada < 0 or apuesta_validada > fondos):
        apuesta_deseada = float(input("Ingresa tu apuesta: $"))
        if (apuesta_deseada > 0 and apuesta_deseada <= fondos):
            apuesta_validada = apuesta_deseada
    return apuesta_deseada

def get_lista_resultados_deseados():
    resultados_deseados = []
    resultados_deseados_validado = -1
    while (resultados_deseados_validado < 0 or resultados_deseados_validado > max_ruleta):
        res_des = int(input("Resultado deseado: "))
        resultados_deseados.append(res_des)
        if (resultados_deseados[0] > 0 and resultados_deseados[0] <= max_ruleta):
            resultados_deseados_validado = resultados_deseados[0]
    return resultados_deseados


def apuesta_simple(fondos, apuesta_actual, resultados_deseados, multiplicador):
    print('Resultado/s deseado/s: ',resultados_deseados)
    print('Apuesta simple: ')
    resultados = []
    capital_inicial = fondos
    conteo_giros = 0
    while fondos > 0 and conteo_giros < max_tiradas:
        fondos -= apuesta_actual
        resultado_obtenido = girar_ruleta()
        print('Resultado: ', resultado_obtenido)
        if (resultado_obtenido in resultados_deseados):
            fondos+= apuesta_actual*multiplicador
            print('Ganaste! Capital actual: ', fondos)
        elif (resultado_obtenido not in resultados_deseados):
            print('Perdiste! Capital actual: ', fondos)
        resultados.append(resultado_obtenido)
        conteo_giros += + 1;
    print(resultados)

def martin_gala(fondos, apuesta_base, resultados_deseados, multiplicador):
    print('Resultado/s deseado/s: ',resultados_deseados)
    print('Martingala: ')
    resultados = []
    apuesta_actual = apuesta_base
    conteo_giros = 0
    print('Fondos iniciales: ', fondos)
    print('Apuesta inicial: ', apuesta_actual)
    while fondos > 0 and conteo_giros < max_tiradas:
        fondos = fondos - apuesta_actual
        resultado_obtenido = girar_ruleta()
        print('Resultado: ', resultado_obtenido)
        if (resultado_obtenido in resultados_deseados):
            premio = apuesta_actual*multiplicador
            fondos = fondos + premio
            print('Ganaste: $',premio,' , volves a la apuesta inicial! Capital actual: $', fondos)
            apuesta_actual = apuesta_base
        else:
            apuesta_actual = apuesta_actual * 2
            print('Perdiste, duplicas! Capital actual: $', fondos)
            print('Proxima apuesta: $', apuesta_actual)
            if (fondos <= apuesta_actual):
                print('No quedan fondos suficientes para seguir haciendo MartinGala')
                resultados.append(resultado_obtenido)
                break
        resultados.append(resultado_obtenido)
        conteo_giros += 1;
    print(resultados)


# En la fibonacci, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def calcular_fib(n):
    if n < 2:
        return n
    else:
        return calcular_fib(n-1) + calcular_fib(n-2)

def fibonacci(fondos, apuesta_base, resultados_deseados, multiplicador):
    print('')
    print('Fibonacci: ')
    print('')
    print('-----Datos iniciales-----')
    print('Resultado/s deseado/s: ',resultados_deseados)
    resultados_fibo = []
    apuesta_actual = apuesta_base
    print('Apuesta inicial: ', apuesta_actual)
    print('')
    print('-----Datos corridas-----')
    fib_index_actual = 1
    valor_fib_actual = 1
    conteo_giros = 0
    
    while fondos > apuesta_actual and conteo_giros < max_tiradas:
        print('Fondo antes de la apuesta: $', fondos)
        fondos = fondos - apuesta_actual
        resultado_obtenido = girar_ruleta()
        print('Resultado de la tirada: ', resultado_obtenido)
        print('Apuesta actual: ', apuesta_actual)
        print('Fibonacci index actual: ', fib_index_actual)
        print('Valor Fibonacci actual: ', valor_fib_actual)
        print('Fondo despues de la apuesta: $', fondos)
        if (resultado_obtenido in resultados_deseados):
            premio = apuesta_actual*multiplicador
            fondos = fondos + premio
            print('Ganaste: $', premio)
            print('Volves a la apuesta anterior! Capital actual: $', fondos)
            if fib_index_actual < 2:
                fib_index_actual = 1
            else:
                fib_index_actual = fib_index_actual - 1
            valor_fib_actual = calcular_fib(fib_index_actual)
            apuesta_actual = apuesta_base * valor_fib_actual
        else:
            fib_index_actual = fib_index_actual + 1
            valor_fib_actual = calcular_fib(fib_index_actual)
            apuesta_actual = apuesta_base * valor_fib_actual
            print('Perdiste! Capital actual: $', fondos)
            if (fondos < apuesta_base):
                print('No quedan fondos suficientes para seguir haciendo Fibonacci')
                resultados_fibo.append(resultado_obtenido)
                break
        resultados_fibo.append(resultado_obtenido)
        conteo_giros += 1
        print(' ')
    print('Resultados fibonacci', resultados_fibo)
    print(' ')


def start_ruleta(ruleta):
    # ingreso fondos y valido, si es 0 el capital tiene que ser infinito
    fondos = float(input("Ingrese el capital total (0, si desea capital infinito): $"))
    while fondos < 0:
        fondos = float(input("Ingrese el capital total: "))
    if fondos == 0:
        fondos = 99999999999

    # ingreso y valido cantidad a apostar.
    apuesta_actual = get_apuesta_deseada(fondos)
    
    # ingreso estrategia de apuesta

    resultados_deseados_rojos = []
    resultados_rojos_as = []
    resultados_rojos_mg = []
    resultados_rojos_fi = []

    resultados_deseados_pares = []
    resultados_pares_as = []
    resultados_pares_mg = []
    resultados_pares_fi = []

    resultados_deseados_docenas = []
    resultados_docenas_as = []
    resultados_docenas_mg = []
    resultados_docenas_fi = []

    resultados_deseados_columnas = []
    resultados_columnas_as = []
    resultados_columnas_mg = []
    resultados_columnas_fi = []

    resultados_deseados_plenos = []
    resultados_plenos_as = []
    resultados_plenos_mg = []
    resultados_plenos_fi = []

    print('Usted apostará $',apuesta_actual)

    for i in range(0, 1):
        #se juega los rojos
        resultados_deseados = ruleta.get('rojos')
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('rojos'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('rojos'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('rojos'))

        #se guarda los rojos
        resultados_deseados_rojos.append(resultados_deseados)
        resultados_rojos_as.append(ap)
        resultados_rojos_mg.append(mg)
        resultados_rojos_fi.append(fi)


        #se juega los pares
        resultados_deseados = ruleta.get('pares')
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pares'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pares'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pares'))

        #se guarda los pares
        resultados_deseados_pares.append(resultados_deseados)
        resultados_pares_as.append(ap)
        resultados_pares_mg.append(mg)
        resultados_pares_fi.append(fi)


        #se juega las docenas
        resultados_deseados = ruleta.get('docenas')[0]
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('docenas'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('docenas'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('docenas'))

        #se guarda las docenas
        resultados_deseados_docenas.append(resultados_deseados)
        resultados_docenas_as.append(ap)
        resultados_docenas_mg.append(mg)
        resultados_docenas_fi.append(fi)

        #se juega las columnas
        resultados_deseados = ruleta.get('columnas')
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('columnas'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('columnas'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('columnas'))

        #se guarda las columnas
        resultados_deseados_columnas.append(resultados_deseados)
        resultados_columnas_as.append(ap)
        resultados_columnas_mg.append(mg)
        resultados_columnas_fi.append(fi)


        #se juega los plenos
        resultados_deseados = get_lista_resultados_deseados()
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pleno'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pleno'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pleno'))

        #se guarda los plenos
        resultados_deseados_plenos.append(resultados_deseados)
        resultados_plenos_as.append(ap)
        resultados_plenos_mg.append(mg)
        resultados_plenos_fi.append(fi)


def main():
    # creo la ruleta y la inicializo
    ruleta = ini_ruleta()
    # inicio el juego
    start_ruleta(ruleta)

if __name__ == "__main__":
    main()