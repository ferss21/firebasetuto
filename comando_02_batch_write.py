# comando_02_batch_write.py
"""
COMANDO 02 - Batch Write (escrituras en lote)

Este script muestra cómo usar un "batch":
    - Permite agrupar varias operaciones de escritura en una sola llamada
      a Firestore.
    - Todas las operaciones del batch se confirman juntas.

En este ejemplo:
- Se crean 3 documentos en la colección 'alumnos':
  'batch_demo_1', 'batch_demo_2' y 'batch_demo_3'.

Uso en consola (dentro de la carpeta del proyecto):
    py comando_02_batch_write.py
"""

from firebase_init import get_db, close_firebase
from firebase_admin import firestore


def main():
    # Obtener el cliente de Firestore
    db = get_db()

    # Crear el objeto batch
    batch = db.batch()

    # Referencia a la colección 'alumnos'
    col_ref = db.collection("alumnos")

    # Agregamos 3 operaciones al batch
    for i in range(1, 4):
        # Documento con ID fijo para el ejemplo
        doc_ref = col_ref.document(f"batch_demo_{i}")
        batch.set(
            doc_ref,
            {
                "nombre": f"Alumno batch {i}",
                "curso": "Batch write demo",
                "activo": True,
                "indice": i,
                "creadoEn": firestore.SERVER_TIMESTAMP,
            },
        )

    # Ejecutar el batch: todas las operaciones se envían juntas
    results = batch.commit()

    print("✅ Batch write ejecutado correctamente.")
    print("   Cantidad de operaciones confirmadas:", len(results))


if __name__ == "__main__":
    try:
        main()
    finally:
        close_firebase()
        print("🔚 Script finalizado, puedes ejecutar otro comando.")

