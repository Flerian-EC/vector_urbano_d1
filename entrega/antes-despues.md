# Medición Comparativa de Madurez y Calidad (Antes y Después) — Desafío 1

Esta medición compara el estado de partida del paquete de datos oficial (`paquetes/D1-base-digital/linea-base/`) con el activo de datos procesado y entregado por el equipo (`entrega/`), utilizando las herramientas deterministas `dataton scorecard` y `dataton nivel` bajo las mismas reglas y escala de 0 a 7 ([`escala-preparacion-0-7.yml`](../dataton-lapaz-2026-punto-cero/evaluacion/escala-preparacion-0-7.yml)).

---

## 1. Resumen de Nivel de Madurez (Escala 0 a 7)

| Dimensión / Criterio | Medición Antes (Línea Base 26/10/2026) | Medición Después (Entrega Equipo 30/10/2026) | Variación e Impacto |
|---|:---:|:---:|---|
| **Nivel Propuesto** | **1 · Identificado** | **5 · Reutilizable** | **+4 Niveles de madurez** |
| **Fuente localizada** | 12 recursos | 18 recursos verificados | +6 tablas analíticas generadas |
| **Documentación Diccionario** | 0.0 % | **100.0 %** | 104 columnas descritas con semántica y tipos |
| **Periodicidad Declarada** | No declarada ("Desconocida") | **Declarada (Anual y Censal)** | Conforme a ciclo censal y memorias |
| **Responsable del Dato** | Por confirmar | **Confirmado (SMCI / INE / ATT)** | Custodios institucionales identificados |
| **Completitud de Tablas** | 84.5 % (incompleta en FO) | **100.0 %** | Cero celdas nulas en campos mínimos |
| **Validez de Tipos y Dominios** | No medible (sin reglas) | **100.0 %** | 100% cumplimiento en patrones y dominios |
| **Unicidad de Registros** | Sin clave declarada | **100.0 %** | Claves primarias únicas sin duplicados |
| **Consistencia de Totales** | No medible | **100.0 %** | Coherencia lógica en numeradores y totales |
| **Territorialización / Vínculos** | No medible | **100.0 %** | Vínculo relacional declarado (Nivel 4 Conectable) |
| **Accesibilidad / Formato Abierto** | 50.0 % | **100.0 %** | Todos los recursos en CSV UTF-8 + Frictionless |
| **Reglas de Uso** | Parcial | **100.0 %** | `reglas-de-uso.md` con CC BY-SA 4.0 / ODbL |

---

## 2. Detalle de Criterios Cumplidos por Nivel (Evaluación Oficial `dataton nivel`)

### Nivel 1 · Identificado [CUMPLE]
- `fuente_localizada`: 18 recursos locales mapeados en `datapackage.json` y fuente primaria declarada en `procedencia.md`.

### Nivel 2 · Documentado [CUMPLE]
- `diccionario_descrito`: **100.0%** de cobertura en `diccionario.csv` (supera ampliamente el umbral del 80%).
- `periodicidad_conocida`: Declarada formalmente en `procedencia.md` como "Anual y Censal".
- `responsable_conocido`: Responsable institucional formalmente identificado (SMCI - GAMLP, INE y ATT).

### Nivel 3 · Depurado [CUMPLE]
- `completitud_minima`: Cumplimiento del 100% en todos los campos mínimos evaluados en las tablas.
- `validez_minima`: Cumplimiento del 100% de reglas de validez (expresiones regulares, rangos numéricos y listas de dominio).
- `unicidad_clave`: Claves declaradas sin ninguna fila duplicada (`codigo_municipio + gestion_censo`, `id_indicador`, `id_dataset`, `id_tramite`).
- `consistencia_minima`: Cumplimiento estricto de reglas lógicas (`hogares_con_internet <= hogares_particulares_ocupados`).

### Nivel 4 · Conectable [CUMPLE]
- `territorio_o_vinculo`: Vínculo relacional documentado y verificado en `reglas-calidad.yml` entre los códigos territoriales del Censo municipal (`020101`) y la matriz de indicadores U4SSC.

### Nivel 5 · Reutilizable [CUMPLE]
- `formato_abierto_y_licencia`: Accesibilidad del **100.0%** con todos los recursos en CSV UTF-8, metadatos legibles por máquina en `datapackage.json` y licencias abiertas declaradas.
- `reglas_de_uso`: Términos de uso ético, atribución y licenciamiento CC BY-SA 4.0 / ODbL presentes en `reglas-de-uso.md`.

### Niveles 6 (Accionable) y 7 (Listo para Ciudad Inteligente)
- Requieren revisión humana por parte del jurado calificador y las unidades técnicas del GAMLP (UIIEM, DICI, UITD).
