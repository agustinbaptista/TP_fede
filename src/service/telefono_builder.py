from service.telefono import Telefono
from domain.telefono_abstract import AbstractTelefonoBuilder

class TelefonoBuilder(AbstractTelefonoBuilder):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TelefonoBuilder, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.marca = None
        self.modelo = None
        self.color = None

    def with_marca(self, marca):
        self.marca = marca
        return self

    def with_modelo(self, modelo):
        self.modelo = modelo
        return self

    def with_color(self, color):
        self.color = color
        return self

    def build(self):
        return Telefono(self)
