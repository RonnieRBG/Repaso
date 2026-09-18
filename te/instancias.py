from te import Te

te_verde = Te()
te_negro = Te()

tipo_1 = type(te_verde)
tipo_2 = type(te_negro)

print("tipo del objeto 1", tipo_1)
print("tipo del objeto 2", tipo_2)

if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("los objetos no son del mismo tipo")
