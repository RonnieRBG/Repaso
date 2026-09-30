from te import Te

print("====SISTEMA DE COMPRA DE TE=====")
print("Seleccione el tipo de Te:")
print("1. Té Negro")
print("2. Té Verde")
print("3. Agua de Hiervas")

opcion_te = int(input(("Ingrese opcion (1, 2, 3): \n")))
opcion_tamanio = int(input("Tamaño ? 1.500gr / 2.300 gr \n"))

tipo, tiempo, recomendacion = Te.selecionar_te_y_recomendacion(opcion_te)
tamanio_seleccionado = Te.obtener_precio(opcion_tamanio)


print("\n--- DETALLE DE LA SOLICITUD ---")
print(f"• Tipo de Te seleccionada: {tipo}")
print(f"• Tiempo de preparación: {tiempo} minutos")  # Atributo de clase
print(f"• Recomendación: {recomendacion}")
print(f"Precio {tamanio_seleccionado}")
1
