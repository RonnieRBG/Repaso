from ordencompra import OrdenCompra
"""

#Sin el metodo constructor

oc = OrdenCompra()
oc.nueva_orden()


oc.identificador = int(input("Ingrese identifcador de la OC: \n"))
oc.total_productos = int(input("Ingrese total de productos: \n"))
oc.monto = int(input("Ingrese monto: \n"))

if oc.monto > 20000:
    oc.codigo_descuento = "20PORCIENTO"
elif oc.monto > 10000:
    oc.codigo_descuento = "10PORCIENTO"
    
"""
#Con el metodo Constructor

identificador = int(input("Ingrese identifcador de la OC: \n"))
total_productos = int(input("Ingrese total de productos: \n"))
monto = int(input("Ingrese monto: \n"))

## esta logicva se pasa orden compra con otra funcion
#if monto > 20000:
#    codigo_descuento = "20PORCIENTO"
#elif monto > 10000:
#    codigo_descuento = "10PORCIENTO"
#else:
#    codigo_descuento = ""
    
oc = OrdenCompra(identificador, 
                 total_productos, 
                 monto, 
                 codigo_descuento)