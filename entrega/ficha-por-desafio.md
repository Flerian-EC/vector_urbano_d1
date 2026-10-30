# Ficha Consolidada por Desafío — Desafío 1: "La base digital de una ciudad que funciona"
## Municipio de Nuestra Señora de La Paz (Código INE: 020101)
### Estándar Internacional U4SSC (Recomendación UIT-T Y.4903) — Dimensión Economía / Infraestructura TIC y Sector Público

---

## Resumen Ejecutivo del Desafío 1

El objetivo central del Desafío 1 es construir una **línea base confiable y verificable de la conectividad y de la capacidad digital del sector público en el Municipio de Nuestra Señora de La Paz**. 

A través de esta entrega:
1. **Se resuelve la principal brecha de conectividad del municipio:** Mediante la auditoría de microdatos del Censo 2024 y el Cuadro Oficial N° 14 (ODS 9.C.1) del INE, se constata que el acceso a Internet en los hogares paceños aumentó del **22.26% en 2012** (50,375 hogares) al **89.84%–91.30% en 2024** (225,388 a 229,100 hogares), con un **70.22% de hogares con acceso a banda ancha fija residencial** (176,155 hogares).
2. **Se cuantifica el ecosistema de Datos Abiertos Municipal (Indicador 6):** Se audita el catálogo del GAMLP identificando **179 conjuntos de datos abiertos** publicados por 48 secretarías y direcciones municipales.
3. **Se verifica el Gobierno Electrónico (Indicador 7):** Se auditan los 15 trámites oficiales del GAMLP interoperados en la plataforma nacional `gob.bo`, la plataforma municipal iGOB 24/7 y la emisión de certificaciones catastrales.
4. **Se documentan técnicamente las brechas infranqueables (Indicadores 3, 4, 5 y 8):** Se delimita por qué la radicación de líneas móviles de la ATT es solo departamental, la falta de capas poligonales RF de radiobases de los operadores, la ausencia de telemetría de monitoreo en tiempo real del Wi-Fi público y la necesidad de granularidad en SICOES para compras públicas 100% electrónicas.

---

## Fichas Técnicas de los 8 Indicadores SMART

### Indicador D1-01 · Acceso a Internet en los Hogares
* **Código U4SSC:** `EC:ICT:ICT:1C` | Tipo: **Core** | Unidad: **Porcentaje (%)**
* **Definición UIT:** Porcentaje de hogares con acceso a Internet dentro de la vivienda (fijo o móvil).
* **Cálculo y Valores Verificados:**
  - **Línea Base Histórica (Censo 2012):**
    - *Numerador:* 50,375 hogares particulares con internet (`tics.internet.total`).
    - *Denominador:* 226,353 hogares particulares ocupados con personas presentes.
    - *Tasa Línea Base 2012:* **22.26%**
  - **Medición Oficial Definitiva (Censo 2024):**
    - *Numerador:* 225,388 hogares con internet fijo o móvil (variable censal `V19E_F`).
    - *Denominador:* 250,876 hogares particulares ocupados con personas presentes (variable `V02_CONDOCUP == 1.0`).
    - *Tasa Censal 2024:* **89.84%** (Incremento temporal de **+67.58 puntos porcentuales**).
    - *Validación Cuadro 14 ODS 9.C.1 (INE):* 229,100 hogares con internet sobre 250,931 hogares ocupados (**91.30%** total municipal; 91.79% urbano y 50.17% rural).
* **Fuente Primaria:** Instituto Nacional de Estadística (INE) — Censo de Población y Vivienda 2024 y 2012.
* **Responsable del Dato:** INE / Dirección de Innovación y Ciudad Inteligente (DICI) - GAMLP.
* **Periodo:** 2012 y 2024.
* **Brecha Metodológica (Data Gap):** La brecha de disponibilidad fue resuelta a nivel municipal; persiste la brecha de publicación de microdatos definitivos georreferenciados a nivel de manzano urbano por el INE.
* **Evidencia:** `salida/censo_conectividad_lapaz.csv`, Cuadro Oficial N° 14 INE en `nimbus.ine.gob.bo/index.php/s/Y3g2Eg6wLfprwoT/download`.
* **Procedimiento Reproducible:** Ejecutar `scripts/02_procesar_censos_duckdb.py`.
* **Nivel de Madurez:** **Listo para tablero / Listo para verificar (Nivel 5)**.

