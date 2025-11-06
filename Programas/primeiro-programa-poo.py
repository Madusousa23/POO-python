class bike:
    def __init__(self,cor, modelo,ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim...Plim..")

    def correr(self):
        print("VRUMMM")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
# b1 = bike("Vermelho","Caloi",2022,600)
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bike("verde", "Monark", 200, 189)
bike.buzinar(b2)