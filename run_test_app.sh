#!/bin/bash
cd "$(dirname "$0")"  # Cambia al directorio del script
source venv/bin/activate  # Activa el entorno virtual
python simple_test.py  # Ejecuta el script principal de tu aplicación
