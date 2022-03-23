class Motor:
    def __init__(self, registro):
        self.numeroCilindros = 1
        self.tipo = "gasolina"
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo


class Asiento:
    def __init__(self,registro):
        self.color = "Azul"
        self.precio = 0
        self.registro =registro

    def cambiarColor(self, color):
        permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in permitidos:
            self.color = color


class Auto:
    cantidadCreados = 0
    def __init__(self):
        self.modelo = "px"
        self.precio = 10**8
        self.asientos = [Asiento(8881)]
        self.marca = "WMB"
        self.motor = Motor(8881)
        self.registro = 8881
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


# if __name__ == "__main__":
#     carro = Auto()
#     print(carro.cantidadAsientos())
#     print(carro.verificarIntegridad())
#     carro.asientos.append("had")
#     carro.asientos.append(Asiento(888))
#     carro.asientos[0].cambiarColor("negro")
#     print(carro.cantidadAsientos())
#     print(carro.verificarIntegridad())
#     print(carro.asientos[0].color)
