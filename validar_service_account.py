# validar_firebase_config.py
"""
Valida que el archivo firebaseConfig.json:
- Existe en el directorio actual.
- Es JSON válido.
- Tiene las claves típicas del config web de Firebase:
  apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId.
"""

import json
import os
import sys
from json.decoder import JSONDecodeError

CONFIG_FILE = "firebaseConfig.json"


def main():
    # 1. Verificar existencia del archivo
    if not os.path.isfile(CONFIG_FILE):
        print(f"❌ No se encontró el archivo '{CONFIG_FILE}' "
              f"en el directorio actual.")
        print("   Asegúrate de haber copiado el config web de Firebase "
              "y guardado con ese nombre.")
        sys.exit(1)

    print(f"📄 Archivo '{CONFIG_FILE}' encontrado.")

    # 2. Leer el JSON
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except JSONDecodeError as e:
        print("❌ El archivo existe, pero NO es JSON válido.")
        print(f"   Detalle del error: {e}")
        sys.exit(1)

    print("✅ El archivo es JSON válido.")

    # 3. Validar claves mínimas del config web
    required_keys = [
        "apiKey",
        "authDomain",
        "projectId",
        "storageBucket",
        "messagingSenderId",
        "appId",
    ]

    missing_keys = [k for k in required_keys if k not in data]

    if missing_keys:
        print("❌ El JSON no tiene todas las claves requeridas para el config web.")
        print("   Faltan estas claves:", ", ".join(missing_keys))
        sys.exit(1)

    # 4. Mostrar info básica
    print("✅ Todas las claves requeridas están presentes.")
    print(f"🆔 projectId: {data.get('projectId')}")
    print(f"📦 storageBucket: {data.get('storageBucket')}")
    print(f"📧 authDomain: {data.get('authDomain')}")

    print("\n🎉 Todo OK: tu firebaseConfig.json coincide con el formato "
          "que entrega Firebase para proyectos web.")


if __name__ == "__main__":
    main()

