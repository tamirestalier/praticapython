import numpy as np
from time import sleep
class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade, dtype=dict)

    def filaVazia(self):
        return self.numeroElementos == 0

    def filaCheia(self):
        return self.numeroElementos == self.capacidade

    def enfileirar(self, valor):
        if self.filaCheia():
            print('A fila está completa')
        else:
            self.valores[self.numeroElementos] = valor
            self.numeroElementos += 1

    def desenfileirar(self):
        if self.filaVazia():
            print('A fila está vazia')
        else:
            for x in range(self.numeroElementos - 1):
                temp = self.valores[x + 1]
                self.valores[x + 1] = None
                self.valores[x] = temp
            self.numeroElementos -= 1

    def primeiro(self):
        if self.filaVazia():
            return -1
        else:
            return self.valores[self.inicio]

'''5 - Escreva um programa em Python que simule o controle de uma pista 
de decolagem de aviões em um aeroporto. Neste programa, 
o usuário deve ser capaz de realizar as seguintes tarefas: 
Listar o número de aviões aguardando na fila de decolagem;
Autorizar a decolagem do primeiro avião da fila;
Adicionar um avião à fila de espera;
Listar todos os aviões na fila de espera;
Listar as características do primeiro avião da fila.'''

print("--- AEROPORTO GOMES ---")
try:
    qtd = int(input("Quantidade de aviões para incluir na pista: "))
    sleep(0.7)
except: 
    print("Opção inválida")

fila = Fila(qtd)

i = 0
while i != 6:
    while True:
        try:
            print('''
        === Selecione uma opção ===
[1] Listar o número de aviões que estão na fila.
[2] Autorizar a decolagem do primeiro avião da fila
[3] Adicionar um avião à fila de espera
[4] Listar todos os aviões na fila de espera
[5] Listar as características do primeiro avião da fila
[6] Sair do programa
''')
            opc = int(input("Escolha sua opção: "))
            sleep(0.7)
            break
        except:
            print("Opção inválida")
    
    if opc == 1:
        if fila.filaVazia():
            print("Não há nenhum avião na pista")
            sleep(0.7)
        else:
            print(f'Há {fila.numeroElementos} avião(ões) na pista de decolagem')
            sleep(0.7)
    
    elif opc == 2:
        if fila.filaVazia():
            print("Não há nenhum avião na pista")
            sleep(0.7)
        else:
            print(f"Avião {fila.valores[0]['Número']} saindo da pista de pouso")
            fila.desenfileirar()
            sleep(0.7)
    
    elif opc == 3:
        if fila.filaCheia():
            print("A pista está cheia")
            sleep(0.7)
        else:
            print("Insira os dados do avião")
            while True:
                try:
                    num = int(input("Número do avião: "))
                    break
                except:
                    print("Opção inválida")
            while True:
                try:
                    desc = str(input("Descrição do avião: "))
                    break
                except:
                    print("Opção inválida")
            
            aviao = {'Número': num, 'Descrição': desc}
            fila.enfileirar(aviao.copy())
        sleep(0.7)

    elif opc == 4:
        if fila.filaVazia():
            print("Não há nenhum avião na pista!")    
            sleep(0.7)    
        else:
            print('--- Fila de espera ---')
            for i in range(fila.numeroElementos):
                print(f"{i+1}º Nº {fila.valores[i]['Número']}, Descrição: {fila.valores[i]['Descrição']}")
            opc1 = int(input('''Deseja liberar para decolagem? 
            [1] Sim
            [2] Não
            Resposta: '''))
            if opc1 == 1:
                print(f"Avião {fila.valores[0]['Número']} saindo da pista de pouso")
                fila.desenfileirar()
                
            elif opc1 == 2:
                print("Tudo bem!")
        sleep(0.7)
    
    elif opc == 5:
        if fila.filaVazia():
            print("Não há nenhum avião na pista!")
            sleep(0.7)
        else:
            print(f'''Característica do primeiro avião da pista:
            Nº: {fila.valores[0]['Número']}
            Descrição: {fila.valores[0]['Descrição']}''')
        sleep(0.7)

    elif opc == 6:
        print("Fim do programa!")
        i = 6
