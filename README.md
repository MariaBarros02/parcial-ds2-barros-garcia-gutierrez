## Nombre de la base de datos: huilasoft_bd

## Colecciones:
1. tickets: 
    - num_tickets: string
    - llegada: number
    - atencion: number
    - prioridad: number
    - object_id: object_id uuid

2. agentes: 
    - nombre: string
    - nivel: string
    - tickets_hora: number 
    - object_id: object_id uuid


3. defectos: 
    - semana: number
    - def_encontrados: number
    - object_id: object_id uuid


## Opción escogida B: Evaluación del software: clase Campana Pruebas


FIABILIDAD — modelo de Goel-Okumoto
  Defectos totales estimados a = 198   |   ritmo b = 0.152 por semana
  Ya descubiertas: 139 (70 %)
  Quedarían por descubrir: 59
  Calidad del ajuste: R² = 1.000
  Semana en la que se descubririán el 95% de los defectos: 20


### Pregunta: ¿Cuántos defectos quedarían sin descubrir si se libera hoy? 

### Pregunta: ¿En que semana se llegaría al 95% (t = ln 20 / b)? 


Si la plataforma MatriculApp se libera hoy (final de la semana 8) quedarían unos 59 defectos sin descubrir, es decir, el 30 % de los defectos totales, hasta ahora solo se han encontrado 139 de los 198 que estima el modelo. Además, el sistema llegaría al 95 % de los defectos descubiertos en la semana 20. En la gráfica se puede observar que los puntos de los defectos reales y la curva del modelo Goel-Okumoto tienen un camino muy similar, con un R^2 de 0.9998, lo que significa que el modelo se ajusta bien a los datos. Se recomienda a HuilaSoft no liberar todavía MatriculApp y seguir con las pruebas entre 10 y 12 semanas más, hasta tener una versión mucho más estable, esto le ayudara a que sus usuarios tengan una mejor experiencia usando la plataforma.
