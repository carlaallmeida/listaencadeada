# criando a classe o Nó
class Node:
    def __init__(self, dado = 0, next_nodo = None):
        self.dado = dado
        self.next = next_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.next)
        
# criação da lista encadeada 
class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str (self.inicio) + "]"
        
# Criando a Função para adicionar um Elemento    

    def insert(self):
        dado = input("Digite um número:")
        node = Node()
        node.dado = dado
        node.next = self.head
        self.head = node

# Criando a Função para Mostrar a Lista
    def exibir(self):
        exibir_lista = self.head
        while exibir_lista:
            print(exibir_lista)
            exibir_lista = exibir_lista.next

# Função para Sair da Lista

    def sair(self):
        print("...Saindo da lista...")
        exit()

lista = Linkedlist ()

while True:
    print("1. Criar uma nova lista")
    print("2. Mostrar a lista")
    print("3. Sair da Lista")
    menu = int(input("Escolha uma opção:"))

    if menu == 1:
       lista.insert()
       print("Numero adicinado com Sucesso!!!")
    elif menu == 2:
       lista.exibir()
    elif menu == 3:
       lista.sair()
    


