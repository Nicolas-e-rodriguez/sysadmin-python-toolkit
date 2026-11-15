import os

class DirectoryProvider:
    """
    Proveedor abstracto que maneja datos simulados (mock) 
    para desarrollo offline o pruebas locales de administración.
    """
    def __init__(self, mode="mock"):
        self.mode = mode
        # Datos de prueba simulando un Active Directory
        self._mock_db = [
            {"username": "nrodriguez", "cn": "Nicolás Rodríguez", "mail": "nicolas@dominio.local", "status": "Active", "dept": "SysAdmin"},
            {"username": "jperez", "cn": "Juan Pérez", "mail": "jperez@dominio.local", "status": "Locked", "dept": "Ventas"},
            {"username": "mgomez", "cn": "María Gómez", "mail": "mgomez@dominio.local", "status": "Active", "dept": "RRHH"},
            {"username": "cgomez", "cn": "Carlos Gómez", "mail": "cgomez@dominio.local", "status": "Disabled", "dept": "Infraestructura"}
        ]

    def search_users(self, query=""):
        """Busca usuarios de manera abstracta o contra el servidor real."""
        if self.mode == "mock":
            print(f"[MODO ABSTRACTO/MOCK] Buscando: '{query}'...")
            if not query:
                return self._mock_db
            # Filtra por nombre o usuario de forma flexible
            results = [
                u for u in self._mock_db 
                if query.lower() in u["username"].lower() or query.lower() in u["cn"].lower()
            ]
            return results
        else:
            # Aquí implementaremos la conexión real con ldap3 cuando estés en red
            raise NotImplementedError("El modo real contra Active Directory aún no está conectado en este módulo.")