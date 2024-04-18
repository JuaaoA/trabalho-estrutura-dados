class DoublyLinkedListIterator:
    # métodos ou funções que manipulam o comportamento do objeto
    def __init__(self, data, nextNode=None):
        # atributos, propriedades ou estados
        self.firstNode #(guarda o endereço/referência/valor do primeiro Node)
        self.lastNode #(guarda o endereço/referência/valor do ultimo Node)
        self.iterator #(guarda o endereço/referência do Node sob o iterador)
        self.size #(guarda o número de elementos da Lista)

    # métodos ou funções que manipulam o comportamento do objeto
    def __init__(self, firstNode=None):
        it: itertator
    
    def insNode(self, data): # insere Node antes do it e it fica neste Node
        pass
    def addNode(self, data): # add Node depois do it e it fica neste Node
        pass
    def elimNode(self): # elimina Node sob it e it avanca p/ prox Node
        pass
    def first_Node(self): # coloca o it sobre o primeiro Node da Lista
        pass
    def last_Node(self): # coloca o iterador sobre o útlimo Node da Lista
        pass
    def nextNode(self): # avança it uma posição para frente. Se it no lastNode , it=None
        pass
    def antNode(self): # avança it uma posição para trás. Se it no firstNode, it=None
        pass
    def posNode(self, position): # poe it em <=1 pos <=size, senao it=None
        pass
    def undefinedIterator(self): # True se o it =None e False o contrario
        pass