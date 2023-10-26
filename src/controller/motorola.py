from domain.telefono_handler import Handler

class MotorolaHandler(Handler):
    def handle(self, request):
        if request.marca.lower() == "motorola":
            print("La empresa Motorola maneja el pedido.")
            print(request)
        else:
            super().handle(request)

