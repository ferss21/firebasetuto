# firebase_init.py
"""
Módulo de inicialización de Firebase para los ejemplos en clase.

Este módulo expone dos funciones:

- get_db():      inicializa la app de Firebase (si no está inicializada)
                 y devuelve un cliente de Firestore.

- close_firebase(): cierra la app de Firebase (para que el script termine
                    limpio y libere recursos).

IMPORTANTE:
- Este módulo usa el archivo 'serviceAccountKey.json', que corresponde a la
  clave de cuenta de servicio descargada desde Firebase Console, en la sección
  "Cuentas de servicio".
- Ese archivo NO debe subirse a repositorios públicos.
"""

import firebase_admin
from firebase_admin import credentials, firestore


def get_db():
    """
    Inicializa la app de Firebase si aún no está inicializada
    y devuelve un cliente de Firestore.

    Si la app ya está inicializada, simplemente devuelve un cliente de Firestore.
    """
    if not firebase_admin._apps:
        # Carga las credenciales de la cuenta de servicio.
        # El archivo 'serviceAccountKey.json' debe estar en la carpeta raíz
        # del proyecto.
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

    # Retorna el cliente de Firestore.
    return firestore.client()


def close_firebase():
    """
    Cierra la app de Firebase si está inicializada.

    Esto ayuda a que cada script termine su ejecución correctamente
    (especialmente útil en entornos como PowerShell o VS Code),
    liberando conexiones y recursos.
    """
    if firebase_admin._apps:
        app = firebase_admin.get_app()
        firebase_admin.delete_app(app)



