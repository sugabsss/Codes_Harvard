class Macaco :
    def __init__(self) :
        self.nome = ["",""]
        self.bucho1 = []
        self.bucho2 = []
        
    def macaco1(self):
        self.nome[0] = input("««« Qual será o nome de nosso macaquinho numero 1 ? »»»\n")
        return self.nome[0]
                
    def macaco2 (self):
        self.nome[1] = input("««« Qual será o nome de nosso macaquinho numero 2 ? »»»\n")
        return self.nome[1]

    def digerir_macaco1(self):
        try:
            for i in range(3):  # Permite três tentativas para o usuário escolher os alimentos
                while True:
                    alimento_escolher = input(f"Escolha uma fruta para o macaco: {', '.join(lista_alimentos)}\n").lower().strip()

                    if alimento_escolher in lista_alimentos:
                        self.bucho1.append(alimento_escolher)
                        print(f"O macaco comeu{self.nome[0]}: {alimento_escolher}")
                        break
                    else:
                        print("Esse alimento não está na lista.")

        except ValueError as e:
            ("Error {e}: Dados necessários não foram fornecidos")

    def digerir_macaco2(self):
        try:
            for j in range(3):  # Permite três tentativas para o usuário escolher os alimentos
                while True:
                    alimento_escolher2 = input(f"Escolha uma fruta para o macaco: {', '.join(lista_alimentos)}\n").lower().strip()

                    if alimento_escolher2 in lista_alimentos:
                        self.bucho2.append(alimento_escolher2)
                        print(f"O macaco comeu{self.nome[1]}: {alimento_escolher2}")
                        break
                    else:
                        print("Esse alimento não está na lista.")
                
        except ValueError as e:
            ("Error {e}: Dados necessários não foram fornecidos ") 
    
    def dados(self):
            print("<-------------------+  Banco de Dados  +--------------+>\n")
            print(f"Nome do primeiro Macaco : {self.nome[0]}, E ele tem agora no bucho:{self.bucho1}")
            print(f"Nome do segundo Macaco : {self.nome[1]}, E ele tem agora no bucho:{self.bucho2}")
            print("<-------------------+---------------------+--------------+>\n")

macaco = Macaco()
lista_alimentos = ['banana', 'maçã', 'uva', 'pera', 'cereja', 'melancia']
macaco.macaco1()
macaco.macaco2()
macaco.digerir_macaco1()
macaco.digerir_macaco2()
macaco.dados()


