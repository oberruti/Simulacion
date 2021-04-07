from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

min_ruleta = 0
max_ruleta = 36
numeros_ruleta = 37.0
verde = 0
max_tiradas = 35
corridas_programa = 10
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


def apuesta_simple(capital_inicial, apuesta_actual, resultados_deseados, multiplicador):
    print('     Apuesta simple: ')
    resultados = []
    fondos = capital_inicial
    conteo_giros = 0
    while conteo_giros < max_tiradas:
        if fondos < apuesta_actual:
            resultados.append({'valor': None, 'caja': fondos})
        else:
            fondos -= apuesta_actual
            resultado_obtenido = girar_ruleta()
            if (resultado_obtenido in resultados_deseados):
                fondos+= apuesta_actual*multiplicador
            resultados.append({'valor': resultado_obtenido, 'caja': fondos})
        conteo_giros += 1
        print('             conteo giros: ', conteo_giros)
    return resultados

def martin_gala(fondos, apuesta_base, resultados_deseados, multiplicador):
    print('     Martin Gala: ')
    resultados = []
    apuesta_actual = apuesta_base
    conteo_giros = 0
    while conteo_giros < max_tiradas:
        if fondos < apuesta_actual:
            resultados.append({'valor': None, 'caja': fondos})
        else:
            fondos = fondos - apuesta_actual
            resultado_obtenido = girar_ruleta()
            if (resultado_obtenido in resultados_deseados):
                premio = apuesta_actual*multiplicador
                fondos = fondos + premio
                apuesta_actual = apuesta_base
            else:
                apuesta_actual = apuesta_actual * 2
            resultados.append({'valor': resultado_obtenido, 'caja': fondos})
        conteo_giros += 1
        print('             conteo giros: ', conteo_giros)
    return resultados


# En la fibonacci, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def calcular_fib(n):
    if n < 2:
        return n
    else:
        return calcular_fib(n-1) + calcular_fib(n-2)

def fibonacci(fondos, apuesta_base, resultados_deseados, multiplicador):
    print('     Fibonacci: ')
    resultados_fibo = []
    apuesta_actual = apuesta_base
    fib_index_actual = 1
    valor_fib_actual = 1
    conteo_giros = 0
    
    while conteo_giros < max_tiradas:
        if fondos < apuesta_actual:
            resultados_fibo.append({'valor': None, 'caja': fondos})
        else:
            fondos = fondos - apuesta_actual
            resultado_obtenido = girar_ruleta()
            if (resultado_obtenido in resultados_deseados):
                premio = apuesta_actual*multiplicador
                fondos = fondos + premio
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
            resultados_fibo.append({'valor': resultado_obtenido, 'caja': fondos})
        conteo_giros += 1
        print('             conteo giros: ', conteo_giros)
    return resultados_fibo



