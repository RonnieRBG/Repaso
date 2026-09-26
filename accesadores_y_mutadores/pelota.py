class Pelota():
#metodo costructor
#un solo  _ para protegidos
# dos __ para privados

    def __init__(self, color="Blanco", tamano=20, material="Plástico"):
        self.__color = color
        self.__tamano = max(1, tamano)  
        self.__material = material
#Accesador o getter siempre lleva el proerty
    @property
    def color(self):
        #devuelve el valor del atributo
        return self.__color
    
#mutador o setter siempre lleva el @property.setter
@color.setter
def color(self, valor):
        #devuelve el valor del atributo
        if not valor:
            raise ValueError("El color no puede estar vacío")
        self._color = valor