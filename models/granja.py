from models.empleado import Empleado

class Granja:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._empleados = []
        self._corrales = []

    def contratar_empleado(self, nombre: str, id_empleado: int):
        self._empleados.append(Empleado(nombre, id_empleado))

    def agregar_corral(self, corral):
        self._corrales.append(corral)

    def obtener_empleados(self):
        return self._empleados

    def obtener_corrales(self):
        return self._corrales

    def cerrar_granja(self):
        self._empleados.clear()

    @property
    def nombre(self):
        return self._nombre
