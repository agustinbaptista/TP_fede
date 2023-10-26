from controller.telefono_control import controladores

from view.menu import menu

def main():
    while True: 
        marca, modelo, color = menu()

        controladores(marca, modelo, color)

        respuesta = input("¿Quiere comprar otro teléfono? S/N: ")
        if respuesta.lower() != "s":
            break 

if __name__ == "__main__":
    main()

