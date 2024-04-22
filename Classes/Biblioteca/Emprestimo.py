class Emprestimo:

    def __init__(self, data_emprestimo, data_devolucao, nome_pessoa) -> None:

        # Propriedades
        self.nome_pessoa = nome_pessoa
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
    
    def __init__(self, nome_pessoa) -> None:

        # Propriedades
        self.nome_pessoa = nome_pessoa
        self.data_emprestimo = None
        self.data_devolucao = None