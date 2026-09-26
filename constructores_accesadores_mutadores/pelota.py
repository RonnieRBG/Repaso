class Pelota():
    def __init__(self):
        self.color = "blanco"
        self.tamanio = 20
        self.material = "plástico"


if __name__ == "__main__":
# Salida: "¡Se ha creado una pelota!"
p = Pelota()
print(p.color, p.tamanio, p.material)
