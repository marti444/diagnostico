Crear una clase llamada vehículo  capaz de procesar la información básica de los autos en una consencionaria.
Deberá tener constructor y los atributos del vehículo serán: patente, marca, modelo y kilometraje. Crear métodos (de acceso) getter y (de modificación) setter mostrará por pantalla al menos 1 atributo y modificar el kilometraje

class Vehículo:
    def _init_(self, patente, marca, modelo, kilometraje):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

    def get_patente(self):
        return self.patente

    def set_kilometraje(self, nuevo_kilometraje):
        self.kilometraje = nuevo_kilometraje
        print("El kilometraje ha sido actualizado.")
