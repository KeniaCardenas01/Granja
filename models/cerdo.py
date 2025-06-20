from models.animal import Animal

class Cerdo(Animal):
    def alimentar(self) -> str:
        return f"{self.nombre} fue alimentado con maíz."

    def vacunar(self) -> str:
        return f"{self.nombre} fue vacunado contra peste porcina."
