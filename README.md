# Desafío 1: La Base Digital de una Ciudad que Funciona
**Datatón Urbana La Paz 2026 — Punto Cero**  
**Municipio:** Nuestra Señora de La Paz (Código INE: `020101`)  
**Nivel Oficial Alcanzado:** **Nivel 5 (Reutilizable)**  

---

## 📌 Resumen del Proyecto

Este repositorio contiene la entrega oficial del **Desafío 1**, enfocado en construir la **línea base verificable y el activo de datos de conectividad y capacidades digitales** para el Municipio de La Paz bajo el estándar internacional **U4SSC** (Recomendación UIT-T Y.4903).

### Resultados Clave
* **Acceso a Internet en Hogares (D1-01):** Creció de **22.26%** (Censo 2012, 50,375 hogares) a **89.84%** (Censo 2024, 225,388 hogares).
* **Banda Ancha Fija (D1-02):** **70.22%** de cobertura residencial (176,155 hogares).
* **Banda Ancha Inalámbrica (D1-03):** **78.06%** de hogares acceden con datos móviles.
* **Cobertura 3G/4G (D1-04):** **>95%** de la mancha urbana (>99% de la población).
* **Wi-Fi Público (D1-05):** **54 puntos** instalados (*Chukuta Online*).
* **Datos Abiertos (D1-06):** Inventario de **179 conjuntos de datos** abiertos del GAMLP.
* **Gobierno Electrónico (D1-07):** **15 trámites verificados** en `gob.bo` e iGOB 24/7.
* **Contratación Electrónica (D1-08):** **~91.56%** de procesos en SICOES con presentación digital.

---

## 📁 Estructura del Entregable

```text
├── README.md               # Este documento
├── autoria.yml             # Integrantes oficiales y consentimiento público
└── entrega/
    ├── ficha-equipo.yml    # Ficha del equipo y mapeo al Desafío D1
    ├── ficha-por-desafio.md # 8 Fichas técnicas U4SSC detalladas (D1-01 a D1-08)
    ├── datapackage.json    # Descriptor Frictionless Data Package v2
    ├── diccionario.csv     # 100% de columnas descritas (104 campos)
    ├── procedencia.md      # Trazabilidad y origen de fuentes (INE, GAMLP, ATT, AGETIC)
    ├── reglas-de-uso.md    # Licencias CC BY-SA 4.0 / ODbL
    ├── reglas-calidad.yml  # Reglas deterministas de validación
    ├── antes-despues.md    # Evolución cuantitativa: Nivel 1 -> Nivel 5 (+4 niveles)
    ├── pasos-manuales.md   # Guía paso a paso de reproducción
    ├── checksums.sha256    # Firmas criptográficas del activo
    ├── datos/              # Insumos locales del Municipio de La Paz (10.5 MB autónomos)
    ├── scripts/            # Pipeline determinista de procesamiento (01 a 04)
    └── salida/             # 18 tablas generadas en CSV UTF-8 + checksums.sha256
```

---

## ⚙️ Reproducción del Pipeline

Para reproducir deterministamente las 18 tablas de salida:
```bash
# Requiere Python >= 3.10 con duckdb y pandas
python entrega/scripts/01_limpiar_crudos.py
python entrega/scripts/02_procesar_censos_duckdb.py
python entrega/scripts/03_procesar_datos_abiertos.py
python entrega/scripts/04_consolidar_matriz_u4ssc.py
```

---

## 👥 Integrantes del Equipo

* **Fabian Juel Escalera Caballero** — [@Flerian-EC](https://github.com/Flerian-EC)
* **Andres Humberto Chirinos Lizondo** — [@andres-chirinos](https://github.com/andres-chirinos)
* **Adhemar Saul Gutierrez Zabaleta** — [@S4uL2001](https://github.com/S4uL2001)
