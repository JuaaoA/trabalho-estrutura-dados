from Classes.Biblioteca.EstruturaDados.Fila import *
from Classes.Biblioteca.EstruturaDados.Pilha import *
from Classes.Biblioteca.Emprestimo import Emprestimo
import random
import datetime
from Classes.Biblioteca.Gerador import *

class Livro:
    
    # Construtor nível
    def __init__(self, titulo, autor, ano, editora, cidade) -> None:
        
        # Colocar propriedades
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.cidade = cidade

        # Fila de reservas
        self.emprestimos = self.Gerar_Fila()

        # Pilha de histórico
        self.historico = self.Gerar_Historico()
    

    def Gerar_Historico(self):
        # Criar pilha do historico
        pilha_historico = ArrayStack()

        # Começar com uma data fixa
        dia = 1
        mes = 1
        ano = datetime.date.today().year

        # Iniciar a criação do historico
        for cont in range(0, 20):

            # Gerar um nome para a pilha de historico
            nome_escolhido = GerarNomeAleatorio()

            # Gerar uma classe de emprestimo
            novo_historico = Emprestimo(nome_escolhido)

            # Iniciar com uma data de empréstimo
            data_inicio = f"{dia}-{mes}-{ano}"

            # Aumentar alguns dias antes de gerar a data de devolução
            dias_a_aumentar = random.randint(1, 8)

            # Caso os dias a aumentar ultrapassem 31
            if (dia + dias_a_aumentar > 31):

                # Aumentar 1 mês
                mes += 1

                # Definir o dia do proximo mês
                dia = dias_a_aumentar - (31 - dia)
            
            # Definir a data de devolução do livro
            data_fim = f"{dia}-{mes}-{ano}"

            # Adicionar as datas ao emprestimo
            novo_historico.data_emprestimo = data_inicio
            novo_historico.data_devolucao = data_fim

            # Adicionar emprestimo a pilha de historicos
            pilha_historico.push(novo_historico)
        
        return pilha_historico


    def Gerar_Fila(self):
        # Gerar fila
        fila_reservas = ArrayQueue()

        for cont in range(0, 20):
            # Escolher um nome para entrar na fila
            nome_escolhido = GerarNomeAleatorio()

            # Criar uma nova reserva para entrar na fila
            nova_reserva = Emprestimo(nome_escolhido)

            # Caso seja o primeiro da fila
            if (cont == 0):
                
                hoje = datetime.date.today()

                # Definir uma data em que foi emprestado
                nova_reserva.data_emprestimo = f"{hoje.day}-{hoje.month}-{hoje.year}"

            # Colocar a reserva na fila
            fila_reservas.enqueue(nova_reserva)
        
        # Retornar a fila
        return fila_reservas


    
if __name__ == "__main__":

    livro = Livro("Viagem", "Cleber", 2002, "foda", "fortal", 1,)  