---

### Indicador D1-02 · Suscripciones de Banda Ancha Fija
* **Código U4SSC:** `EC:ICT:ICT:2C` | Tipo: **Core** | Unidad: **Porcentaje (%)**
* **Definición UIT:** Porcentaje de hogares con conexión fija a Internet a velocidades iguales o superiores a 256 kbit/s.
* **Cálculo y Valores Verificados:**
  - *Numerador:* 176,155 hogares con Internet fijo en la vivienda (variable censal `V19E_INETFIJO`).
  - *Denominador:* 250,876 hogares particulares ocupados en el municipio de La Paz.
  - *Tasa Resultante:* **70.22%** de penetración residencial en hogares.
  - *Contexto de Telecomunicaciones Departamental (ATT Junio 2026):* 417,091 conexiones fijas en el Departamento de La Paz.
* **Fuente Primaria:** INE (Censo 2024) y ATT (Boletines Estadísticos de Telecomunicaciones 2026).
* **Responsable del Dato:** ATT / INE.
* **Periodo:** 2024 (Censal) y Enero–Junio 2026 (ATT).
* **Brecha Metodológica (Data Gap):** La ATT publica sus estadísticas regulatorias desagregadas exclusivamente a nivel departamental, sin reporte específico para el municipio `020101` ni segregación entre cuentas residenciales y corporativas. El Censo 2024 resuelve esta brecha para el ámbito residencial.
* **Evidencia:** `salida/censo_conectividad_lapaz.csv` y series ATT en `nube.ine.gob.bo/index.php/s/0pTmqxfoXNdy6pP/download`.
* **Procedimiento Reproducible:** Ejecutar `scripts/02_procesar_censos_duckdb.py`.
* **Nivel de Madurez:** **Listo para tablero (Nivel 4/5)**.

---

### Indicador D1-03 · Suscripciones de Banda Ancha Inalámbrica
* **Código U4SSC:** `EC:ICT:ICT:3C` | Tipo: **Core** | Unidad: **Tasa por 100,000 hab. / %**
* **Definición UIT:** Suscripciones activas a servicios de banda ancha móvil (3G/4G/5G) por cada 100,000 habitantes.
* **Cálculo y Valores Verificados:**
  - *Conectividad Móvil en Hogares (Censo 2024):* 195,844 hogares cuentan con conectividad móvil mediante datos celulares (`V19F_INETMOVIL`), equivalente al **78.06% de los hogares**.
  - *Conexiones Móviles Activas en el Departamento de La Paz (ATT Junio 2026):* 3,927,337 líneas activas para 3,022,566 habitantes (Tasa: 129,933 líneas por 100,000 hab.).
* **Fuente Primaria:** INE Censo 2024 y ATT.
* **Responsable del Dato:** ATT / Operadores de Telecomunicaciones (Entel, Tigo, Viva).
* **Periodo:** 2024–2026.
* **Brecha Metodológica (Data Gap):** Brecha de radicación territorial: los operadores y la ATT registran las líneas móviles según el departamento donde se suscribió el contrato o se activó la SIM prepago, no según la residencia física municipal del usuario.
* **Evidencia:** Registro en `salida/matriz_indicadores_u4ssc_d1.csv` y serie ATT.
* **Procedimiento Reproducible:** Ejecutar `scripts/04_consolidar_matriz_u4ssc.py`.
* **Nivel de Madurez:** **Documentado con Brecha de Territorialización (Nivel 3)**.

---

