from TiendaMascotas.main import monto
class OrdenCompra():
    
    #metodo Constructor, leugo de varios intentos se modifica nuevamente el constructor
    
    #def __init__(self, identificador = 0, total_productos = 0, monto = 0, codigo_descuento = ""):
     #   self.identificador = identificador
      #  self.total_productos = total_productos
       # self.monto = monto
        #self.codigo_descuento = codigo_descuento

     
    def __init__(self, identificador = 0, total_productos = 0, monto = 0, codigo_descuento = ""):
       self.identificador = identificador
       self.total_productos = total_productos
       self.monto = monto
       self.codigo_descuento = codigo_descuento
    
    
    def nueva_orden(self):
        self.identificador = 0
        self.total_productos = 0
        self.monto = 0
       
## este codigo tiene problemas
"""
    def asigna_monto(self, nuevo_monto : int):
        self.monto = nuevo_monto
        self.codigo_descuento = ""
        if self.monto > 20000:
            self.codigo_descuento = "20PORCIENTO"
        elif self.monto > 10000:
            self.codigo_descuento = "10PORCIENTO"
#else:
#    codigo_descuento = ""

"""

if __name__ == "__main__":
    pass