from models.animal import Animal

class Vaca(Animal):
    def alimentar(self) -> str:
        return f"{self.nombre} fue alimentada con pasto."

    def vacunar(self) -> str:
        return f"{self.nombre} fue vacunada contra fiebre aftosa."
