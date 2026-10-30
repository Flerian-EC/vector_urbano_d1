# Procedencia y Trazabilidad del Activo de Datos — Desafío 1

| Metadato | Valor |
|---|---|
| Fuente | Instituto Nacional de Estadística (INE), Gobierno Autónomo Municipal de La Paz (GAMLP), Autoridad de Fiscalización y Regulación de Telecomunicaciones y Transportes (ATT), AGETIC y catálogo oficial Datatón Punto Cero |
| Responsable del dato | Secretaría Municipal de Ciudad Inteligente (SMCI) - GAMLP |
| Periodicidad | Anual y Censal (Actualización periódica según ciclo censal y memorias institucionales) |
| Cobertura geográfica | Municipio de Nuestra Señora de La Paz (código INE: 020101) |
| Formato original | CSV, Parquet, JSONL |
| Formato de entrega | CSV UTF-8 normalizado, Frictionless Data Package |
| Licencia declarada | Abierta (Declaración de uso de Datos Abiertos de datos.gob.bo / CC BY 4.0 / ODbL) |

---

## 1. Origen de las Fuentes de Información

1. **Censo de Población y Vivienda 2012 y 2024 (INE):**
   - **Censo 2012:** Microdatos georreferenciados a nivel de manzano urbano (`layer=manzanas`) y comunidad rural (`layer=comunidades`) procesados localmente en formato Parquet mediante DuckDB (`datos/censo_2012_lapaz/MUN=020101/`).
   - **Censo 2024:** Microdatos de vivienda del Municipio de Nuestra Señora de La Paz (020101) extraídos de la federación de datos abiertos `datosbolivia.github.io` (nodo `censo-2024`) y verificados con el Cuadro Oficial N° 14 del INE (ODS 9.C.1) alojado en `nimbus.ine.gob.bo`.
   - **Responsable:** Instituto Nacional de Estadística (INE).

2. **Portal de Datos Abiertos del GAMLP (`datosabiertos.lapaz.bo`):**
   - Índice consolidado de 179 conjuntos de datos en formato Parquet (`datos/gamlp_datos_abiertos/indice.parquet`) y tablas transaccionales en CSV (`data/archive (1)/datasets/`).
   - **Responsable:** Dirección de Innovación y Ciudad Inteligente (DICI) - SMCI - GAMLP.

3. **Portal Único de Trámites del Estado (`gob.bo`) y Plataforma iGOB 24/7:**
   - Catálogo nacional de trámites digitalizados (`tramites.jsonl`) y servicios en línea del GAMLP.
   - **Responsable:** Unidad de Innovación y Transformación Digital (UITD) - GAMLP / AGETIC.

4. **Telecomunicaciones y Espectro Radioeléctrico (ATT):**
   - Series mensuales de conexiones fijas y móviles por departamento publicadas por la ATT e INE (2017–2026).
   - **Responsable:** Autoridad de Regulación y Fiscalización de Telecomunicaciones y Transportes (ATT).

5. **Datos Crudos del Repositorio Datatón Punto Cero (`datos/`):**
   - Kioscos electrónicos y localidades con fibra óptica 2020 (Viceministerio de Telecomunicaciones / PRONTIS).
   - Líneas telefónicas fijas en servicio (INE, 1996–2016).
   - Registros de autenticaciones y aprobaciones de Ciudadanía Digital (AGETIC).

---

## 2. Registro de Cambios y Transformaciones Realizadas

Se aplicó un pipeline de preparación de datos 100% determinista y reproducible implementado en `entrega/scripts/`:

1. **`01_limpiar_crudos.py` (Curación y saneamiento de datos crudos):**
   - **Telefonía fija:** Eliminación de separadores de tabulación y conversión a comas estándar; supresión de la fila vacía inicial; eliminación de espacios en blanco y comas de miles en campos numéricos para garantizar tipado entero.
   - **Kioscos y Fibra Óptica:** Estandarización de codificación a UTF-8 y eliminación de caracteres espurios.
   - **Ciudadanía Digital:** Unificación de delimitadores heterogéneos (pipe `|` convertido a coma `,`); imputación de valores faltantes en la columna institucional `nombre` con `SIN_DATO` para preservar integridad de filas.

2. **`02_procesar_censos_duckdb.py` (Cálculo censal reproducible con DuckDB):**
   - Agregación paralela sobre 9,880 manzanos y 66 comunidades del Municipio de La Paz (`MUN=020101`).
   - Cálculo determinista del denominador (hogares particulares ocupados) y numerador (hogares con internet) para 2012 y 2024.
   - Generación de la tabla `salida/censo_conectividad_lapaz.csv`.

3. **`03_procesar_datos_abiertos.py` (Auditoría institucional del GAMLP y gob.bo):**
   - Extracción de los 179 conjuntos de datos abiertos municipales a `salida/gamlp_datos_abiertos_inventario.csv`.
   - Normalización de los 15 trámites verificados del GAMLP en `salida/gamlp_tramites_verificados.csv`.
   - Procesamiento de conectividad policial (`salida/gamlp_seguridad_internet_modulos.csv`) y certificaciones catastrales (`salida/gamlp_certificaciones_catastro.csv`).

4. **`04_consolidar_matriz_u4ssc.py` (Matriz consolidada de indicadores U4SSC):**
   - Consolidación formal de los 8 indicadores del Desafío 1 con numeradores, denominadores, tasas, fuentes y brechas documentadas en `salida/matriz_indicadores_u4ssc_d1.csv`.
