from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre: str, peso: float):
        self._nombre = nombre
        self._peso = peso

    @abstractmethod
    def alimentar(self) -> str:
        pass

    @abstractmethod
    def vacunar(self) -> str:
        pass

    def registrar_peso(self, nuevo_peso: float) -> str:
        anterior = self._peso
        self._peso = nuevo_peso
        return f"{self._nombre}: peso actualizado de {anterior}kg a {nuevo_peso}kg"

    @property
    def nombre(self):
        return self._nombre

    @property
    def peso(self):
        return self._peso
