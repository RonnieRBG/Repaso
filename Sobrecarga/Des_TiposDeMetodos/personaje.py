class Personaje():
    def __init__ (self, nombre: str):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
    
    def mostar_estado(self, nombre : str, nivel : int, experiencia : int):
        self.nombre = nombre
        self.experiencia = experiencia
        self.nivel = nivel

        print(f"el nombre del personaje es {nombre}\n",
        "el nivel del personaje es : {nivel}\n",
        "la experiencia del personaje es: {nivel}")


