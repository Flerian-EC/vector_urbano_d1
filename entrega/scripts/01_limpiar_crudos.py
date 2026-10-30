#!/usr/bin/env python3
"""01_limpiar_crudos.py
Depura los archivos crudos del paquete D1 resolviendo las observaciones de problemas-observados.md:
1. Normaliza separadores a coma en UTF-8.
2. Limpia espacios en blanco, comas de miles y filas vacías en líneas telefónicas.
3. Estandariza delimitadores (| a ,) y nulos en series de Ciudadanía Digital.
4. Genera versiones saneadas listas para interoperabilidad en salida/.
"""

import os
import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_DIR = BASE_DIR / "datos"
SALIDA_DIR = BASE_DIR / "salida"
SALIDA_DIR.mkdir(parents=True, exist_ok=True)

def depurar_lineas_telefonicas():
    src = DATOS_DIR / "distribucion-de-lineas-telefonicas-fijas-en-servicio.csv"
    dst = SALIDA_DIR / "lineas_telefonicas_fijas_depurado.csv"

    with open(src, "r", encoding="utf-8", errors="replace") as fh:
        raw_lines = fh.readlines()

    cleaned_rows = []
    for line in raw_lines:
        line_str = line.strip()
        if not line_str:
            continue
        parts = [p.strip() for p in line.split("\t")]
        if not any(parts):
            continue
        # Limpiar números con comas de miles o espacios
        cleaned_parts = []
        for p in parts:
            clean_num = p.replace(" ", "").replace(",", "")
            if clean_num.isdigit():
                cleaned_parts.append(clean_num)
            else:
                cleaned_parts.append(p)
        cleaned_rows.append(cleaned_parts)

    with open(dst, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(cleaned_rows)
    print(f"Generado {dst.name} con {len(cleaned_rows)} filas.")

def depurar_kioscos():
    src = DATOS_DIR / "localidades_kioscos_electronicos_2020.csv"
    dst = SALIDA_DIR / "kioscos_electronicos_depurado.csv"
    with open(src, "r", encoding="utf-8", errors="replace") as fh:
        reader = csv.reader(fh)
        rows = [[col.strip() for col in row] for row in reader if any(row)]
    with open(dst, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(rows)
    print(f"Generado {dst.name} con {len(rows)} filas.")

def depurar_fibra_optica():
    src = DATOS_DIR / "localidades_fo_2020.csv"
    dst = SALIDA_DIR / "fibra_optica_depurado.csv"
    with open(src, "r", encoding="utf-8", errors="replace") as fh:
        reader = csv.reader(fh)
        rows = [[col.strip() for col in row] for row in reader if any(row)]
    with open(dst, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(rows)
    print(f"Generado {dst.name} con {len(rows)} filas.")

def depurar_ciudadania_digital():
    cd_dir = DATOS_DIR / "ciudadania-digital"
    if not cd_dir.is_dir():
        return
    for item in sorted(cd_dir.glob("*.csv")):
        dst = SALIDA_DIR / f"cd_{item.name}"
        with open(item, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        delimiter = "|" if "|" in text.splitlines()[0] else ","
        fh_read = text.splitlines()
        reader = csv.reader(fh_read, delimiter=delimiter)
        rows = []
        for r in reader:
            if not r or not any(r):
                continue
            cleaned = [c.strip() if c.strip() else "SIN_DATO" for c in r]
            rows.append(cleaned)
        with open(dst, "w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerows(rows)
        print(f"Generado {dst.name} con {len(rows)} filas.")

if __name__ == "__main__":
    depurar_lineas_telefonicas()
    depurar_kioscos()
    depurar_fibra_optica()
    depurar_ciudadania_digital()
    print("01_limpiar_crudos completado con éxito.")
