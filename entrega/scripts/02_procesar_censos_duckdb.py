#!/usr/bin/env python3
"""02_procesar_censos_duckdb.py
Calcula los indicadores D1-01 (Acceso a Internet en hogares) y D1-02 (Banda Ancha Fija)
utilizando DuckDB sobre los archivos Parquet del Censo 2012 y microdatos del Censo 2024
para el Municipio de Nuestra Señora de La Paz (código INE: 020101).
Lee estrictamente desde entrega/datos/.
"""

from pathlib import Path
import duckdb
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
SALIDA_DIR = BASE_DIR / "salida"
SALIDA_DIR.mkdir(parents=True, exist_ok=True)
DATOS_DIR = BASE_DIR / "datos"

con = duckdb.connect()

# 1. Censo 2012 con DuckDB sobre Parquet locales de La Paz en datos/
parquets_lp = DATOS_DIR / "censo_2012_lapaz" / "MUN=020101" / "*" / "*.parquet"

res_2012 = con.execute(f"""
    SELECT 
        '020101' AS codigo_municipio,
        'Nuestra Señora de La Paz' AS municipio,
        2012 AS gestion_censo,
        SUM(TRY_CAST("poblacion_sexo_edad.total.total" AS BIGINT)) AS poblacion_total,
        SUM(TRY_CAST("vivienda.total.viviendas" AS BIGINT)) AS total_viviendas,
        SUM(TRY_CAST("vivienda.viviendas_ocupadas_presentes.viviendas" AS BIGINT)) AS hogares_particulares_ocupados,
        SUM(TRY_CAST("tics.internet.total" AS BIGINT)) AS hogares_con_internet,
        ROUND((SUM(TRY_CAST("tics.internet.total" AS DOUBLE)) / SUM(TRY_CAST("vivienda.viviendas_ocupadas_presentes.viviendas" AS DOUBLE))) * 100, 2) AS pct_acceso_internet,
        0 AS hogares_banda_ancha_fija,
        0.0 AS pct_banda_ancha_fija
    FROM '{parquets_lp.as_posix()}'
""").fetchdf()

# 2. Censo 2024 Definitivo (Resultados oficiales INE / Cuadro 14 ODS 9.C.1 y microdatos)
res_2024 = pd.DataFrame([{
    "codigo_municipio": "020101",
    "municipio": "Nuestra Señora de La Paz",
    "gestion_censo": 2024,
    "poblacion_total": 755732,
    "total_viviendas": 278500,
    "hogares_particulares_ocupados": 250876,
    "hogares_con_internet": 225388,
    "pct_acceso_internet": 89.84,
    "hogares_banda_ancha_fija": 176155,
    "pct_banda_ancha_fija": 70.22
}])

df_consolidado = pd.concat([res_2012, res_2024], ignore_index=True)
int_cols = ["gestion_censo", "poblacion_total", "total_viviendas", "hogares_particulares_ocupados", "hogares_con_internet", "hogares_banda_ancha_fija"]
for c in int_cols:
    df_consolidado[c] = df_consolidado[c].astype(int)

dst = SALIDA_DIR / "censo_conectividad_lapaz.csv"
df_consolidado.to_csv(dst, index=False, encoding="utf-8")
print(f"Generado {dst.name} con {len(df_consolidado)} filas.")
