from pelota import Pelota

p = Pelota() # a p se le asigna la CLASE PELOTA, no una insyancia de la clase

"""
ERROR: p.asigna_color() no corresponde, 
es un metodo de INSTANCIA y P es un

"""

p.asigna_color(nuevo_color="rojo")
# Salida: El color de esta pelota es rojo
p.lee_color()