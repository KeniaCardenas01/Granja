from models.vaca import Vaca
from models.cerdo import Cerdo
from models.gallina import Gallina
from models.corral import Corral
from models.granja import Granja

if __name__ == "__main__":
    try:
        granja = Granja("El Buen Pastor")

        # Empleados
        granja.contratar_empleado("Juan Pérez", 1)
        granja.contratar_empleado("Ana Gómez", 2)

        # Corral y animales
        corral1 = Corral(101)
        granja.agregar_corral(corral1)

        vaca = Vaca("Lola", 250)
        cerdo = Cerdo("Pepe", 120)
        gallina = Gallina("Clara", 2.1)

        corral1.agregar_animal(vaca)
        corral1.agregar_animal(cerdo)
        corral1.agregar_animal(gallina)

        print(vaca.alimentar())
        print(cerdo.vacunar())
        print(gallina.registrar_peso(2.3))

        for emp in granja.obtener_empleados():
            print(emp.realizar_tarea("Supervisar corral"))
            print(emp.registrar_asistencia())

        print(corral1.limpiar())

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
