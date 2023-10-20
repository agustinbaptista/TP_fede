from controller.telefono_builder import TelefonoBuilder
from service.telefono_service import MotorolaHandler, XiaomiHandler, SamsungHandler, GeneralHandler
from view.menu import menu

def main():
    while True: 
        marca, modelo, color = menu()

        motorola_handler = MotorolaHandler()
        xiaomi_handler = XiaomiHandler()
        samsung_handler = SamsungHandler()
        general_handler = GeneralHandler()

        motorola_handler.set_next(xiaomi_handler)
        xiaomi_handler.set_next(samsung_handler)
        samsung_handler.set_next(general_handler)

        celular = TelefonoBuilder().with_marca(marca)\
                                   .with_modelo(modelo)\
                                   .with_color(color)\
                                   .build()
        motorola_handler.handle(celular)

        respuesta = input("¿Quiere comprar otro teléfono? S/N: ")
        if respuesta.lower() != "s":
            break 

if __name__ == "__main__":
    main()

