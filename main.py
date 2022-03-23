class Motor:
    def __init__(self,cilindro, tipo,registro):
        self.numeroCilindros = cilindro
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo


class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro =registro

    def cambiarColor(self, color):
        permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in permitidos:
            self.color = color


class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,lista,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = lista
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        trueAsientos = [type(a) == Asiento for a in self.asientos]
        return sum(trueAsientos)

    def verificarIntegridad(self):
        lstregistros = []
        for a in self.asientos:
            if type(a) == Asiento:
                lstregistros.append(a)
        lstregistros = [a.registro for a in lstregistros]
        lstregistros.append(self.motor.registro)
        lstregistros = [self.registro == i for i in lstregistros]
        if all(lstregistros):
            return "Auto original"
        return "Las piezas no son originales"
