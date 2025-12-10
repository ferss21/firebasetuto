# comando_04_get_doc.py
"""
COMANDO 04 - get() de un documento

Este script muestra cómo LEER un documento específico
a partir de su ID, utilizando el método get().

En este ejemplo:
- Se intenta leer el documento 'demo1' de la colección 'alumnos'.
- Si existe, se imprimen sus datos.
- Si no existe, se muestra un mensaje de advertencia.

Uso en consola (dentro de la carpeta del proyecto):
    py comando_04_get_doc.py

Recomendación:
    Primero ejecutar comando_01_set_doc.py para asegurarse de que
    el documento 'demo1' exista.
"""

from firebase_init import get_db, close_firebase


def main():
    # Obtener el cliente de Firestore
    db = get_db()

    # Referencia al documento 'demo1' en la colección 'alumnos'
    doc_ref = db.collection("alumnos").document("demo1")

    # get() trae una "instantánea" (snapshot) del documento
    doc = doc_ref.get()

    if doc.exists:
        print("✅ Documento encontrado:")
        print(f"   ID: {doc.id}")
        print("   Datos:", doc.to_dict())
    else:
        print(
            "⚠️ El documento 'demo1' no existe.\n"
            "   Sugerencia: ejecuta primero comando_01_set_doc.py"
        )


if __name__ == "__main__":
    try:
        main()
    finally:
        close_firebase()
        print("🔚 Script finalizado, puedes ejecutar otro comando.")
