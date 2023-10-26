from domain.classes import AbstractHandler

class Handler(AbstractHandler):
    _next_handler = None
    
    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
