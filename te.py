class Te:
    precio_300gr = 3000
    precio_500gr = 5000

    @staticmethod
    def tiempo_recomendacion(sabor):
        if sabor == 1:  # Té negro
            return 3, "Se recomienda consumir al desayuno."
        elif sabor == 2:  # Té verde
            return 5, "Se recomienda consumir al medio día."
        elif sabor == 3:  # Agua de hierbas
            return 6, "Se recomienda consumir al atardecer."

    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            return Te.precio_300gr
        elif formato == 500:
            return Te.precio_500gr