from domain.telefono_handler import Handler

class GeneralHandler(Handler):
    def handle(self, request):
        if request.marca.lower() != "samsung" and request.marca.lower() != "motorola" and request.marca.lower() != "xiaomi":
            print("La empresa General maneja el pedido.")
            print(request)
        else:
            super().handle(request)