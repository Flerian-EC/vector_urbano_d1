#!/usr/bin/env python3
"""04_consolidar_matriz_u4ssc.py
Consolida la matriz oficial de medición de los 8 Indicadores SMART del Desafío 1:
"La base digital de una ciudad que funciona" (Recomendación UIT-T Y.4903 U4SSC)
para el Municipio de Nuestra Señora de La Paz (código INE: 020101).
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
SALIDA_DIR = BASE_DIR / "salida"
SALIDA_DIR.mkdir(parents=True, exist_ok=True)

indicadores_d1 = [
    {
        "id_indicador": "D1-01",
        "codigo_u4ssc": "EC:ICT:ICT:1C",
        "nombre_indicador": "Acceso a Internet en los hogares",
        "dimension_u4ssc": "Economía / Infraestructura TIC",
        "tipo_indicador": "Core",
        "gestion_periodo": "2024 (Línea Base Censal: 2012)",
        "numerador_descripcion": "Hogares particulares con acceso a Internet (fijo o móvil)",
        "numerador_valor": 225388,
        "denominador_descripcion": "Total hogares particulares ocupados con personas presentes",
        "denominador_valor": 250876,
        "metrica_resultado": "89.84% (vs 22.26% en Censo 2012)",
        "unidad_medida": "Porcentaje (%)",
        "fuente_primaria": "INE (Censo de Población y Vivienda 2024 / CPV 2012)",
        "responsable_dato": "Instituto Nacional de Estadística (INE) / SMCI GAMLP",
        "estado_madurez": "Calculado Oficial",
        "brecha_identificada": "Resuelta a nivel municipal; pendiente publicación definitiva de microdatos georreferenciados a nivel de manzano 2024 por el INE."
    },
    {
        "id_indicador": "D1-02",
        "codigo_u4ssc": "EC:ICT:ICT:2C",
        "nombre_indicador": "Suscripciones de banda ancha fija",
        "dimension_u4ssc": "Economía / Infraestructura TIC",
        "tipo_indicador": "Core",
        "gestion_periodo": "2024 (Conexiones ATT: Junio 2026)",
        "numerador_descripcion": "Hogares particulares con servicio de Internet fijo en la vivienda",
        "numerador_valor": 176155,
        "denominador_descripcion": "Total hogares particulares ocupados en el municipio",
        "denominador_valor": 250876,
        "metrica_resultado": "70.22% (Residencial)",
        "unidad_medida": "Porcentaje (%)",
        "fuente_primaria": "INE CPV 2024 (variable V19E_INETFIJO) / ATT",
        "responsable_dato": "Autoridad de Regulación y Fiscalización de Telecomunicaciones y Transportes (ATT) / INE",
        "estado_madurez": "Calculado Oficial Residencial",
        "brecha_identificada": "La ATT reporta suscripciones comerciales/residenciales consolidadas a nivel departamental (417,091 líneas a junio 2026), sin desagregación a nivel del municipio 020101."
    },
    {
        "id_indicador": "D1-03",
        "codigo_u4ssc": "EC:ICT:ICT:3C",
        "nombre_indicador": "Suscripciones de banda ancha inalámbrica",
        "dimension_u4ssc": "Economía / Infraestructura TIC",
        "tipo_indicador": "Core",
        "gestion_periodo": "2024 / Junio 2026",
        "numerador_descripcion": "Suscripciones activas de banda ancha móvil en el municipio (Censal: Hogares con datos móviles)",
        "numerador_valor": 195844,
        "denominador_descripcion": "Población total del municipio (Censal: Total hogares ocupados)",
        "denominador_valor": 250876,
        "metrica_resultado": "78.06% hogares (Líneas Depto ATT: 3,927,337)",
        "unidad_medida": "Porcentaje hogares / Tasa por 100k hab.",
        "fuente_primaria": "INE CPV 2024 (variable V19F_INETMOVIL) / ATT Boletines 2026",
        "responsable_dato": "ATT / Operadores Móviles (Entel, Tigo, Viva)",
        "estado_madurez": "Documentado con Brecha de Radicación",
        "brecha_identificada": "Brecha de territorialización: las líneas SIM prepago/postpago se registran en la ATT por departamento de adquisición contractual y no por residencia municipal del abonado."
    },
    {
        "id_indicador": "D1-04",
        "codigo_u4ssc": "EC:ICT:ICT:4C",
        "nombre_indicador": "Cobertura de banda ancha inalámbrica",
        "dimension_u4ssc": "Economía / Infraestructura TIC",
        "tipo_indicador": "Core",
        "gestion_periodo": "2024–2026",
        "numerador_descripcion": "Superficie municipal urbana cubierta por huella de radiobases 3G/4G/LTE",
        "numerador_valor": 180,
        "denominador_descripcion": "Área de mancha urbana consolidada del municipio (km²)",
        "denominador_valor": 185,
        "metrica_resultado": ">95% en mancha urbana (>99% de población cubierta)",
        "unidad_medida": "Porcentaje de área / población (%)",
        "fuente_primaria": "ATT / Mapas de cobertura de operadores móviles",
        "responsable_dato": "ATT / Dirección de Tecnologías GAMLP",
        "estado_madurez": "Documentado con Brecha Geoespacial",
        "brecha_identificada": "Brecha geoespacial: ausencia de capas poligonales shapefile/GeoJSON públicas de la huella RF de celdas 4G/5G para cálculo formal de intersección con el límite municipal."
    },
    {
        "id_indicador": "D1-05",
        "codigo_u4ssc": "EC:ICT:ICT:5C",
        "nombre_indicador": "Disponibilidad de Wi-Fi en áreas públicas",
        "dimension_u4ssc": "Economía / Infraestructura TIC",
        "tipo_indicador": "Core",
        "gestion_periodo": "2024–2026",
        "numerador_descripcion": "Número total de puntos de acceso Wi-Fi gratuitos instalados por el municipio en plazas y áreas públicas",
        "numerador_valor": 54,
        "denominador_descripcion": "No aplica (métrica de conteo absoluto N)",
        "denominador_valor": 1,
        "metrica_resultado": "N = 54 puntos públicos",
        "unidad_medida": "Conteo absoluto (N)",
        "fuente_primaria": "Programa Chukuta Online / SMCI GAMLP",
        "responsable_dato": "Secretaría Municipal de Ciudad Inteligente (SMCI) - GAMLP",
        "estado_madurez": "Documentado con Brecha de Monitoreo",
        "brecha_identificada": "Brecha operativa: falta de telemetría pública en tiempo real (uptime/ping/ancho de banda) para certificar qué porcentaje de puntos instalados se encuentran efectivamente en servicio."
    },
    {
        "id_indicador": "D1-06",
        "codigo_u4ssc": "EC:ICT:PS:1A",
        "nombre_indicador": "Datos abiertos",
        "dimension_u4ssc": "Sector Público",
        "tipo_indicador": "Advanced",
        "gestion_periodo": "2025–2026",
        "numerador_descripcion": "Total de conjuntos de datos publicados en formatos abiertos y legibles por máquina por el GAMLP",
        "numerador_valor": 179,
        "denominador_descripcion": "Inventario total de bases de datos y registros administrativos del GAMLP",
        "denominador_valor": 0,
        "metrica_resultado": "N = 179 datasets (48 dependencias municipales)",
        "unidad_medida": "Conteo absoluto (N) / Porcentaje (%)",
        "fuente_primaria": "Portal de Datos Abiertos del GAMLP (datosabiertos.lapaz.bo)",
        "responsable_dato": "Dirección de Innovación y Ciudad Inteligente (DICI) - GAMLP",
        "estado_madurez": "Calculado Oficial (Numerador N)",
        "brecha_identificada": "Brecha metodológica de denominador: el GAMLP no posee un inventario consolidado formal del 100% de las bases de datos transaccionales existentes en sus secretarías."
    },
    {
        "id_indicador": "D1-07",
        "codigo_u4ssc": "EC:ICT:PS:2A",
        "nombre_indicador": "Gobierno electrónico",
        "dimension_u4ssc": "Sector Público",
        "tipo_indicador": "Advanced",
        "gestion_periodo": "2025–2026",
        "numerador_descripcion": "Número de trámites y servicios municipales transaccionales en línea",
        "numerador_valor": 15,
        "denominador_descripcion": "Catálogo total de trámites y servicios administrados por el GAMLP (estimado Guía de Trámites)",
        "denominador_valor": 120,
        "metrica_resultado": "15 trámites verificados en gob.bo (12.5% de catálogo base)",
        "unidad_medida": "Conteo absoluto (N) / Porcentaje (%)",
        "fuente_primaria": "Plataforma iGOB 24/7 (GAMLP) / Directorio de Trámites del Estado (gob.bo)",
        "responsable_dato": "Unidad de Innovación y Transformación Digital (UITD) - GAMLP / AGETIC",
        "estado_madurez": "Calculado Parcial con Brecha de Clasificación",
        "brecha_identificada": "Falta de estandarización en la Guía de Trámites municipal para distinguir trámites 100% transaccionales digitales de servicios presenciales con mera reserva de citas."
    },
    {
        "id_indicador": "D1-08",
        "codigo_u4ssc": "EC:ICT:PS:3A",
        "nombre_indicador": "Contratación electrónica del sector público",
        "dimension_u4ssc": "Sector Público",
        "tipo_indicador": "Advanced",
        "gestion_periodo": "2024–2025",
        "numerador_descripcion": "Procesos de contratación pública del GAMLP adjudicados mediante presentación electrónica de propuestas",
        "numerador_valor": 412,
        "denominador_descripcion": "Total de procesos de contratación pública convocados por el GAMLP",
        "denominador_valor": 450,
        "metrica_resultado": "91.56% de procesos con recepción electrónica",
        "unidad_medida": "Porcentaje (%)",
        "fuente_primaria": "Sistema de Contrataciones Estatales (SICOES) / Subasta Electrónica",
        "responsable_dato": "Dirección de Contrataciones (DCON) - GAMLP / Ministerio de Economía",
        "estado_madurez": "Calculado Preliminar con Brecha Transaccional",
        "brecha_identificada": "Requiere consolidar los códigos CUCE del GAMLP en SICOES para discriminar contratos de obras mayores de compras menores por caja chica."
    }
]

df_matriz = pd.DataFrame(indicadores_d1)
dst = SALIDA_DIR / "matriz_indicadores_u4ssc_d1.csv"
df_matriz.to_csv(dst, index=False, encoding="utf-8")
print(f"Generado {dst.name} con {len(df_matriz)} filas.")
