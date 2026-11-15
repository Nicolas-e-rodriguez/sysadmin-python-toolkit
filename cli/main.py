import argparse
import sys
import os

# Agregamos la ruta raíz del proyecto para que Python encuentre el módulo 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.providers import DirectoryProvider

def main():
    parser = argparse.ArgumentParser(
        description="Toolkit de Sistema y Directorio (Modo CLI)"
    )
    
    # Subcomandos o argumentos principales
    parser.add_argument(
        "--list", 
        action="store_true", 
        help="Lista todos los usuarios disponibles en el directorio."
    )
    parser.add_argument(
        "--search", 
        type=str, 
        help="Busca un usuario por nombre de usuario o nombre completo."
    )
    parser.add_argument(
        "--mode", 
        type=str, 
        default="mock", 
        choices=["mock", "real"], 
        help="Define si usa datos simulados (mock) o conexión real."
    )

    args = parser.parse_args()

    # Inicializamos el proveedor con el modo elegido
    provider = DirectoryProvider(mode=args.mode)

    if args.list:
        users = provider.search_users("")
        print(f"\n--- LISTADO DE USUARIOS ({len(users)}) ---")
        for u in users:
            print(f"  • {u['username']:<12} | {u['cn']:<20} | Estado: {u['status']:<8} | Dpto: {u['dept']}")
        print("-" * 65)

    elif args.search:
        users = provider.search_users(args.search)
        print(f"\n--- RESULTADOS DE BÚSQUEDA PARA: '{args.search}' ({len(users)}) ---")
        if not users:
            print("  (No se encontraron coincidencias)")
        else:
            for u in users:
                print(f"  • {u['username']:<12} | {u['cn']:<20} | Mail: {u['mail']} | Dpto: {u['dept']}")
        print("-" * 65)

    else:
        # Si ejecuta sin argumentos, muestra la ayuda automáticamente
        parser.print_help()

if __name__ == "__main__":
    main()
