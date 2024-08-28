class Square:
    def __init__(self,lados):
        self.tamanho = lados

    def definir_tamanho(self):
        while True:
            try:
                self.tamanho = int(input("Qual irá ser o tamanho lado do quadrado?\n"))

                lado = self.tamanho

                if self.tamanho <= 0:
                    print("Por favor digite um número maior que '0'")

                area = lado * lado
                return area
            
            except ValueError as e:
                print(f"Erro: {e}. Por favor, insira um número válido.")

    def main(self):
        calcular_area = self.definir_tamanho()
        print(f"Tamanho da Área : {calcular_area}")

square = Square(None)
square.main()