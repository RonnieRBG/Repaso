from medicamento.medicamento import Medicamento
class Pelota():
    FORMA = "redondeada"
    POSICIONES = [3, 0, 2, 0, 1, 0]

    @staticmethod
    def crear_rebote():
        return [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

    @staticmethod
    #Funcion que determina si un precio es valido
    def es_precio_valido(precio:int) -> bool:
        return precio > 0

    if __name__ == "__main__":
        #mi_pelota = Pelota()
        #print(Pelota.crear_rebote)
        ##Prueba valicacion de precio de medicamentos
        precio_medicamento = int(input("Ingrese un precio para el medicamento"))3
        es_valido = Medicamento.es_precio_valido(precio_medicamento)
        if es_valido:
            print("El precio ingresado es valido")
        else:
            print("El precio ingresado no es válido")
    ## Prueba: verificar si los valores estaticos son iguales
    medicamento_1, medicamento_2 = Medicamento(), Medicamento()
    if medicamento_1.IVA == medicamento_2.IVA:
        print("El IVA aplicado a los medicamentos es el mismo")

