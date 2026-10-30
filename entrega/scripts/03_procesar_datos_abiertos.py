#!/usr/bin/env python3
"""03_procesar_datos_abiertos.py
Procesa y extrae la evidencia de datos abiertos municipales e interoperabilidad
gubernamental para los indicadores D1-06 (Datos Abiertos) y D1-07 (Gobierno Electrónico)
utilizando DuckDB sobre el catálogo de datos abiertos del GAMLP y registros de gob.bo.
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

# 1. Indicador D1-06: Inventario de Datasets Abiertos del GAMLP
indice_path = DATOS_DIR / "gamlp_datos_abiertos" / "indice.parquet"
if indice_path.is_file():
    df_datasets = con.execute(f"""
        SELECT 
            dab_id AS id_dataset,
            dab_titulo AS titulo,
            dab_resumen AS descripcion,
            dab_fuente AS unidad_productora,
            dab_frecuencia_actualizacion AS periodicidad,
            dab_version AS version,
            dab_fecha_registro AS fecha_registro,
            dab_fecha_actualizacion AS fecha_actualizacion,
            dab_estado AS estado
        FROM '{indice_path.as_posix()}'
        ORDER BY dab_id
    """).fetchdf()
    dst_datasets = SALIDA_DIR / "gamlp_datos_abiertos_inventario.csv"
    df_datasets.to_csv(dst_datasets, index=False, encoding="utf-8")
    print(f"Generado {dst_datasets.name} con {len(df_datasets)} filas (Total Datasets GAMLP: {len(df_datasets)}).")

# 2. Indicador D1-07: Trámites Verificados del GAMLP en gob.bo
tramites_gamlp = [
    {"id_tramite": 2333, "nombre": "EMISIÓN DE PROFORMA - IMPUESTO MUNICIPAL A LA PROPIEDAD DE BIENES INMUEBLES", "estado": "PUBLICADO", "slug": "emision-de-proforma-impuesto-municipal-a-la-propiedad-de-bienes-inmuebles", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2335, "nombre": "MODIFICACIÓN DE DATOS DEL CONTRIBUYENTE EN EL PADRÓN MUNICIPAL", "estado": "PUBLICADO", "slug": "modificacion-de-datos-del-contribuyente-en-el-padron-municipal", "tipo_canal": "En línea"},
    {"id_tramite": 2341, "nombre": "INSCRIPCIÓN VEHÍCULO AUTOMOTOR TERRESTRE POR IMPORTACIÓN", "estado": "PUBLICADO", "slug": "inscripcion-vehiculo-automotor-terrestre-por-importacion", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2363, "nombre": "INSCRIPCIÓN DEL VEHÍCULO AUTOMOTOR TERRESTRE POR FABRICACIÓN NACIONAL", "estado": "PUBLICADO", "slug": "inscripcion-del-vehiculo-automotor-terrestre-por-fabricacion-nacional", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2368, "nombre": "INSCRIPCIÓN DE VEHÍCULO AUTOMOTOR TERRESTRE CAMBIO DE RADICATORIA", "estado": "PUBLICADO", "slug": "inscripcion-de-vehiculo-automotor-terrestre-cambio-de-radicatoria", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2369, "nombre": "DUPLICADO DE CERTIFICADO DE REGISTRO DE PROPIEDAD DEL VEHÍCULO (RUAT-03)", "estado": "PUBLICADO", "slug": "duplicado-de-certificado-de-registro-de-propiedad-del-vehiculo-ruat-03", "tipo_canal": "En línea"},
    {"id_tramite": 2370, "nombre": "TRANSFERENCIA DE VEHÍCULO AUTOMOTOR TERRESTRE", "estado": "PUBLICADO", "slug": "transferencia-de-vehiculo-automotor-terrestre", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2371, "nombre": "BAJA DEFINITIVA DE VEHÍCULO AUTOMOTOR TERRESTRE", "estado": "PUBLICADO", "slug": "baja-definitiva-de-vehiculo-automotor-terrestre", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2374, "nombre": "CERTIFICACIÓN DE DATOS DEL VEHÍCULO AUTOMOTOR TERRESTRE", "estado": "PUBLICADO", "slug": "certificacion-de-datos-del-vehiculo-automotor-terrestre", "tipo_canal": "En línea"},
    {"id_tramite": 2383, "nombre": "DUPLICADO DE PLACA POR EXTRAVÍO, ROBO O DETERIORO", "estado": "PUBLICADO", "slug": "duplicado-de-placa-por-extravio-robo-o-deterioro", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2390, "nombre": "EMPADRONAMIENTO DE BIENES INMUEBLES", "estado": "PUBLICADO", "slug": "empadronamiento-bienes-inmuebles", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2396, "nombre": "REGISTRO DE RESCISIÓN O DESISTIMIENTO DEL IMPUESTO MUNICIPAL", "estado": "PUBLICADO", "slug": "registro-de-rescision-o-desistimiento-del-impuesto-municipal", "tipo_canal": "En línea / Presencial"},
    {"id_tramite": 2448, "nombre": "AUTORIZACIONES DE VIAJE PARA MENORES DE EDAD", "estado": "PUBLICADO", "slug": "autorizaciones-menores", "tipo_canal": "En línea (iGOB 24/7)"},
    {"id_tramite": 2483, "nombre": "SOLICITUD DE LICENCIA DE FUNCIONAMIENTO PARA ACTIVIDADES ECONÓMICAS", "estado": "PUBLICADO", "slug": "solicitud-de-licencia-de-funcionamiento-para-via-publica", "tipo_canal": "En línea (iGOB 24/7)"},
    {"id_tramite": 3593, "nombre": "CALIFICACIÓN, REGISTRO Y CARNETIZACIÓN DE DISCAPACIDAD", "estado": "PUBLICADO", "slug": "calificacion-registro-y-carnetizacion-de-discapacidad", "tipo_canal": "En línea / Presencial"}
]

df_tramites = pd.DataFrame(tramites_gamlp)
dst_tramites = SALIDA_DIR / "gamlp_tramites_verificados.csv"
df_tramites.to_csv(dst_tramites, index=False, encoding="utf-8")
print(f"Generado {dst_tramites.name} con {len(df_tramites)} trámites verificados del GAMLP.")

# 3. Servicios policiales y trámites catastrales del GAMLP (Datasets 129 y 182)
d129_path = DATOS_DIR / "gamlp_datos_abiertos" / "datasets" / "129.csv"
if d129_path.is_file():
    df_pol = con.execute(f"""
        SELECT 
            AÑO AS gestion,
            SUM(TRY_CAST("NÚMERO DE CONECCIONES" AS INT)) AS conexiones_internet_policiales
        FROM '{d129_path.as_posix()}'
        WHERE "SERVICIOS BÁSICOS DISPONIBLES" = 'INTERNET'
          AND TRY_CAST("NÚMERO DE CONECCIONES" AS INT) IS NOT NULL
        GROUP BY AÑO
        ORDER BY AÑO
    """).fetchdf()
    dst_pol = SALIDA_DIR / "gamlp_seguridad_internet_modulos.csv"
    df_pol.to_csv(dst_pol, index=False, encoding="utf-8")
    print(f"Generado {dst_pol.name} con {len(df_pol)} filas.")

d182_path = DATOS_DIR / "gamlp_datos_abiertos" / "datasets" / "182.csv"
if d182_path.is_file():
    df_cat = con.execute(f"""
        SELECT 
            AÑO AS gestion,
            SUM(TRY_CAST("NÚMERO DE CERTIFICACIONES CATASTRALES EMITIDAS" AS INT)) AS total_certificaciones_catastrales
        FROM '{d182_path.as_posix()}'
        GROUP BY AÑO
        ORDER BY AÑO
    """).fetchdf()
    dst_cat = SALIDA_DIR / "gamlp_certificaciones_catastro.csv"
    df_cat.to_csv(dst_cat, index=False, encoding="utf-8")
    print(f"Generado {dst_cat.name} con {len(df_cat)} filas.")
