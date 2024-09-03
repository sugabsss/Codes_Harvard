import sys,csv

palavras_forca = []
class Forca:
    def __init__(self):
    #Criando inputs para o usúario criar palavras e colocar seus respectivos nomes;
        self.jogador1 = ''
        self.jogador2 = ''
        self.palavra = ''
    
    #Set de um número máximo de tentativas possiveis;
        self.tentativas = 5      
        
    #Conjuto de letras que ainda precisam ser encontradas;
        self.letras_restantes = set()

    #Conjuto de letras que já foram encontradas;
        self.letras_encotradas = set()  

    def usuario1(self):      #Função de criação de usúario 1;
        while True:
                print("»»»»»» Vamos Jogar O Jogo da Forca! ««««««")
                self.jogador1 = input("Nome do jogador 1: ").strip()

                if self.jogador1:
                    break
                else: 
                    print("Digite um nome de usúario Válido Jogador 1 : ")
                    
    def usuario2(self):     #Função de criação de usúario 2;
        while True:
                self.jogador2 = input("Nome do jogador 2: ").strip()

                if self.jogador2:
                    print(f"\n»»»»»» Regras: ««««««\n 1. Você possui apenas 5 chances, caso erre mais de 5 vezes perderá;\n 2. Não é possivel selecionar caracteres especiais ou numeros;\n 3. Categorias: Tipos de Dados, Linguagens/Frameworks de Programação, Arquitetura Computacional;\n 4. Boa sorte {self.jogador2};\n ")
                    break
                else: 
                    print("Digite um nome de usúario Válido Jogador 2 : ")
    
    def pergunta_forca(self):       #Função para pegar a palavra forca que foi escrita pelo usúario 1;
        while True:
            self.palavra = input(f"----> ATENÇÃO : (Lembre-se de respeitar a lista de categorias) <-----\n    »»»»» {self.jogador1}, digite a palavra da forca: «««««\n").lower().strip()
            
            self.letras_restantes = set(self.palavra)
        
            if self.palavra:   
                return {'palavra':self.palavra}
            else:
                print("Coloque uma palavra Válida!")
    
    def tentativas_forca(self):         #Função para estabelecer um limite de tentativas e um limite de caracteres de entrada;
        print(f" ATENÇÃO *  Tamanho da Palavra Escrita pelo ({self.jogador1}) é : ----> {len(self.palavra)} <----")
        
        while self.tentativas > 0:
            self.resposta = input(f"Coloque uma letra : ").lower().strip()

            if len(self.resposta) != 1 or not ('a' <= self.resposta <= 'z'):
                    print("> Desculpe, letra inválida. Por favor digite uma letra entre 'a' e 'z'.")
                    continue    
                
            if self.resposta in self.letras_restantes:
                self.letras_encotradas.add(self.resposta)
                self.letras_restantes.remove(self.resposta)
                print(f"A letra '{self.resposta}' foi encontrada na palavra forca;")
            
            if not self.letras_restantes:
                print("Parabéns! Você encontrou todas as letras.")
                break

            try:
                posicao = self.palavra.index(self.resposta)
                print(f"A letra '{self.resposta}' está na posição: {posicao}")
            
            except ValueError:
                print(f"A letra '{self.resposta}' não foi encontrada na palavra.")
                self.tentativas -= 1
                print(f"» » » » »  Você tem {self.tentativas} tentativas restantes.« « « « «\n")

        if self.tentativas == 0:
            print(f"Excesso no número de tentativas! Você perdeu a palavra era '{self.palavra}'.")
            sys.exit(1)
            
def palavra_update(): 
    try:
        with open("forca.csv", mode = 'r') as file:
            reader = csv.DictReader(file)
            global palavras_forca

            for row in reader:
                row["palavra"] = (row["palavra"])
                palavras_forca.append(row)
                                      
    except FileNotFoundError:
        print("Error 404 FIle not FoundError")
        return 
    
    except Exception as e:  
        print(f"Error ao ler arquivo:{e}")
        return 

def palavra_salvar():
    fieldnames = ["palavra"]

    try:
        with open("forca.csv", mode = 'w') as file:
            write = csv.DictWriter(file, fieldnames=fieldnames)
            write.writeheader()
            write.writerows(palavras_forca)
            
    except FileNotFoundError:
        print("Error 404 FIle not FoundError")
        return 
    
    except Exception as e:  
        print(f"Error ao ler arquivo:{e}")
        return 
    
def main():
    forca = Forca()
    forca.usuario1()
    forca.usuario2()
    palavra_update()

    
    palavra = forca.pergunta_forca()
    forca.tentativas_forca()
    palavras_forca.append(palavra)

    palavra_salvar() 

main()

