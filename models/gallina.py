from models.animal import Animal

class Gallina(Animal):
    def alimentar(self) -> str:
        return f"{self.nombre} fue alimentada con granos."

    def vacunar(self) -> str:
        return f"{self.nombre} fue vacunada contra gripe aviar."
