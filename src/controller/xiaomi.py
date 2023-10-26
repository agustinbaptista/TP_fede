from domain.telefono_handler import Handler

class XiaomiHandler(Handler):
    def handle(self, request):
        if request.marca.lower() == "xiaomi":
            print("La empresa Xiaomi maneja el pedido.")
            print(request)
        else:
            super().handle(request)

