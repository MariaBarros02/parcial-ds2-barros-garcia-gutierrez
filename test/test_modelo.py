# PRUEBA 1: En la semana 0 no se han descubierto defectos
def test_goel_semana_cero(modelo):

    resultado = modelo.goel(0, modelo.a or 100, modelo.b or 0.5)

    assert resultado == 0

# PRUEBA 2: Comprobar el resultado matemático del modelo
def test_goel_resultado(modelo):

    a = modelo.a or 100
    b = modelo.b or 0.5
    semana = 2