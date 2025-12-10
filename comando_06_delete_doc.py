# comando_06_delete_doc.py
"""
COMANDO 06 - delete() de un documento

Este script muestra cómo ELIMINAR un documento de Firestore
usando el método delete().

En este ejemplo:
- Se intenta eliminar el documento 'demo1' de la colección 'alumnos'.

Uso en consola:
    py .\comando_06_delete_doc.py
"""

from firebase_init import get_db, close_firebase


def main():
    # Obtener el cliente de Firestore
    db = get_db()

    # Referencia al documento 'demo1'
    doc_ref = db.collection("alumnos").document("demo1")

    # delete() devuelve información sobre la operación (hora de actualización)
    result = doc_ref.delete()

    print("✅ Solicitud de eliminación enviada para 'demo1'.")
    print("   Info devuelta por Firestore:", result)


if __name__ == "__main__":
    try:
        main()
    finally:
        close_firebase()
        print("🔚 Script finalizado, puedes ejecutar otro comando.")