def start_ruleta(ruleta):
    # ingreso fondos y valido, si es 0 el capital tiene que ser infinito
    fondos = float(input("Ingrese el capital total (0, si desea capital infinito): $"))
    while fondos < 0:
        fondos = float(input("Ingrese el capital total: "))
    if fondos == 0:
        fondos = 99999999999

    # ingreso y valido cantidad a apostar.
    apuesta_actual = get_apuesta_deseada(fondos)

    pleno_deseado = get_lista_resultados_deseados()
    
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

    #print('Usted apostará $',apuesta_actual)

    for i in range(0, corridas_programa):

        print('')
        print('#se juega los rojos')
        resultados_deseados = ruleta.get('rojos')
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('rojos'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('rojos'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('rojos'))

        print('#se guarda los rojos')
        resultados_deseados_rojos.append(resultados_deseados)
        resultados_rojos_as.append(ap)
        resultados_rojos_mg.append(mg)
        resultados_rojos_fi.append(fi)


        print('#se juega los pares')
        resultados_deseados = ruleta.get('pares')
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pares'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pares'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pares'))

        print('#se guarda los pares')
        resultados_deseados_pares.append(resultados_deseados)
        resultados_pares_as.append(ap)
        resultados_pares_mg.append(mg)
        resultados_pares_fi.append(fi)


        print('#se juega las docenas')
        resultados_deseados = ruleta.get('docenas')[0]
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('docenas'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('docenas'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('docenas'))

        print('#se guarda las docenas')
        resultados_deseados_docenas.append(resultados_deseados)
        resultados_docenas_as.append(ap)
        resultados_docenas_mg.append(mg)
        resultados_docenas_fi.append(fi)

        print('#se juega las columnas')
        resultados_deseados = ruleta.get('columnas')[0]
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('columnas'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('columnas'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('columnas'))

        print('#se guarda las columnas')
        resultados_deseados_columnas.append(resultados_deseados)
        resultados_columnas_as.append(ap)
        resultados_columnas_mg.append(mg)
        resultados_columnas_fi.append(fi)


        print('#se juega los plenos')
        resultados_deseados = pleno_deseado
        ap = apuesta_simple(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pleno'))
        mg = martin_gala(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pleno'))
        fi = fibonacci(fondos, apuesta_actual, resultados_deseados, estrategia_multiplicador.get('pleno'))

        print('#se guarda los plenos')
        resultados_deseados_plenos.append(resultados_deseados)
        resultados_plenos_as.append(ap)
        resultados_plenos_mg.append(mg)
        resultados_plenos_fi.append(fi)

    retorno = {
    'resultados_deseados_rojos': resultados_deseados_rojos,
    'resultados_rojos_as': resultados_rojos_as,
    'resultados_rojos_mg': resultados_rojos_mg,
    'resultados_rojos_fi': resultados_rojos_fi,
    'resultados_deseados_pares': resultados_deseados_pares,
    'resultados_pares_as': resultados_pares_as,
    'resultados_pares_mg': resultados_pares_mg,
    'resultados_pares_fi': resultados_pares_fi,
    'resultados_deseados_docenas': resultados_deseados_docenas,
    'resultados_docenas_as': resultados_docenas_as,
    'resultados_docenas_mg': resultados_docenas_mg,
    'resultados_docenas_fi': resultados_docenas_fi,
    'resultados_deseados_columnas': resultados_deseados_columnas,
    'resultados_columnas_as': resultados_columnas_as,
    'resultados_columnas_mg': resultados_columnas_mg,
    'resultados_columnas_fi': resultados_columnas_fi,
    'resultados_deseados_plenos': resultados_deseados_plenos,
    'resultados_plenos_as': resultados_plenos_as,
    'resultados_plenos_mg': resultados_plenos_mg,
    'resultados_plenos_fi': resultados_plenos_fi,
    'fondos': fondos
    }


    return retorno



# def get_grafico_resultados(resultados):
#     valores_resultados = []
#     index = []
#     for x in range(0, len(resultados[0])):
#         resultado = resultados[0][x].get('valor')
#         valores_resultados.append(resultado)
#         index.append(x)

#     lista = []
#     for i in range(0, len(valores_resultados)):
#         element = []
#         element.append(valores_resultados[i])
#         element.append(i)
#         lista.append(element)
#     df = pd.DataFrame(columns=['resultados', 'tirada'], index=index, data=lista)
#     ax1 = df.plot(kind='scatter', x='tirada', y='resultados', color='r', label="Resultados")    
#     print(df)
#     plt.xlabel("Tirada")
#     plt.ylabel("Valores")

#     plt.title("Grafico resultados obtenidos")
#     plt.savefig("grafico-resultados-obtenidos.svg")


def get_fr_obtenida(resultados, resultados_posibles):
    resultados_filtrados = []
    for objeto in resultados:
        resultados_filtrados.append(objeto.get('valor'))
    veces_obtenido_resultado_deseado = 0
    for x in resultados_posibles:
        veces_obtenido_resultado_deseado += resultados_filtrados.count(x)
    cantidad_tiros = len(resultados)
    return float(float(veces_obtenido_resultado_deseado)/float(cantidad_tiros))


def graficar(valores_obtenidos, fondos):
    resultados_deseados_rojos = valores_obtenidos.get('resultados_deseados_rojos')
    resultados_rojos_as = valores_obtenidos.get('resultados_rojos_as')
    resultados_rojos_mg = valores_obtenidos.get('resultados_rojos_mg')
    resultados_rojos_fi = valores_obtenidos.get('resultados_rojos_fi')

    resultados_deseados_pares = valores_obtenidos.get('resultados_deseados_pares')
    resultados_pares_as = valores_obtenidos.get('resultados_pares_as')
    resultados_pares_mg = valores_obtenidos.get('resultados_pares_mg')
    resultados_pares_fi = valores_obtenidos.get('resultados_pares_fi')

    resultados_deseados_docenas = valores_obtenidos.get('resultados_deseados_docenas')
    resultados_docenas_as = valores_obtenidos.get('resultados_docenas_as')
    resultados_docenas_mg = valores_obtenidos.get('resultados_docenas_mg')
    resultados_docenas_fi = valores_obtenidos.get('resultados_docenas_fi')

    resultados_deseados_columnas = valores_obtenidos.get('resultados_deseados_columnas')
    resultados_columnas_as = valores_obtenidos.get('resultados_columnas_as')
    resultados_columnas_mg = valores_obtenidos.get('resultados_columnas_mg')
    resultados_columnas_fi = valores_obtenidos.get('resultados_columnas_fi')

    resultados_deseados_plenos = valores_obtenidos.get('resultados_deseados_plenos')
    resultados_plenos_as = valores_obtenidos.get('resultados_plenos_as')
    resultados_plenos_mg = valores_obtenidos.get('resultados_plenos_mg')
    resultados_plenos_fi = valores_obtenidos.get('resultados_plenos_fi')

    get_grafico_fr_by_resultados(resultados_rojos_as, resultados_deseados_rojos, "rojos apuesta simple F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_rojos_mg, resultados_deseados_rojos, "rojos martin gala F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_rojos_fi, resultados_deseados_rojos, "rojos fibonacci F.I: $"+str(fondos))

    get_grafico_fr_by_resultados(resultados_pares_as, resultados_deseados_pares, "pares apuesta simple F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_pares_mg, resultados_deseados_pares, "pares martin gala F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_pares_fi, resultados_deseados_pares, "pares fibonacci F.I: $"+str(fondos))

    get_grafico_fr_by_resultados(resultados_docenas_as, resultados_deseados_docenas, "docenas apuesta simple F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_docenas_mg, resultados_deseados_docenas, "docenas martin gala F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_docenas_fi, resultados_deseados_docenas, "docenas fibonacci F.I: $"+str(fondos))

    get_grafico_fr_by_resultados(resultados_columnas_as, resultados_deseados_columnas, "columnas apuesta simple F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_columnas_mg, resultados_deseados_columnas, "columnas martin gala F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_columnas_fi, resultados_deseados_columnas, "columnas fibonacci F.I: $"+str(fondos))

    get_grafico_fr_by_resultados(resultados_plenos_as, resultados_deseados_plenos, "plenos apuesta simple F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_plenos_mg, resultados_deseados_plenos, "plenos martin gala F.I: $"+str(fondos))
    get_grafico_fr_by_resultados(resultados_plenos_fi, resultados_deseados_plenos, "plenos fibonacci F.I: $"+str(fondos))



def get_grafico_fr_by_resultados(resultados, resultados_posibles, nombre_archivo):
    lista_de_fr = []

    #corridas para obtener valores
    for i in range(0, corridas_programa):
    
        lista_de_lista_de_resultados = []
        fr_obtenidas = []

        for y in range(1, max_tiradas+1):
            temporal_lista  = []

            #analiza resultados incrementalmente
            for x in range(0, y):
                temporal_lista.append(resultados[i][x])
            lista_de_lista_de_resultados.append(temporal_lista)
            fr_obtenidas.append(get_fr_obtenida(lista_de_lista_de_resultados[y-1], resultados_posibles[0]))

        lista_de_fr.append(fr_obtenidas)



    #para grafica de resultados    
    tiradas = []
    for i in range(1, max_tiradas+1):
        tiradas.append(i)

    #armado de graficos
    get_grafico_fr(tiradas, lista_de_fr, nombre_archivo)


def get_grafico_fr(tiradas, lista_de_fr, nombre_archivo):
    df = pd.DataFrame(columns=tiradas, data=lista_de_fr)
    
    print(df)

    names = []
    cantidad_de_lineas = len(lista_de_fr)
    for i in range(0, cantidad_de_lineas):
            names.append('FR ' + str(i+1))

    df = df.set_index([names])

    df.T.plot()
    plt.xlabel("Tiradas")
    plt.ylabel("Frecuencias relativas")
    plt.title("Grafico frecuencias relativas "+str(nombre_archivo))
    plt.savefig("grafico-fr-relativas-"+str(nombre_archivo)+".svg")



def main():
    # creo la ruleta y la inicializo
    ruleta = ini_ruleta()
    # inicio el juego
    valores_obtenidos = start_ruleta(ruleta)
    fondos = valores_obtenidos.get('fondos')
    if fondos == 99999999999:
        fondos = 'infinito'
    else:
        fondos = str(fondos)
    graficar(valores_obtenidos, fondos)

if __name__ == "__main__":
    main()