from domain.telefono_handler import Handler

class SamsungHandler(Handler):
    def handle(self, request):
        if request.marca.lower() == "samsung":
            print("La empresa Samsung maneja el pedido.")
            print(request)
        else:
            super().handle(request)

