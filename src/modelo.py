import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class CampanaPruebas: 
    def __init__(self, defectos):

        # semanas
        self.s = np.array(defectos["semanas"], dtype=float)
        # defectos sumados semana tras semana
        self.d = np.array(defectos["defectos_sum"], dtype=float)
        
        #R1
        self.fiabilidad = None
        self.a = None
        self.b = None

    def goel(self, t, a, b):
        return a * (1 - np.exp(-b * t))

    def restantes(self):
            return self.a - self.d[-1]

    def r_cuadrado(self, reales, estimados):
        # Lo que el modelo no logró explicar
        error = np.sum((reales - estimados) ** 2)
        # La variación total que había en los datos
        total = np.sum((reales - np.mean(reales)) ** 2)
        # R² = 1 significa ajuste perfecto; 0 significa que el modelo no aporta nada
        return 1 - error / total

    def calcular_sem_95(self):
        #Formula en la guía del parcial
        return np.log(20) / self.b

    def procentaje(self): 
        return 100 * self.d[-1] / self.a;

    def ajustar(self):
        semilla = [max(self.d) * 1.3, 0.2]
        # a no puede ser menor que las correcciones ya hechas; b siempre positivo
        limites = ([max(self.d), 0.001], [max(self.d) * 50, 5.0])
        parametros, _ = curve_fit(self.goel, self.s, self.d, p0=semilla,
                                  bounds=limites, maxfev=50000)
        self.a, self.b = parametros
        estimados = self.goel(self.s, self.a, self.b)
        self.fiabilidad = {"a": self.a, "b": self.b,
                           "R2": self.r_cuadrado(self.d, estimados),
                           "encontradas": self.d[-1],
                           "restantes": self.restantes(),
                           "porcentaje": self.procentaje(), 
                           "semana95" : self.calcular_sem_95()
                           }
        return self.fiabilidad

  

    def informe(self):

        #Mostrar resultado resumido
        f = self.fiabilidad

        print("FIABILIDAD — modelo de Goel-Okumoto")
        print(f"  Defectos totales estimados a = {f['a']:.0f}   |   ritmo b = {f['b']:.3f} por semana")
        print(f"  Ya descubiertas: {f['encontradas']:.0f} ({f['porcentaje']:.0f} %)")
        print(f"  Quedarían por descubrir: {f['restantes']:.0f}")
        print(f"  Calidad del ajuste: R² = {f['R2']:.3f}")
        print(f"  Semana en la que se descubririán el 95% de los defectos: {f['semana95']:.0f}")
        print()

    def graficoF(self, titulo=""):

        figura, ejes = plt.subplots(figsize=(8, 4.2))
        f = self.fiabilidad

        ejes.plot(self.s, self.d, color="blue", linewidth=1, label="Defectos reales")
  
        ejes.plot(self.s, self.goel(self.s, f["a"], f["b"]),
                        color="#8B151A", linewidth=0.8, label="Modelo Goel-Okumoto")


        ejes.axhline(f["a"], color="black", linestyle="--", linewidth=1, label="Total estimado a")
        ejes.set_xlabel("Semanas")
        ejes.set_ylabel("Defectos acumulados")
        ejes.set_title(f"Fiabilidad   (R² = {f['R2']:.3f})")
        ejes.legend(fontsize=9)
        ejes.grid(True)
        figura.suptitle(titulo , fontsize=13)
        plt.tight_layout()
        plt.show()
        #Guardar la grafica
        figura.savefig("graficas/resultado.png", dpi=300, bbox_inches="tight")
