# comando_05_update_doc.py
"""
COMANDO 05 - update() de un documento

Este script muestra cómo ACTUALIZAR únicamente algunos campos
de un documento usando el método update().

Diferencia principal:
- set():   reemplaza TODO el documento (a menos que se use merge).
- update(): solo modifica los campos indicados, y falla si el documento
            no existe.

En este ejemplo:
- Se actualiza el documento 'demo1' de la colección 'alumnos'.
- Se cambian los campos 'curso' y 'activo'.

Uso en consola:
    py .\comando_05_update_doc.py
"""

from firebase_init import get_db, close_firebase
from google.api_core.exceptions import NotFound


def main():
    # Obtener el cliente de Firestore
    db = get_db()

    # Referencia al documento 'demo1'
    doc_ref = db.collection("alumnos").document("demo1")

    try:
        # update() modifica únicamente los campos indicados
        doc_ref.update(
            {
                "curso": "Firebase con Python (actualizado)",
                "activo": True,
            }
        )
        print("✅ Documento 'demo1' actualizado correctamente.")
    except NotFound:
        # Si el documento no existe, update() lanza una excepción
        print(
            "⚠️ No existe el documento 'demo1', no se pudo actualizar.\n"
            "   Sugerencia: ejecuta primero comando_01_set_doc.py"
        )


if __name__ == "__main__":
    try:
        main()
    finally:
        close_firebase()
        print("🔚 Script finalizado, puedes ejecutar otro comando.")
