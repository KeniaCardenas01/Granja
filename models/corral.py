class Corral:
    def __init__(self, id_corral: int):
        self._id_corral = id_corral
        self._animales = []

    def agregar_animal(self, animal):
        self._animales.append(animal)

    def listar_animales(self):
        return [a.nombre for a in self._animales]

    def limpiar(self) -> str:
        return f"Corral {self._id_corral} ha sido limpiado."
