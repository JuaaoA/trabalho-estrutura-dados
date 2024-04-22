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
            editora_livro = f"{random.choice(random.choice(Gerador.GetNome_Livros()))} {random.choice(Gerador.GetCidades())}"

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
    2 - Criar nova reserva
    3 - Criar novo livro
    4 - Sair""")
    linha("=-=", tamanho_linha)


def criar_nova_reserva():
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

    # Cabeçalho
    linha("=-=", tamanho_linha)
    print("\tDigite um indice para adicionar uma reserva\nDigite 0 para voltar ao menu")
    linha("=-=", tamanho_linha)

    # Fazer o usuário colocar uma resposta
    resposta = escolha_range(0, livros.size)

    # Decidir o que fazer
    if (resposta == 0):
        return
    
    # Criar reserva
    else:

        linha("=-=", tamanho_linha)

        # Solicitar o nome do usuário
        nome_reserva = input("Digite o seu nome: ")

        # Criar uma reserva de empréstimo
        reserva = Emprestimo(nome_reserva)

        # Colocar o iterador na posição indicada
        livros.posNode(resposta)

        # Inserir a reserva
        livros.iterator.data.emprestimos.push(reserva)

        # Indicar ao usuário que foi bem sucedido
        linha("=-=", tamanho_linha)
        print("Sucesso com a reserva!")



def criar_novo_livro():

    # Pedir para o usuário digitar todas as informações do novo livro
    linha("=-=", tamanho_linha)

    nome_livro = input("Digite o nome para o novo livro: ")

    linha("=-=", tamanho_linha)

    autor_livro = input("Digite o autor para o novo livro: ")

    linha("=-=", tamanho_linha)

    ano_livro = int(input("Digite o Ano de publicação do novo livro: "))

    linha("=-=", tamanho_linha)

    editora_livro = input("Digite a editora para o novo livro: ")

    linha("=-=", tamanho_linha)
    
    cidade_livro = input("Digite a cidade para o novo livro: ")

    linha("=-=", tamanho_linha)

    # Adicionar ao nó
    livros.addNode(Livro(nome_livro, autor_livro, ano_livro, editora_livro, cidade_livro))

    # Mostrar ao usuário que foi feito com sucesso
    print("O livro foi criado com sucesso e já está nas prateleiras!")
    input("Pressione ENTER para retornar...")


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
    
    """
    Colocar todo o caminho para consultar dentro de cada livro
    """

    # Cabeçalho
    linha("=-=", tamanho_linha)
    print("\tDigite um indice para consultar um livro\nDigite 0 para voltar ao menu")
    linha("=-=", tamanho_linha)

    

    # Contador atualmente guarda todo o tamanho dos livros
    resposta = escolha_range(0, livros.size)
    
    # Decidir o que fazer de acordo com o que o usuário colocou            
    # Sair
    if (resposta == 0):
        return
    
    # Consultar o livro
    else:

        # Por o iterator dos livros na posição correta
        livros.posNode(resposta)

        # Mostrar detalhes do livro de acordo com a posicão do iterador
        detalhes_livro()

        # Linha
        linha("=-=", tamanho_linha)

        # Mostrar ações
        print(
        """
            1 - Consultar reservas de empréstimos
            2 - Consultar histórico de empréstimos
        """)

        # Linha
        linha("=-=", tamanho_linha)

        # Usuário decidirá o que mostrar
        resposta = escolha_range(1, 2)

        # Linha
        linha("=-=", tamanho_linha)

        # Realizar ações
        if (resposta == 1):
            mostrar_reservas()
        else:
            mostrar_historico()
        
        # Linha
        linha("=-=", tamanho_linha)
        
        # Esperar o usuário pressionar enter após visualizar
        input("Pressione Enter para finalizar...")


# Mostra todas as reservas do livro em específico que está no iterator
def mostrar_reservas():

    # Pegar dados desse livro
    dado_livro = livros.iterator.data

    # Gerar uma cópia das reservas
    copia_reservas = dado_livro.emprestimos.criar_copia()

    # Imprimir todas as reservas
    contador = 1
    while not (copia_reservas.is_empty()):

        # Pegar uma liha
        linha = copia_reservas.dequeue()

        # Mostrar Reserva
        print(f"{contador} - {linha.nome_pessoa}")

        # Aumentar o contador em 1
        contador += 1


# Mostra o histórico de empréstimo do livro em específico que está no iterator
def mostrar_historico():

    # Pegar dados desse livro
    dado_livro = livros.iterator.data

    # Gerar uma cópia dos emprestimos já feitos
    copia_historico = dado_livro.historico

    # Enquanto a pilha ta cheia
    contador = 1
    while not (copia_historico.is_empty()):
        
        # Elemento retirado da pilha
        retirado = copia_historico.pop()

        # Mostrar na tela
        print(f"{contador} - {retirado.nome_pessoa}\n\tData Empréstimo: {retirado.data_emprestimo}\n\tData Devolução: {retirado.data_devolucao}\n")

        # Incrementar 1 ao contador
        contador += 1


# Pede para que o usuário digite um valor para selecionar, e tratará todos os erros
def escolha_range(inicio, fim):
    # Iniciar variavel sem valor
    resposta = ""
    
    # Loop para a resposta
    while (True):
        
        # Tratamento de erros
        try:
            resposta = input(">>> ")

            # Verificar se resposta é um número
            if (resposta.isnumeric()):

                # Converter para inteiro
                resposta = int(resposta)

                # Verificar se está dentro do range
                if (inicio <= resposta <= fim):
                    # Sair do loop
                    break

        # Tratar erro de sair inesperadamente      
        except KeyboardInterrupt:
            # Interromper o programa ao acontecer uma interrupção de teclado
            print("\nPROGRAMA INTERROMPIDO: Encerrando...")
            exit()
    
    # Retornar a resposta
    return resposta

# Mostra o livro que está no iterator
def detalhes_livro():

    # Para facilitar, pegar dados do livro no iterador
    dado_livro = livros.iterator.data

    linha("=-=", tamanho_linha)

    # Imprimir todos os detalhes do livro
    print(f"""
    Titulo: {dado_livro.titulo}
    Autor: {dado_livro.autor}
    Editora: {dado_livro.editora}

    Publicado em {dado_livro.ano} em {dado_livro.cidade}
    """)


def menu():
    # Mostrar as opções
    opcoes()

    # Deixar o usuário escrever
    resposta = escolha_range(1, 5)
    
    # APOS escolher, decidir o que fazer de acordo com a resposta
        
    # SAIR DO PROGRAMA
    if (resposta == 4):
        return False        
    
    # OUTROS
    if (resposta == 1):
        consultar_livros()
    elif (resposta == 2):
        criar_nova_reserva()
    elif (resposta == 3):
        criar_novo_livro()
    
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