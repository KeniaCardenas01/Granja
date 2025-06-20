from datetime import date

class Empleado:
    def __init__(self, nombre: str, id_empleado: int):
        self._nombre = nombre
        self._id = id_empleado

    def realizar_tarea(self, tarea: str) -> str:
        return f"{self._nombre} realiza: {tarea}"

    def registrar_asistencia(self) -> str:
        return f"Asistencia de {self._nombre} registrada el {date.today()}"

    def reportar_incidencia(self, texto: str) -> str:
        return f"{self._nombre} reportó: {texto}"

    @property
    def nombre(self):
        return self._nombre
