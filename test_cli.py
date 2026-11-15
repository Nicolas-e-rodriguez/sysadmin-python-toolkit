from core.providers import DirectoryProvider

# Inicializamos el proveedor en modo mock (abstracto)
provider = DirectoryProvider(mode="mock")

print("--- PRUEBA 1: Listar todos los usuarios simulados ---")
todos = provider.search_users()
for u in todos:
    print(f"Usuario: {u['username']} | Nombre: {u['cn']} | Estado: {u['status']}")

print("\n--- PRUEBA 2: Buscar un usuario específico ('gomez') ---")
filtrados = provider.search_users("gomez")
for u in filtrados:
    print(f"Encontrado -> {u['username']} ({u['dept']})")
