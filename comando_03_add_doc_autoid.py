# comando_03_add_doc_autoid.py
"""
COMANDO 03 - Documento con ID automático

Este script muestra cómo crear un documento en Firestore
dejando que Firestore genere el ID automáticamente.

En este ejemplo:
- Se usa la colección 'alumnos'.
- El ID se genera de forma aleatoria.
- Se guardan campos como nombre, curso, activo, puntaje y creadoEn.

Uso en consola (dentro de la carpeta del proyecto):
    py comando_03_add_doc_autoid.py
"""

from firebase_init import get_db, close_firebase
from firebase_admin import firestore
import random


def main():
    # Obtener el cliente de Firestore
    db = get_db()

    # Referencia a la colección 'alumnos'
    col_ref = db.collection("alumnos")

    # Datos de ejemplo, con valores aleatorios para probar
    data = {
        "nombre": f"Alumno {random.randint(1, 999)}",
        "curso": "Curso prueba add (autoid)",
        "activo": random.choice([True, False]),
        "puntaje": random.randint(0, 100),
        "creadoEn": firestore.SERVER_TIMESTAMP,
    }

    # doc() sin pasar ID → Firestore genera un ID único automáticamente
    doc_ref = col_ref.document()
    doc_ref.set(data)

    print("✅ Documento creado con ID automático:")
    print(f"   ID: {doc_ref.id}")


if __name__ == "__main__":
    try:
        main()
    finally:
        close_firebase()
        print("🔚 Script finalizado, puedes ejecutar otro comando.")
