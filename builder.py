class Telefono:
    def __init__(self, builder):
        self.marca = builder.marca
        self.color = builder.color
        self.modelo = builder.modelo

    def __str__(self):
        return f"Telefono =  marca: {self.marca} | modelo: {self.modelo} | color:{self.color}"


class TelefonoBuilder:
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.color = None

    def whit_marca(self, marca):
        self.marca = marca
        return self

    def whit_modelo(self, modelo):
        self.modelo = modelo
        return self

    def whit_color(self, color):
        self.color = color
        return self

    def build(self):
        return Telefono(self)



celular1 = TelefonoBuilder().whit_marca("Motorola").whit_color("Naranja").build()

celular2 = TelefonoBuilder().whit_marca("Samsung").whit_modelo("AB 24").whit_color("Blanco").build()



print(celular1)

print(celular2)

