import numpy as np
# PRUEBA 1: La cual fue recomendad. En la semana 0 no se han descubierto defectos
def test_goel_semana_cero(modelo):

    resultado = modelo.goel(0, modelo.a or 100, modelo.b or 0.5)

    assert resultado == 0, (
        "Se esperaba 0, pero se obtuvo", resultado
    )

# PRUEBA 2: Comprobar el resultado matemático del modelo
def test_goel_resultado(modelo):

    a = modelo.a or 100
    b = modelo.b or 0.5
    semana = 2

    resultado = modelo.goel(semana, a, b)

    esperado = a * (1 - np.exp(-b * semana))

    assert resultado == esperado, (
        "Se esperaba " +  esperado + " pero se obtuvo " + resultado
    )