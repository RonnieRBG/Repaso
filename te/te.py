class Te():
    duracion = 365

    @staticmethod
    def selecionar_te_y_recomendacion(tipo_te: int):
        if tipo_te == 1:
            tipo = "Té negro"
            tiempo = 3
            recomendacion = "Se recomienda consumir al desayuno"
        elif tipo_te == 2:
            tipo = "Te verde"
            tiempo = 5
            recomendacion = "Se recomienda consumir al medio día"
        elif tipo_te == 3:
            tipo = "Agua de hiervas"
            tiempo = 6
            recomendacion = "Se recomienda consumir al atardecer"
        else:
            tipo = "No válido"
            tiempo = 0
            recomendacion = "Sabor no válido"
    
        return tipo, tiempo, recomendacion       

    @staticmethod
    def obtener_precio(tamanio_te: int):
        if tamanio_te == 1:
            return 500 * 10
        elif tamanio_te == 2:
            return 300 * 10




