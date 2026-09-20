class Medicamento():
    DESCUENTO = 0.05
    IVA = 0.19 
    
    
    @staticmethod
    #Funcion que determina si un precio es valido
    def es_precio_valido(precio:int) -> bool:
        return precio > 0
    
    def ingresar_precio(self, precio: int) -> None:
       
        if Medicamento.es_precio_valido(precio):
            
            self.precio = precio
            self.descuento = 0.0
            
            if self.precio >= 10000 and self.precio <= 19999:
                self.descuento = 0.1
                
            elif self.precio >= 20000 and self.precio <= 29999:
                self.descuento = 0.2
                
            elif self.precio >= 30000:
                self.descuento = 0.3
            else:
                self.precio = precio
                
            self.precio = precio * (1.0 - self.descuento)
        else:
            print("Precio inválido")
            
            
## if __name__ == "__main__":
        #mi_pelota = Pelota()
        #print(Pelota.crear_rebote)
        ##Prueba valicacion de precio de medicamentos
        ##precio_medicamento = int(input("Ingrese un precio para el medicamento"))
        ##es_valido = Medicamento.es_precio_valido(precio_medicamento)
        ##if es_valido:
        ##    print("El precio ingresado es valido")
        ##else:
          ##  print("El precio ingresado no es válido")
    ## Prueba: verificar si los valores estaticos son iguales
## medicamento_1, medicamento_2 = Medicamento(), Medicamento()

if __name__ == "__main__":
    medicamento_nuevo = Medicamento()
    precio_ingresado = int(input("Ingrese precio de medicamento: "))
    medicamento_nuevo.ingresar_precio(precio_ingresado)
    medicamento_nuevo.es_precio_valido(precio_ingresado)
    print(f"el precio del medicamento es {precio_ingresado}")
    print(f"el decuento del medicamento es de {(medicamento_nuevo.descuento) * 100 }%")

## if medicamento_1.IVA == medicamento_2.IVA:
   ##     print("El IVA aplicado a los medicamentos es el mismo")
     ##   remedio = Medicamento()
       ## print(Medicamento().DESCUENTO)
        ## print(f"Los medicamentos tienen un IVA del {int(remedio.IVA * 100)} %")


