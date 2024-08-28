import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Retangulo:
    def __init__(self,base=0,altura=0,perimetro=0,area=0):
        self.base_valor = base
        self.altura_valor = altura
        self.perimetro_valor = perimetro
        self.area_valor = area
    
    def calcular(self):
        while True:
            try:
                self.base_valor = int(input("Qual o Tamanho da base do espaço?\n"))

                self.altura_valor = int(input("Qual o Tamanho da altura do espaço?\n"))

                if self.base_valor <= 0 or self.altura_valor <= 0:
                    print("Por favor, Insira um valor maior que '0' ")
                else:
                    break

            except ValueError as e:
                print("Error {e}: Por favor inserir um número inteiro válido")

    def cal_perimetro(self):
        self.perimetro_valor = 2 *(self.altura_valor + self.base_valor)
        return self.perimetro_valor
    
    def cal_area(self):
        self.area_valor = self.altura_valor * self.base_valor
        return self.area_valor
    
    def dados(self):
        print("<-------------------+  Dados Registrados  +--------------+>\n")
        print (f"Altura : {self.altura_valor}")
        print (f"Base : {self.base_valor}")
        print (f"Perimetro : {self.cal_perimetro()}")
        print (f"Área : {self.cal_area()}")
        print("<-------------------+---------------------+--------------+>\n")

def formatar_valor(valor):
    return locale.currency(valor, symbol=True, grouping=True)


def main ():
    retangulo = Retangulo()
    retangulo.calcular()
    
    retangulo.dados()

    area = retangulo.cal_area()
    perimetro = retangulo.cal_perimetro()

    quantidade_pisos = area 
    quantidade_rodape = perimetro

    print("<-------------------+  Preço Final  +--------------+>\n")
    print(f"Para está construção serão necessários : {quantidade_rodape}\nPara está construção serão necessários : {quantidade_pisos}")
    print("<-------------------+---------------------+--------------+>\n")
    preco_pisos = area * 20
    preco_rodape = perimetro * 40

    preco_pisos_formatado = formatar_valor(preco_pisos)
    preco_rodape_formatado = formatar_valor(preco_rodape)

    print("<-------------------+  Preço Final  +--------------+>\n")
    print(f"O valor dos pisos Ficará : {preco_pisos_formatado}\nO valor do rodapé ficará : {preco_rodape_formatado}")
    print("<-------------------+---------------------+--------------+>\n")
main()