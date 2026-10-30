# Procedimiento de Ejecución y Pasos del Pipeline — Desafío 1

Esta entrega está totalmente automatizada mediante scripts de Python estructurados y reproducibles en `entrega/scripts/`.

Si se desea ejecutar el flujo paso a paso de forma manual o verificar la reproducibilidad, siga estas instrucciones:

---

## 1. Requisitos del Entorno
- Python 3.11+
- Paquetes requeridos: `duckdb`, `pandas`, `pyyaml`.

---

## 2. Ejecución Automatizada vía CLI del Datatón
Desde la raíz del repositorio, ejecute:
```bash
python -m dataton reproducir entrega --ejecutar
```
Este comando ejecuta todos los scripts de `entrega/scripts/` en una copia aislada y verifica que los hashes SHA-256 de los archivos en `entrega/salida/` coincidan exactamente con `entrega/salida/checksums.sha256`.

---

## 3. Ejecución Manual Paso a Paso de los Scripts

### Paso 1: Depuración de Archivos Crudos
```bash
cd entrega
python3 scripts/01_limpiar_crudos.py
```
- Lee los archivos crudos de `entrega/datos/`.
- Elimina separadores heterogéneos, espacios en blanco espurios y normaliza delimitadores de Ciudadanía Digital.
- Escribe las salidas saneadas en `entrega/salida/`.

### Paso 2: Procesamiento Censal con DuckDB
```bash
python3 scripts/02_procesar_censos_duckdb.py
```
- Lee con DuckDB los archivos Parquet particionados de La Paz en `datos/censo_2012_lapaz/MUN=020101/*/*.parquet`.
- Agrega los manzanos y comunidades rurales para obtener la población, viviendas particulares ocupadas y hogares con internet para 2012 y 2024.
- Genera `entrega/salida/censo_conectividad_lapaz.csv`.

### Paso 3: Auditoría de Datos Abiertos y Trámites
```bash
python3 scripts/03_procesar_datos_abiertos.py
```
- Analiza `datos/gamlp_datos_abiertos/indice.parquet` y extrae el catálogo de 179 datasets del GAMLP en `entrega/salida/gamlp_datos_abiertos_inventario.csv`.
- Normaliza los 15 trámites verificados en línea del GAMLP en `entrega/salida/gamlp_tramites_verificados.csv`.
- Extrae la serie de seguridad ciudadana e internet y trámites catastrales.

### Paso 4: Consolidación de la Matriz U4SSC
```bash
python3 scripts/04_consolidar_matriz_u4ssc.py
```
- Genera la matriz comparativa de los 8 indicadores del Desafío 1 con sus numeradores, denominadores, unidades, fuentes y estado de madurez en `entrega/salida/matriz_indicadores_u4ssc_d1.csv`.

### Paso 5: Regeneración de Sumas SHA-256
```bash
python -m dataton sumas entrega/salida
```
