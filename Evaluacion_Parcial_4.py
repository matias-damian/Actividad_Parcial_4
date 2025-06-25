import time

# Actividad parcial 4
# MatiasToledo

# Variables
stock_fortificados_concepcion: int = 500
compras_fortificados_concepcion: list = []

stock_fortificados_puentealto: int = 1300
compras_fortificados_puentealto: list = []

# Funciones auxiliares
def has_uppercase(input_string: str) -> bool:
    return any(char.isupper() for char in input_string)

def has_number(input_string: str) -> bool:
    return any(char.isdigit() for char in input_string)

def existe_comprador(registro: list, comprador: str) -> bool:
    """Verifica si ya existe el comprador en el registro (lista de dicts)."""
    return any(comprador in compra for compra in registro)

# Funciones de compra
def fortificados_concepcion():
    global stock_fortificados_concepcion
    try:
        if stock_fortificados_concepcion < 1:
            print("No hay stock de entradas para esta locación")
            return

        comprador = input("Por favor, ingrese el nombre del comprador: ").strip()
        if existe_comprador(compras_fortificados_concepcion, comprador):
            print("No puede volver a comprar la misma persona")
            return

        codigo = input("Por favor, ingrese el código de confirmación: ").strip()
        if len(codigo) < 6:
            print("El código de confirmación debe tener un largo mínimo de 6 caracteres")
            return
        if not has_uppercase(codigo):
            print("El código de confirmación debe tener al menos una letra mayúscula")
            return
        if not has_number(codigo):
            print("El código de confirmación debe tener al menos un número")
            return
        if " " in codigo:
            print("El código de confirmación no puede tener espacios en blanco")
            return

        compras_fortificados_concepcion.append({comprador: codigo})
        stock_fortificados_concepcion -= 1

        print("Entrada registrada exitosamente")
        print("-- Compra en Concepción --")
        print("Nombre del comprador:", comprador)
        print("Código de confirmación:", codigo)

    except Exception as e:
        print("Error en Concepción:", e)

def fortificados_puentealto():
    global stock_fortificados_puentealto
    try:
        if stock_fortificados_puentealto < 1:
            print("No hay stock de entradas para esta locación")
            return

        comprador = input("Por favor, ingrese el nombre del comprador: ").strip()
        if existe_comprador(compras_fortificados_puentealto, comprador):
            print("No puede volver a comprar la misma persona")
            return

        try:
            entradas = int(input("Por favor, ingrese el número de entradas a comprar: ").strip())
        except ValueError:
            print("Ingrese un número válido de entradas")
            return

        if entradas < 1:
            print("Tiene que comprar al menos una entrada")
            return
        if entradas > 3:
            print("No puede comprar más de 3 entradas por persona")
            return
        if entradas > stock_fortificados_puentealto:
            print("No hay suficiente stock disponible")
            return

        compras_fortificados_puentealto.append({comprador: entradas})
        stock_fortificados_puentealto -= entradas

        print("Entrada registrada exitosamente")
        print("-- Compra en Puente Alto --")
        print("Nombre del comprador:", comprador)
        print("Número de entradas:", entradas)

    except Exception as e:
        print("Error en Puente Alto:", e)

# Menú principal
def menu():
    while True:
        try:
            print("\nTOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
            print("1. Comprar entrada a Los Fortificados en Concepción.")
            print("2. Comprar entrada a Los Fortificados en Puente Alto.")
            print("3. Salir.")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                fortificados_concepcion()
            elif opcion == "2":
                fortificados_puentealto()
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Debe ingresar una opción válida!!")

        except Exception as e:
            print("Error en el menú principal:", e)
        
        time.sleep(3)

menu()
