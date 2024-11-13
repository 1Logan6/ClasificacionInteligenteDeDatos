class RegresionLinealSimple:
    def __init__(self):
        #self.publicidad = [23, 26, 30, 34, 43, 48, 52, 57, 58] # Datos de advertising
        #self.ventas = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518] # Datos de sales

        self.publicidad = [1,2,3,4,5,6,7,8,9]  # Datos de advertising B1 
        self.ventas = [2,4,6,8,10,12,14,16,18]  # Datos de sales B0 Inter
        self.n = len(self.publicidad)
    
    def suma_xy(self):
        return sum(p * v for p, v in zip(self.publicidad, self.ventas))
    
    def suma_x(self):
        return sum(self.publicidad)
    
    def suma_y(self):
        return sum(self.ventas)
    
    def suma_x_cuadrada(self):
        return sum(p ** 2 for p in self.publicidad)
    
    def calcular_beta_1(self):
        numerador = (self.n * self.suma_xy()) - (self.suma_x() * self.suma_y())
        denominador = (self.n * self.suma_x_cuadrada()) - (self.suma_x() ** 2)
        return numerador / denominador
    
    def calcular_beta_0(self, beta_1):
        return (self.suma_y() - (beta_1 * self.suma_x())) / self.n
    
    def ajustar(self):
        beta_1 = self.calcular_beta_1()
        beta_0 = self.calcular_beta_0(beta_1)
        return beta_0, beta_1
    
    def predecir(self, valor_publicidad, beta_0, beta_1):
        return beta_0 + beta_1 * valor_publicidad

if __name__ == "__main__":
    # Aqui se crea el modelo y se asignan los valores de beta 0 y beta 1
    modelo = RegresionLinealSimple()
    beta_0, beta_1 = modelo.ajustar()

    # Aqui se imprime los resultados de B0 y B1
    print(f"Valores obtenidos del modelo: ventas = {beta_0:.2f} + {beta_1:.2f} * publicidad")

    # Y aqui pedimos un dato para realizar la prediccion
    try:
        valor_publicidad = float(input("Ingresa un valor de publicidad para predecir ventas: "))
        prediccion_ventas = modelo.predecir(valor_publicidad, beta_0, beta_1)
        print(f"Predicción dada la publicidad = {valor_publicidad}: se estiman las siguientes ventas = {prediccion_ventas:.2f}")
    except ValueError:
        print("Por favor, ingresa un número válido :).")
