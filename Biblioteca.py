# Importar Classes
from Classes.Biblioteca.EstruturaDados.Fila import *
from Classes.Biblioteca.EstruturaDados.Pilha import *
from Classes.Biblioteca.EstruturaDados.Lista_Dupla_Encadeada import *
from Classes.Biblioteca import Gerador
import random
from Classes.Biblioteca.Livro import *
from Classes.Biblioteca.Emprestimo import *

# Funções

# Função para carregar os livros
def Carregar_Livros():
    
    # Iniciar uma lista dupla encadeada para os livros
    livros_criar = Lista_Dupla_Encadeada()

    # Para cada letra da lista
    for cont_letra in range(0, 25):
        
        # Gerar 10 livros por inicial de letra
        for c in range(0, 10):

            # Gerar um novo nome de livro
            titulo_livro = f"{random.choice(Gerador.GetNome_Livros()[cont_letra])} {random.choice(random.choice(Gerador.GetNome_Livros()))} {random.choice(random.choice(Gerador.GetNome_Livros()))}"

            # Gerar um autor para esse livro
            autor_livro = f"{random.choice(Gerador.GetNomes())} {random.choice(Gerador.GetSobrenomes())}"

            # Gerar um ano para esse livro
            ano_livro = random.randint(1950, 2024)

            # Gerar Editora para esse livro
            editora_livro = f"{random.choice(Gerador.GetNome_Livros())} {random.choice(Gerador.GetCidades())}"

            # Definir cidade para esse livro
            cidade_livro = random.choice(Gerador.GetCidades())

            # Criar um novo livro com o que foi gerado
            novo_livro = Livro(titulo_livro, autor_livro, ano_livro, editora_livro, cidade_livro)

            # Colocar livro na lista
            livros_criar.addNode(novo_livro)
    
    # Retornar a lista encadeada completa
    return livros_criar
            


# Função para imprimir uma linha usando um determinado estilo e tamnho
def linha(estilo, tamanho):
    print(estilo * tamanho)

# Função para apresentar o programa ao usuário
def apresentacao():

    # Cabeçalho
    linha("=-=", tamanho_linha)
    print("Biblioteca")
    linha("=-=", tamanho_linha)

    # Nomes
    print("""João Augusto Tolentino Santana\nMarcela Varejão Gomes""")

    # Linha para divisão para as opções do menu
    linha("=-=", tamanho_linha)


def opcoes():
    print("""    1 - Consultar Livros
    2 - Marcar livro como devolvido
    3 - Criar nova reserva
    4 - Criar novo livro
    5 - Sair""")
    linha("=-=", tamanho_linha)


def consultar_livros():

    # Variáveis globais
    global livros

    # Iniciar livros no primeiro nó
    livros.first_Node()

    # Variável para contar os livros em indices
    contador = 1
    while (livros.iterator):

        # Imprimir livros
        print(f"Livro {contador} - {livros.iterator.data.titulo} / Autor: {livros.iterator.data.autor}")

        # Ir para o proximo nó
        livros.nextNode()

        # Ir para o proximo indice
        contador += 1

    pass


def menu():
    # Mostrar as opções
    opcoes()

    # Deixar o usuário escrever
    while (True):    

        # Tratamento de erro
        try:
            resposta = input(">>> ")
        except KeyboardInterrupt:
            # Avisar que o programa será interrompido e sair
            print("\nPROGRAMA INTERROMPIDO: Encerrando...")
            exit()
        
        # Caso resposta seja um número
        if (resposta.isnumeric()):

            # Converter para um número inteiro
            resposta = int(resposta)

            # Caso a resposta esteja entre o range das opções
            if (1 <= resposta <= 5):
                break
    
    # APOS escolher, decidir o que fazer de acordo com a resposta
        
    # SAIR DO PROGRAMA
    if (resposta == 5):
        return False        
    
    # OUTROS
    if (resposta == 1):
        consultar_livros()
    
    linha("=-=", tamanho_linha)

    return True


# Iniciar Código
if __name__ == '__main__':

    # Definir tamanho de linha fixo
    tamanho_linha = 25

    # Carregar todos os livros
    livros = Carregar_Livros()

    # Iniciar a apresentação
    apresentacao()

    # Indicar pro programa continuar rodando
    continuar = True
    while (continuar):
        # Mostrar o menu
        continuar = menu()
    pass