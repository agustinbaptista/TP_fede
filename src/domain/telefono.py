from domain.telefono_abstract import AbstractTelefono

class Telefono(AbstractTelefono):
    def __init__(self, builder):
        self.marca = builder.marca
        self.color = builder.color
        self.modelo = builder.modelo

    def __str__(self):
        detalles = []
        if self.marca:
            detalles.append(f"Marca: {self.marca}")
        if self.modelo:
            detalles.append(f"Modelo: {self.modelo}")
        if self.color:
            detalles.append(f"Color: {self.color}")
        return "" + " | ".join(detalles)
