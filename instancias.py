from te import Te


te_negro = Te()
te_verde = Te()

tipo_te_negro = type(te_negro)
tipo_te_verde = type(te_verde)


print("Tipo de te_negro:", tipo_te_negro)
print("Tipo de te_verde:", tipo_te_verde)

if tipo_te_negro == tipo_te_verde:
    print("Ambos objetos son del mismo tipo.")
else:
    print("Los objetos no son del mismo tipo.")