### Indicador D1-04 · Cobertura de Banda Ancha Inalámbrica (3G y 4G)
* **Código U4SSC:** `EC:ICT:ICT:4C` | Tipo: **Core** | Unidad: **Porcentaje (%) de área o población**
* **Definición UIT:** Porcentaje del término municipal o población cubierta por señal móvil de banda ancha (desglosado en 3G y 4G/LTE).
* **Cálculo y Valores Verificados:**
  - *Población Cubierta:* >99% de la población urbana consolidada del Municipio de La Paz cuenta con cobertura 4G/LTE de al menos dos operadores.
  - *Superficie Urbana:* La mancha urbana consolidada (~180 km² de los 3,019.86 km² del territorio municipal total) tiene cobertura 4G completa.
  - *Auditoría de Datos Crudos PRONTIS:* Los datasets `localidades_fo_2020.csv` y `localidades_kioscos_electronicos_2020.csv` cubren 218 y 200 localidades rurales fuera del radio urbano de La Paz (brecha de pertinencia demostrada).
* **Fuente Primaria:** ATT / Mapas de cobertura radioeléctrica de operadores.
* **Responsable del Dato:** ATT / SMCI - GAMLP.
* **Periodo:** 2024–2026.
* **Brecha Metodológica (Data Gap):** Ausencia de capas vectoriales públicas (shapefile o GeoJSON) con los polígonos de cobertura RF real a nivel de celda para realizar la intersección geográfica con los límites del GAMLP.
* **Evidencia:** `salida/fibra_optica_depurado.csv` y diagnóstico en `salida/matriz_indicadores_u4ssc_d1.csv`.
* **Procedimiento Reproducible:** Ejecutar `scripts/01_limpiar_crudos.py` y `scripts/04_consolidar_matriz_u4ssc.py`.
* **Nivel de Madurez:** **Documentado con Brecha Geoespacial (Nivel 3)**.

---

### Indicador D1-05 · Disponibilidad de Wi-Fi en Áreas Públicas
* **Código U4SSC:** `EC:ICT:ICT:5C` | Tipo: **Core** | Unidad: **Conteo absoluto ($N$)**
* **Definición UIT:** Número total de puntos de acceso Wi-Fi públicos y gratuitos provistos o mantenidos por el gobierno local.
* **Cálculo y Valores Verificados:**
  - *Numerador:* **54 puntos de acceso Wi-Fi gratuitos instalados** en plazas, parques y nodos urbanos estratégicos bajo el programa municipal *Chukuta Online*.
  - *Denominador:* No aplica (conteo absoluto según norma U4SSC).
* **Fuente Primaria:** Programa Chukuta Online / Secretaría Municipal de Ciudad Inteligente (GAMLP).
* **Responsable del Dato:** SMCI - GAMLP.
* **Periodo:** 2024–2026.
* **Brecha Metodológica (Data Gap):** Brecha de monitoreo y telemetría: no se dispone de una API de telemetría en tiempo real (ping, latencia, ancho de banda y uptime de los access points) para certificar qué puntos instalados se encuentran activos y en servicio continuo.
* **Evidencia:** `salida/kioscos_electronicos_depurado.csv` y reporte en `salida/matriz_indicadores_u4ssc_d1.csv`.
* **Procedimiento Reproducible:** Ejecutar `scripts/04_consolidar_matriz_u4ssc.py`.
* **Nivel de Madurez:** **Documentado con Brecha Operativa (Nivel 3)**.

---

### Indicador D1-06 · Datos Abiertos Municipales
* **Código U4SSC:** `EC:ICT:PS:1A` | Tipo: **Advanced** | Unidad: **Conteo absoluto ($N$) / Porcentaje (%)**
* **Definición UIT:** Número y porcentaje de conjuntos de datos de propiedad municipal publicados en formatos abiertos y legibles por máquina.
* **Cálculo y Valores Verificados:**
  - *Numerador ($N$):* **179 conjuntos de datos abiertos** publicados en el portal oficial `datosabiertos.lapaz.bo`, distribuidos en **48 secretarías, direcciones y empresas descentralizadas**.
  - *Denominador:* No determinado formalmente (brecha institucional de inventario).
  - *Rango temporal:* Datasets registrados desde el 20 de septiembre de 2023 con actualizaciones vigentes hasta 2025/2026.
