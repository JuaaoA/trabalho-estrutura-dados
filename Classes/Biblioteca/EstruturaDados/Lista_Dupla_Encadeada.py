class IteratorNode:

    def __init__(self, data, nextNode=None, antNode=None):

        # Propriedades
        self.data = data
        self.nextNode = nextNode
        self.antNode = None

        pass

class Lista_Dupla_Encadeada:
    # métodos ou funções que manipulam o comportamento do objeto
    def __init__(self, data, nextNode=None):
        # atributos, propriedades ou estados
        self.firstNode #(guarda o endereço/referência/valor do primeiro Node)
        self.lastNode #(guarda o endereço/referência/valor do ultimo Node)
        self.iterator #(guarda o endereço/referência do Node sob o iterador)
        self.size #(guarda o número de elementos da Lista)

    # métodos ou funções que manipulam o comportamento do objeto
    def __init__(self, firstNode=None):
        
        # Adicionar atributos dos nós
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode

        # Colocar tamanho do node
        if (firstNode):
            self.size = 1
        else:
            self.size = 0

    
    def insNode(self, data): # insere Node antes do it e it fica neste Node
        
        # Criar um novo nó
        newNode = IteratorNode(data, self.iterator.data)

        #  Caso o nó esteja vazio
        if (self.size == 0):

            # Determinar o novo nó como o primeiro
            self.firstNode = newNode

            # Determinar o novo nó como o ultimo
            self.lastNode = newNode

            # Determinar o Iterator para esse nó
            self.iterator = newNode
        
        # Caso o iterator esteja na primeira posição
        elif (self.iterator == self.firstNode):
            # Definir o proximo node como o antigo primeiro
            newNode.nextNode = self.firstNode

            # Definir o novo nó como primeiro
            self.firstNode = newNode
            
            # Definir node anterior como vazio
            newNode.antNode = None
            
            # Colocar o iterador no primeiro node
            self.iterator = newNode
            pass

        # Caso o iterator esteja no meio da lista
        else:
            # Iniciar em um node inicial
            currentNode = self.firstNode

            while currentNode.nextNode != self.iterator:
                # Percorrer a lista
                currentNode = currentNode.nextNode
            
            # Determina o node anterior e próximo do novo nó
            newNode.nextNode = self.iterator
            newNode.antNode = self.currentNode

            # Determina o proximo node do anterior
            currentNode.nextNode = newNode

            # Determina o anterior do iterador
            self.iterator.antNode = newNode    

            # Poe o iterador no novo nó
            self.iterator = newNode

        # Aumentar tamanho do nó em 1
        self.size += 1        
        pass


    def addNode(self, data): # add Node depois do it e it fica neste Node
        
        # Criar classe do novo nó
        newNode = IteratorNode(data, None)

        if (self.size == 0):

            # Determinar as propriedades como o novo nó
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        
        # Caso o iterator esteja no final
        elif (self.iterator == self.lastNode):
            
            # Determinar o node anterior do novo
            newNode.antNode = self.lastNode

            # Determinar o proximo node do ultimo
            self.lastNode.nextNode = newNode

            # Determinar o novo nó como o ultimo
            self.lastNode = newNode

            # Por o iterador no ultimo nó
            self.iterator = newNode
        
        # Caso o iterador esteja no meio da lista
        else:
            # Determinar o proximo do novo nó o proximo do iterator
            newNode.nextNode = self.iterator.nextNode

            # Determinar o anterior do novo nó o iterator
            newNode.antNode = self.iterator

            # Determinar o novo proximo do iterator
            self.iterator.nextNode = newNode

            # Definir o iterador para o novo
            self.iterator = newNode
        
        self.size += 1
        return True


    def elimNode(self): # elimina Node sob it e it avanca p/ prox Node
        
        # Caso o iterator esteja no primeiro node
        if (self.iterator == self.firstNode):
            
            # Caso o iterator também seja o ultimo
            if (self.iterator == self.lastNode):

                # Apontar todos para nada
                self.lastNode = None
                self.iterator = None
                self.firstNode = None
            
            # Se não, significa que possui mais de um nó na lista
            else:

                # O primeiro nó será o proximo
                self.firstNode = self.firstNode.nextNode

                # Isolar nó
                self.iterator.nextNode = None

                # Iterador apontará para o novo primeiro
                self.iterator = self.firstNode
        
        # Iterator não está no primeiro node
        else:

            # Pegar node anterior
            anterior =  self.iterator.antNode

            # Caso o iterator seja o ultimo nó
            if (self.iterator == self.lastNode):
                
                # Não definir um próximo ao ultimo nó
                anterior.nextNode = None

                # Definir o anterior como ultimo nó
                self.lastNode = anterior

                # Isonar o antigo ultimo nó
                self.iterator.nextNode = None
                self.iterator.antNode = None

                # Indefinir o iterator
                self.iterator = None
            
            # Se não, o iterador está dentro da lista
            else:

                # Definir o próximo do anterior o proximo do iterator
                anterior.nextNode = self.iterator.nextNode

                # Guardar o nó que vai ser eliminado
                anterior = self.iterator

                # Definir o iterador no próximo nó
                self.iterator = self.iterator.nextNode

                # Isolar o nó eliminado
                anterior.nextNode = None
                anterior.antNode = None
            
            # Diminuir tamanho da lista
            self.size = self.size - 1

            return True


    def first_Node(self): # coloca o it sobre o primeiro Node da Lista
        self.iterator = self.firstNode
        return True
    
    def last_Node(self): # coloca o iterador sobre o útlimo Node da Lista
        self.iterator = self.lastNode
        return True
    
    def nextNode(self): # avança it uma posição para frente. Se it no lastNode , it=None
        if (self.iterator):
            self.iterator = self.iterator.nextNode
        return True
    
    def antNode(self): # avança it uma posição para trás. Se it no firstNode, it=None
        if (self.iterator):

            if (self.iterator.antNode != None):
                self.iterator = self.iterator.antNode
            else:
                self.iterator = None
            
        return True
            
    def posNode(self, position): # poe it em <=1 pos <=size, senao it=None
        # Caso a posição esteja dentro do tamanho do node
        if (position > 0 and position <= self.size):

            # Variável contadora
            i = 1

            # Começar com o iterador no primeiro nó
            self.first_Node()

            # Enquanto o contador não chega na posição indicada
            while (i < position):
                
                # Caso o proximo nó não esteja vazio
                if (self.iterator.nextNode != None):

                    # Proximo nó
                    self.iterator = self.iterator.nextNode
                    
                    # Aumentar em um a posição
                    i += 1
        
        # Caso a posição esteja fora do node
        else:

            # Deixar o iterator vazio
            self.iterator = None
        

    def undefinedIterator(self): # True se o it =None e False o contrario
        # Faz mais sentido retornar direto
        return not (self.iterator == None)