class Bola:
    def __init__(self,cor,circuferencia,material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material
    
    def usuario_cor(self):
        self.cor = input('Qual é a cor da bola?\n')
        return self.cor

    def material_pergunta(self):
        self.circuferencia = input('Qual é o material da bola?\n')
        return self.circuferencia

    def circuferencia_pergunta(self):
        self.material = input('Qual é a Circuferência da bola?\n')
        return self.material
    
    def main(self):
        resposta_cor = self.usuario_cor()
        resposta_material = self.material_pergunta()
        resposta_circuferencia = self.circuferencia_pergunta()
        print(f"Olá! Aqui está a sua bola:\n----> Cor = {resposta_cor} <----\n ----> Material = {resposta_material} <----\n ---->Circunferência = {resposta_circuferencia}.<----")

bola = Bola(None,None,None)
bola.main()