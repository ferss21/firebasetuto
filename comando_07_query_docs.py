# comando_07_query_docs.py
"""
COMANDO 07 - Consultas (query) básicas en Firestore

Este script muestra cómo realizar una CONSULTA (query) sobre una colección
usando filtros simples.

En este ejemplo:
- Se usa la colección 'alumnos'.
- Se filtra por el campo 'activo' == True.
- Se limita el resultado a un máximo de 5 documentos.

IMPORTANTE:
- Esta versión está pensada para NO requerir índices compuestos adicionales,
  por lo que es más sencilla para demostración en clase.

Uso en consola (dentro de la carpeta del proyecto):
    py comando_07_query_docs.py

Sugerencia:
    Ejecutar antes varias veces 'comando_03_add_doc_autoid.py' para generar
    datos de prueba.
"""

from firebase_init import get_db, close_firebase
from google.api_core.exceptions import FailedPrecondition


def main():
    # Obtener el cliente de Firestore
    db = get_db()

    # Referencia a la colección 'alumnos'
    col_ref = db.collection("alumnos")

    # Consulta simple:
    # - Filtra por alumnos cuyo campo 'activo' sea True
    # - Limita el resultado a 5 documentos
    query = col_ref.where("activo", "==", True).limit(5)

    try:
        # Convertimos el iterador en lista para poder revisar si está vacío
        docs = list(query.stream())
    except FailedPrecondition as e:
        # Por si Firestore pidiera un índice, se captura la excepción
        print("⚠️ Firestore indica que esta consulta requiere un índice compuesto.")
        print("   Detalle técnico del error:")
        print(f"   {e}")
        return

    print("✅ Resultado de la consulta (alumnos activos, máximo 5):")

    if not docs:
        print(
            "⚠️ La consulta no devolvió documentos.\n"
            "   Sugerencia: ejecuta varias veces comando_03_add_doc_autoid.py "
            "para generar datos de prueba."
        )
        return

    # Recorremos los documentos y mostramos su contenido
    for doc in docs:
        print(f"- ID: {doc.id} → {doc.to_dict()}")


if __name__ == "__main__":
    try:
        main()
    finally:
        close_firebase()
        print("🔚 Script finalizado, puedes ejecutar otro comando.")