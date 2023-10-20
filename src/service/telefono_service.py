from domain.telefono_handler import Handler

class MotorolaHandler(Handler):
    def handle(self, request):
        if request.marca.lower() == "motorola":
            print("La empresa Motorola maneja el pedido.")
            print(request)
        else:
            super().handle(request)

class XiaomiHandler(Handler):
    def handle(self, request):
        if request.marca.lower() == "xiaomi":
            print("La empresa Xiaomi maneja el pedido.")
            print(request)
        else:
            super().handle(request)

class SamsungHandler(Handler):
    def handle(self, request):
        if request.marca.lower() == "samsung":
            print("La empresa Samsung maneja el pedido.")
            print(request)
        else:
            super().handle(request)

class GeneralHandler(Handler):
    def handle(self, request):
        if request.marca.lower() != "samsung" and request.marca.lower() != "motorola" and request.marca.lower() != "xiaomi":
            print("La empresa General maneja el pedido.")
            print(request)
        else:
            super().handle(request)


