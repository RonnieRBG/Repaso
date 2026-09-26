class Pelota():
    def __init__(self, color: str, tamanio: int, material: str, precio: int=  3200):
        self.color = color
        self.tamanio = tamanio
        self.material = material
        self.precio = precio
        self.forma = "redonda"

if __name__ == "__main__":
    p = Pelota("Amarillo", 16, "plástico")
    # Salida: Amarillo 16 plástico
    print(p.color, p.tamanio, p.material)
    # Salida: 
    # TypeError: __init__() missing 3 required positional arguments: 
    # 'color', 'tamanio', and 'material'
    ##p2 = Pelota()