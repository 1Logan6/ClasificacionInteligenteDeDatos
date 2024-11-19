class Datos:
    def __init__(self, publicidad, ventas):
        self.publicidad = publicidad
        self.ventas = ventas
        self.n = len(publicidad)

class CalculosMateDiscreta:
    def __init__(self, datos):
        self.datos = datos
    
    def suma_xy(self):
        return sum(p * v for p, v in zip(self.datos.publicidad, self.datos.ventas))
    
    def suma_x(self):
        return sum(self.datos.publicidad)
    
    def suma_y(self):
        return sum(self.datos.ventas)
    
    def suma_x_cuadrada(self):
        return sum(p ** 2 for p in self.datos.publicidad)

class ParametrosModelo:
    def __init__(self, calculos):
        self.calculos = calculos
    
    def calcular_beta_1(self):
        n = self.calculos.datos.n
        suma_xy = self.calculos.suma_xy()
        suma_x = self.calculos.suma_x()
        suma_y = self.calculos.suma_y()
        suma_x_cuadrada = self.calculos.suma_x_cuadrada()
        numerador = (n * suma_xy) - (suma_x * suma_y)
        denominador = (n * suma_x_cuadrada) - (suma_x ** 2)
        return numerador / denominador
    
    def calcular_beta_0(self, beta_1):
        suma_y = self.calculos.suma_y()
        suma_x = self.calculos.suma_x()
        n = self.calculos.datos.n
        return (suma_y - (beta_1 * suma_x)) / n

class ModeloRegresionLinealSimple:
    def __init__(self, datos):
        self.datos = datos
        self.calculos = CalculosMateDiscreta(datos)
        self.parametros = ParametrosModelo(self.calculos)
        self.beta_0, self.beta_1 = self.ajustar()
    
    def ajustar(self):
        beta_1 = self.parametros.calcular_beta_1()
        beta_0 = self.parametros.calcular_beta_0(beta_1)
        return beta_0, beta_1
    
    def predecir(self, valor_publicidad):
        return self.beta_0 + self.beta_1 * valor_publicidad

if __name__ == "__main__":
    # Crear los datos
    datos = Datos(publicidad=[1,2,3,4,5,6,7,8,9], ventas=[2,4,6,8,10,12,14,16,18])
    
    # Crear el modelo de regresión lineal simple
    modelo = ModeloRegresionLinealSimple(datos)
    
    # Mostrar los valores de beta
    print(f"Valores obtenidos del modelo: ventas = {modelo.beta_0:.2f} + {modelo.beta_1:.2f} * publicidad")

    # Solicitar valor de publicidad para predicción
    try:
        valor_publicidad = float(input("Ingresa un valor de publicidad para predecir ventas: "))
        prediccion_ventas = modelo.predecir(valor_publicidad)
        print(f"Predicción dada la publicidad = {valor_publicidad}: se estiman las siguientes ventas = {prediccion_ventas:.2f}")
    except ValueError:
        print("Por favor, ingresa un número válido :).")