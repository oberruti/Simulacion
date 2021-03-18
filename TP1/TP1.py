from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


min_ruleta = 0
max_ruleta = 36
numeros_ruleta = 37.0
valor_estadistico_ruleta = 1.0/37.0


#fr = frecuencia relativa
#vp = valor promedio
#vd = valor desvio
#vv = valor varianza

def girar_ruleta(cantidad_giros):
    resultados = []
    for i in range(0,cantidad_giros):
        resultado = randint(min_ruleta, max_ruleta)
        resultados.append(resultado)
    return resultados


def get_fr_esperada(cantidad_giros):
    fr_esperada = 0.0
    fr_esperada = float(cantidad_giros)/float(numeros_ruleta)
    return fr_esperada


def get_vp_esperado(cantidad_giros):
    sumatoria_giros = 0.0
    for i in range(0, cantidad_giros):
        sumatoria_giros+=i
    return float(sumatoria_giros)/float(cantidad_giros)


def get_vd_esperado(cantidad_giros):
    valores_posibles = []
    for i in range(min_ruleta, max_ruleta):
        valores_posibles.append(i)
    lista = np.array(valores_posibles)
    return lista.std()
    

def get_vv_esperado(cantidad_giros):
    valores_posibles = []
    for i in range(min_ruleta, max_ruleta):
        valores_posibles.append(i)
    lista = np.array(valores_posibles)
    return lista.var()


def get_fr_obtenida(resultados, resultado_deseado):
    veces_obtenido_resultado_deseado = resultados.count(resultado_deseado)
    cantidad_tiros = len(resultados)
    return float(float(veces_obtenido_resultado_deseado)/float(cantidad_tiros))


def get_vp_obtenido(resultados):
    sumatoria_valores_obtenidos = 0
    for i in resultados:
        sumatoria_valores_obtenidos+=i
    return float(sumatoria_valores_obtenidos/len(resultados))


def get_vd_obtenido(resultados):
    lista = np.array(resultados)
    return lista.std()


def get_vv_obtenido(resultados):
    lista = np.array(resultados)
    return lista.var()


def get_grafico_resultados(tiradas, resultados_deseados, resultados):
    df = pd.DataFrame(columns=tiradas, data=[resultados_deseados, resultados])
    df = df.set_index([["Resultados deseados", "Resultados obtenidos"]])
    df.T.plot()
    plt.xlabel("Tiradas")
    plt.ylabel("Valores")
    plt.title("Grafico resultados deseados vs obtenidos")
    plt.savefig("grafico-resultados.png")


def get_grafico_fr(tiradas, fr_esperadas, fr_obtenidas):
    df = pd.DataFrame(columns=tiradas, data=[fr_esperadas, fr_obtenidas])
    df = df.set_index([["Frecuencia relativa esperada", "Frecuencia relativa obtenida"]])
    print(df)
    df.T.plot()
    plt.xlabel("Tiradas")
    plt.ylabel("Valores")
    plt.title("Grafico frecuencias relativas esperadas vs obtenidas")
    plt.savefig("grafico-fr-relativas.png")


def get_grafico_vp(tiradas, vp_esperados, vp_obtenidos):
    df = pd.DataFrame(columns=tiradas, data=[vp_esperados, vp_obtenidos])
    df = df.set_index([["Valor promedio esperado", "Valor promedio obtenido"]])
    print(df)
    df.T.plot()
    plt.xlabel("Tiradas")
    plt.ylabel("Valores")
    plt.title("Grafico valores promedio esperados vs valores promedio obtenidos")
    plt.savefig("grafico-vp.png")


def get_grafico_vd(tiradas, vd_esperados, vd_obtenidos):
    df = pd.DataFrame(columns=tiradas, data=[vd_esperados, vd_obtenidos])
    df = df.set_index([["Valor desvio esperado", "Valor desvio obtenido"]])
    print(df)
    df.T.plot()
    plt.xlabel("Tiradas")
    plt.ylabel("Valores")
    plt.title("Grafico valores desvio estandar esperados vs obtenidos")
    plt.savefig("grafico-vd.png")


def get_grafico_vv(tiradas, vv_esperados, vv_obtenidos):
    df = pd.DataFrame(columns=tiradas, data=[vv_esperados, vv_obtenidos])
    df = df.set_index([["Valor varianza esperado", "Valor varianza obtenido"]])
    print(df)
    df.T.plot()
    plt.xlabel("Tiradas")
    plt.ylabel("Valores")
    plt.title("Grafico valores varianza esperados vs valores varianza obtenidos")
    plt.savefig("grafico-vv.png")


def jugar_ruleta(cantidad_giros, resultado_deseado):
    resultados = []
    fr_esperadas = []
    vp_esperados = []
    vd_esperados = []
    vv_esperados = []
    fr_obtenidas = []
    vp_obtenidos = []
    vd_obtenidos = []
    vv_obtenidos = []
    for i in range(1, cantidad_giros+1):
        resultados.append(girar_ruleta(i))
        fr_esperadas.append(get_fr_esperada(i))
        vp_esperados.append(get_vp_esperado(i))
        vd_esperados.append(get_vd_esperado(i))
        vv_esperados.append(get_vv_esperado(i))
        fr_obtenidas.append(get_fr_obtenida(resultados[i-1], resultado_deseado))
        vp_obtenidos.append(get_vp_obtenido(resultados[i-1]))
        vd_obtenidos.append(get_vd_obtenido(resultados[i-1]))
        vv_obtenidos.append(get_vv_obtenido(resultados[i-1]))
    tiradas = []
    resultados_deseados = []
    for i in range(1, cantidad_giros+1):
        tiradas.append(i)
        resultados_deseados.append(resultado_deseado)

    get_grafico_resultados(tiradas, resultados_deseados, resultados[len(resultados)-1])
    get_grafico_fr(tiradas, fr_esperadas, fr_obtenidas)
    get_grafico_vp(tiradas, vp_esperados, vp_obtenidos)
    get_grafico_vd(tiradas, vd_esperados, vd_obtenidos)
    get_grafico_vv(tiradas, vv_esperados, vv_obtenidos)


def main():
    cantidad_giros = int(input("Ingrese la cantidad de giros para la ruleta: "))
    resultado_deseado_verificado = -1
    while(resultado_deseado_verificado<0 or resultado_deseado_verificado>36):
        resultado_deseado = int(input("Ingrese el resultado deseado para la ruleta (entre 0 y 36): "))
        if resultado_deseado > 0 or resultado_deseado < 36:
            resultado_deseado_verificado = resultado_deseado
    jugar_ruleta(cantidad_giros, resultado_deseado_verificado)


if __name__ == "__main__":
    main()