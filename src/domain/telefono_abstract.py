from abc import ABC, abstractmethod

class AbstractHandler(ABC):
    @abstractmethod
    def handle(self, request):
        pass

class AbstractTelefonoBuilder(ABC):
    @abstractmethod
    def with_marca(self, marca):
        pass

    @abstractmethod
    def with_modelo(self, modelo):
        pass

    @abstractmethod
    def with_color(self, color):
        pass

    @abstractmethod
    def build(self):
        pass

class AbstractTelefono(ABC):
    @abstractmethod
    def __str__(self):
        pass
