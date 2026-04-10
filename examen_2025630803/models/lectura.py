class Lectura:
    def __init__(self, id_lectura, estacion, presion_hpa, temporada):
        self.id_lectura = id_lectura
        self.estacion = estacion
        self.presion_hpa = float(presion_hpa)
        self.temporada = temporada

    def clasificar(self):
        valor = self.presion_hpa
        
        if valor < 997.2:
            return "Muy baja"
        elif 997.2 <= valor < 1010.4:
            return "Baja"
        elif 1010.4 <= valor < 1021.1:
            return "Normal"
        elif 1021.1 <= valor < 1032.0:
            return "Alta"
        elif valor >= 1032.0:
            return "Muy alta"

    def __str__(self):
        return f"{self.id_lectura} - {self.estacion} (temporada: {self.temporada}) - {self.presion_hpa:.1f} hPa"
    def __repr__(self):
        return f"Lectura(id='{self.id_lectura}', valor={self.presion_hpa:.1f}, clase='{self.clasificar()}')"