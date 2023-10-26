from service.telefono_builder import TelefonoBuilder

from controller.motorola import MotorolaHandler
from controller.xiaomi import XiaomiHandler
from controller.samsung import SamsungHandler
from controller.general import GeneralHandler

def controladores(marca, modelo, color):
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


