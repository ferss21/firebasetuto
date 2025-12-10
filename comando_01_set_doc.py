# comando_01_set_doc.py
"""
COMANDO 01 - set()

Este script muestra cómo CREAR o REESCRIBIR un documento específico
en Firestore utilizando el método set().

Características:
- Usa la colección 'alumnos'.
- Crea (o reemplaza) el documento con ID 'demo1'.
- Establece varios campos: nombre, curso, activo, creadoEn.

Uso en consola (desde la carpeta del proyecto):
    py .\comando_01_set_doc.py
"""

from firebase_init import get_db, close_firebase
from firebase_admin import firestore


def main():
    # Obtener el cliente de Firestore
    db = get_db()

    # Referencia a un documento con ID fijo: 'demo1'
    doc_ref = db.collection("alumnos").document("demo1")

    # set() crea el documento si no existe
    # o lo SOBREESCRIBE por completo si ya existe.
    doc_ref.set(
        {
            "nombre": "Marlaneth",
            "curso": "Firebase con Python",
            "activo": True,
            # SERVER_TIMESTAMP guarda la fecha/hora del servidor de Firebase
            "creadoEn": firestore.SERVER_TIMESTAMP,
        }
    )

    print("✅ Documento 'demo1' creado/reescrito en la colección 'alumnos'.")


if __name__ == "__main__":
    try:
        main()
    finally:
        # Cierra la app de Firebase para liberar recursos.
        close_firebase()
        print("🔚 Script finalizado, puedes ejecutar otro comando.")
