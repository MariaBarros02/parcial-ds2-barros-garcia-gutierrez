from pymongo import MongoClient
import numpy as np
from modelo import CampanaPruebas;
import sys
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
sys.path.append(str(raiz))

from test.test_modelo import test_goel_semana_cero, test_goel_resultado


client = MongoClient ('mongodb://admin:123456@127.0.0.1:27017/')
db = client.huilasoft_bd;

defectos = list(db.defectos.find())



semanas = [defecto["semana"] for defecto in defectos]
defectos_acum =  [defecto["def_encontrados"] for defecto in defectos]
print(defectos_acum)
print(semanas)
defectos_sum = np.cumsum(defectos_acum)

defectos_normalizados = {
    "semanas": semanas, 
    "defectos_sum": defectos_sum
    } 

simulacion = CampanaPruebas(defectos_normalizados);

simulacion.ajustar()

simulacion.graficoF("Evolución del software")
simulacion.informe();

test_goel_semana_cero(simulacion)
test_goel_resultado(simulacion)



