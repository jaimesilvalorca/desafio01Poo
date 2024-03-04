from te import Te


sabor = int(input("Ingrese el sabor del té (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
formato = int(input("Ingrese el formato (300 o 500 gramos): "))


te_pedido = Te()

tiempo, recomendacion = Te.tiempo_recomendacion(sabor)

precio = Te.obtener_precio(formato)


print("Detalle del pedido:")
print("Sabor:", "Té negro" if sabor == 1 else "Té verde" if sabor == 2 else "Agua de hierbas")
print("Formato:", formato, "gramos")
print("Precio:", precio, "pesos")
print("Tiempo de preparación:", tiempo, "minutos")
print("Recomendación:", recomendacion)