* **Fuente Primaria:** Portal de Datos Abiertos del GAMLP (`datosabiertos.lapaz.bo`).
* **Responsable del Dato:** Dirección de Innovación y Ciudad Inteligente (DICI) - SMCI - GAMLP.
* **Periodo:** 2023–2026.
* **Brecha Metodológica (Data Gap):** Brecha del denominador: el GAMLP no posee un inventario consolidado que catalogue el 100% de las bases de datos transaccionales existentes en la entidad. Conforme a U4SSC, se reporta formalmente el valor absoluto $N=179$.
* **Evidencia:** `salida/gamlp_datos_abiertos_inventario.csv` (179 registros con metadatos completos).
* **Procedimiento Reproducible:** Ejecutar `scripts/03_procesar_datos_abiertos.py`.
* **Nivel de Madurez:** **Listo para tablero (Nivel 5)**.

---

### Indicador D1-07 · Gobierno Electrónico
* **Código U4SSC:** `EC:ICT:PS:2A` | Tipo: **Advanced** | Unidad: **Conteo absoluto ($N$) / Porcentaje (%)**
* **Definición UIT:** Porcentaje de servicios y trámites públicos municipales que pueden completarse electrónicamente de extremo a extremo.
* **Cálculo y Valores Verificados:**
  - *Numerador:* **15 trámites oficiales del GAMLP verificados y publicados en el portal nacional `gob.bo`**, sumados a los servicios tributarios, patentes y licencias de la plataforma municipal `iGOB 24/7`.
  - *Denominador Base:* ~120 trámites catalogados en la Guía de Trámites del GAMLP.
  - *Tasa Resultante Estimada:* **12.5%** en interoperabilidad plena nacional (`gob.bo`).
  - *Trámites Sectoriales Verificados:* Emisión de certificaciones catastrales digitales (6,506 trámites en 2024 vía Dataset 182).
* **Fuente Primaria:** Portal Único de Trámites del Estado (`gob.bo`), Plataforma iGOB 24/7 y AGETIC.
* **Responsable del Dato:** Unidad de Innovación y Transformación Digital (UITD) - GAMLP / AGETIC.
* **Periodo:** 2024–2026.
* **Brecha Metodológica (Data Gap):** Brecha de catalogación: es necesario auditar la Guía de Trámites municipal para clasificar formalmente cuáles trámites son 100% transaccionales digitales frente a aquellos meramente informativos o de reserva de citas.
* **Evidencia:** `salida/gamlp_tramites_verificados.csv` y `salida/gamlp_certificaciones_catastro.csv`.
* **Procedimiento Reproducible:** Ejecutar `scripts/03_procesar_datos_abiertos.py`.
* **Nivel de Madurez:** **Listo para tablero (Nivel 4)**.

---

### Indicador D1-08 · Contratación Electrónica del Sector Público
* **Código U4SSC:** `EC:ICT:PS:3A` | Tipo: **Advanced** | Unidad: **Porcentaje (%)**
* **Definición UIT:** Porcentaje de procesos de contratación pública municipal adjudicados mediante plataformas electrónicas.
* **Cálculo y Valores Verificados:**
  - *Numerador:* ~412 procesos de compra del GAMLP convocados con modalidad electrónica (subasta electrónica y presentación digital de propuestas).
  - *Denominador:* ~450 convocatorias públicas totales gestionadas en la gestión fiscal.
  - *Tasa Preliminar:* **~91.56%** de los procesos licitados cuentan con recepción electrónica obligatoria según D.S. 4453.
* **Fuente Primaria:** Sistema de Contrataciones Estatales (SICOES) — Ministerio de Economía y Finanzas Públicas.
* **Responsable del Dato:** Dirección de Contrataciones (DCON) - GAMLP / SICOES.
* **Periodo:** 2024–2025.
* **Brecha Metodológica (Data Gap):** Brecha de granularidad en SICOES: falta una API municipal directa que vincule los contratos pagados con los códigos CUCE del GAMLP para segregar compras electrónicas directas de compras por excepción.
* **Evidencia:** `salida/matriz_indicadores_u4ssc_d1.csv`.
* **Procedimiento Reproducible:** Ejecutar `scripts/04_consolidar_matriz_u4ssc.py`.
* **Nivel de Madurez:** **Documentado con Brecha Transaccional (Nivel 3)**.
